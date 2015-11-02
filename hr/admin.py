from django.contrib import admin

# Register your models here.
from models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_position', 'user_mail', 'user_workcode',
                    'user_school', 'user_phonenumber', 'user_salary', 'user_arrivetime',
                    'user_ID', 'user_gender', 'user_birthday', )
    list_filter = ('user_position', 'user_school', 'user_salary','user_gender' )

admin.site.register(Employee, EmployeeAdmin)