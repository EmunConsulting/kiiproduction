from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import Room, Message, PrivateMessage, PrivateChat


# Register your models here.

class RoomAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'slug',)
    search_fields = ('name', 'slug',)
    ordering = ('id',)


class MessageAdmin(ImportExportModelAdmin):
    list_display = ('id', 'content', 'user', 'room', 'created_on',)
    search_fields = ('content', 'user', 'room',)
    ordering = ('id',)


class PrivateMessageAdmin(ImportExportModelAdmin):
    list_display = ('id', 'chat', 'sender', 'content', 'created_on',)
    search_fields = ('chat', 'sender', 'content')
    ordering = ('id',)


class PrivateChatAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user1', 'user2', 'created_on',)
    search_fields = ('user1', 'user2')
    ordering = ('id',)


admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(PrivateMessage, PrivateMessageAdmin)
admin.site.register(PrivateChat, PrivateChatAdmin)

