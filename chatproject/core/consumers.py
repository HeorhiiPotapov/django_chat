import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from .models import Message, Room


class ChatConsumer(WebsocketConsumer):

    def get_room(self):
        return Room.objects.get(name=self.room_name)

    def last_messages(self, data):
        room = self.get_room()
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(Message.last_messages().filter(room=room.id))
        }
        self.send_message(content)

    def new_message(self, data):
        sender = self.scope['user']
        sender_user = User.objects.filter(username=sender)[0]
        room = self.get_room()
        message = Message.objects.create(
            sender=sender_user, text=data['message'], room=room)
        text = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(text)

# ========= serialize multiple messages ===========
    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

# ========= work with one message from multiple messages ======
    def message_to_json(self, message):
        room = self.get_room()
        return {
            'room': room.id,
            'sender': message.sender.username,
            'text': message.text,
            'created': str(message.created.strftime("%H:%m"))
        }
# ============ end serializer =============

    commands = {
        'last_messages': last_messages,
        'new_message': new_message
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        Room.objects.get_or_create(name=self.room_name)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))
