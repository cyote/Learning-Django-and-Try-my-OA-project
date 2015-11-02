from django.contrib import admin

# Register your models here.
from models import Project, DecorationContract, SupplierType, Supplier

# admin.site.register(Question)

'''
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)


admin.site.register(Choice)
'''
#class SupplierInline(admin.TabularInline):
   # model = Supplier
    #extra = 5

'''
class ProjectAdmin(admin.ModelAdmin):
    inlines = [SupplierInline]
'''

#class SupplierTypeAdmin(admin.ModelAdmin):
    #inlines = [SupplierInline]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('proj_code','Proj_name', 'adr_txt', 'sign_date', 'rent', 'landlord', )
    list_filter = ('proj_code','Proj_name' )

class DecorationContractAdmin(admin.ModelAdmin):
    list_display =('school_name', 'proj_name', 'proj_type', 'supplier', 'sign_date', 'price')
    list_filter =('school_name', 'proj_name', 'proj_type', 'supplier', 'sign_date', 'price')

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'supplier_account', 'supplier_account_bank', 'supplier_Type')

admin.site.register(Project, ProjectAdmin)
admin.site.register(DecorationContract, DecorationContractAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(SupplierType)

