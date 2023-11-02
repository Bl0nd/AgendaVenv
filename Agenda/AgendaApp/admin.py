from django.contrib import admin
from AgendaApp.models import Contato,Cidade, Telefone

# Classe para exibir Telefones ao cad de contato
class Telefones(admin.StackedInline):
    model: Telefone

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'data_nascimento']
    list_filter = ['data_nascimento', 'cidade', 'estado']
    search_fields = ['nome', 'apelido']
    inlines = [Telefones]

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Cidade)
admin.site.register(Telefone)