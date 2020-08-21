from django.contrib import admin
from .models import Message, Profile, Room


class MessagesInline(admin.TabularInline):
    model = Message
    extra = 1


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [MessagesInline, ]


admin.site.register(Profile)
