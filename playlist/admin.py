from django.contrib import admin
from .models import *

class PlaylistModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]
    search_fields = ["name"]
    class Meta:
        model = Playlist

admin.site.register(Playlist, PlaylistModelAdmin)

