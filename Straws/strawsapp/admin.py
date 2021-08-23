from django.contrib import admin
from .models import TablesHistoryDatabase,TableForm1,TableForm2,TableForm3
# Register your models here.
@admin.register(TablesHistoryDatabase)
class TableFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_number','items','total_amount','payment_mode']

@admin.register(TableForm1)
class TableFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_number','items','total_amount','payment_mode']

@admin.register(TableForm2)
class TableFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_number','items','total_amount','payment_mode']

@admin.register(TableForm3)
class TableFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_number','items','total_amount','payment_mode']