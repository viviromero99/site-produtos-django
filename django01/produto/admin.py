from django.contrib import admin

from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    fields = ('categoria',  'nome', 'descricao', 'slug', 'imagem', 'estoque', 'preco', 'disponivel')
    list_display = ['categoria',  'nome', 'descricao', 'slug', 'imagem', 'estoque', 'preco', 'disponivel']
    search_fields = ['nome', 'imagem']
    list_filter = ['categoria']
    list_editable = ['descricao', 'imagem', 'estoque', 'preco', 'disponivel']
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Produto, ProdutoAdmin)
