from django.contrib import admin
from .models import regard, Report


class regardAdmin(admin.ModelAdmin):
    list_display = ('id','address')
    list_display_links = ('id','address')
    search_fields = ('id','address')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id','regard_id','quarter', 'profit', 'expense', 'products')
    list_display_links = ('id','regard_id')

admin.site.register(regard, regardAdmin)
admin.site.register(Report, ReportAdmin)