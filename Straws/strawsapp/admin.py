from django.contrib import admin
from .models import TablesHistoryDatabase,TableForm1,TableForm2,TableForm3,TableForm4,TableForm5,TableForm6,TableForm7,TableForm8,TableForm9,TableForm10
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

@admin.register(TableForm4)
class TableFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_number','items','total_amount','payment_mode']

@admin.register(TableForm5)
class TableFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_number','items','total_amount','payment_mode']

@admin.register(TableForm6)
class TableFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_number','items','total_amount','payment_mode']

@admin.register(TableForm7)
class TableFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_number','items','total_amount','payment_mode']

@admin.register(TableForm8)
class TableFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_number','items','total_amount','payment_mode']

@admin.register(TableForm9)
class TableFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_number','items','total_amount','payment_mode']

@admin.register(TableForm10)
class TableFormAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_number','items','total_amount','payment_mode']