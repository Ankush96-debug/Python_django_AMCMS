from django.contrib import admin
from home.models import basetable,project_table,vendor_table,expired_table
# Register your models here.

admin.site.register(basetable)
admin.site.register(project_table)
admin.site.register(vendor_table)
admin.site.register(expired_table)