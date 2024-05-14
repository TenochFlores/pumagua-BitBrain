from django.contrib import admin

# Register your models here.
from .models import bebederos
from .models import Reporte

admin.site.register(bebederos)

admin.site.register(Reporte)