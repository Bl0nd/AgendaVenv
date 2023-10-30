from django.contrib import admin
from AgendaApp.models import Contato

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'data_nascimento']
    list_filter = ['data_nascimento', 'cidade', 'estado']
    search_fields = ['nome', 'apelido']

admin.site.register(Contato, ContatoAdmin)