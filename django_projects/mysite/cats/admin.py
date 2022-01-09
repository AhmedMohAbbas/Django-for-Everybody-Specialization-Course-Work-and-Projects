from django.contrib import admin

# Register your models here.
from .models import Cat

admin.site.register(Cat)

from .models import Breed

admin.site.register(Breed)