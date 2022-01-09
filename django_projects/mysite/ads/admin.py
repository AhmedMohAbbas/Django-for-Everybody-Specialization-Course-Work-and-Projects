from django.contrib import admin

# Register your models here.
from .models import Ad, Comment, Fav
admin.site.register(Ad)
admin.site.register(Comment)
admin.site.register(Fav)