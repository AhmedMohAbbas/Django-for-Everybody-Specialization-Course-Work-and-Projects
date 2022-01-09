from django.contrib import admin

# Register your models here.
from .models import Make

admin.site.register(Make)

from .models import Auto

admin.site.register(Auto)