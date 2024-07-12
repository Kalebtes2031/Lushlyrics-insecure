from django.contrib import admin
from .models import playlist_user, playlist_song
from main.models import User

# Register your models here.
admin.site.register(playlist_user)
admin.site.register(playlist_song)