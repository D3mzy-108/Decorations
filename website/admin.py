from django.contrib import admin
from .models import *


@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    pass
