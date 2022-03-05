from django.contrib import admin
from . models import *

# Register your models here.
class categAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(categ,categAdmin)

class ProductfreeAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','img','paid_or_free']
    list_editable = ['price','stock','img']
    prepopulated_fields = {'slug':('name',)}
  
admin.site.register(ProductFree,ProductfreeAdmin)
