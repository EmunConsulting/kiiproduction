
from django.contrib import admin
from .models import Profile, Post, Comment, Like, FriendRequest, Message, Notification, Group, GroupPost, Event, ActivityLog, Media, Story

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(FriendRequest)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Group)
admin.site.register(GroupPost)
admin.site.register(Event)
admin.site.register(ActivityLog)
admin.site.register(Media)
admin.site.register(Story)
