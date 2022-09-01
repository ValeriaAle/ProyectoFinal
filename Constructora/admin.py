from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(cliente)

admin.site.register(ficha_tecnica)

admin.site.register(Casa)

