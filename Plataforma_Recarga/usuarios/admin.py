from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    search_fields = ('nome', 'email')

    def save_model(self, request, obj, form, change):
        if not obj.senha.startswith('pbkdf2_'):
            obj.senha = make_password(obj.senha)

        super().save_model(request, obj, form, change)