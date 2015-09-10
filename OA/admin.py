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

admin.site.register(Project)
admin.site.register(DecorationContract)
admin.site.register(Supplier)
admin.site.register(SupplierType)

