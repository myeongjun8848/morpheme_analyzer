from django.contrib import admin
from .models import PosTag

class PosTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'description', 'analyzer')

admin.site.register(PosTag, PosTagAdmin)
