from django.contrib import admin
from galeria.models import Fotografia

class LIstandoFotografia(admin.ModelAdmin):
    list_display = ('id','nome', 'publicada', 'usuario',)
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_filter = ('categoria', 'usuario',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Fotografia, LIstandoFotografia)
