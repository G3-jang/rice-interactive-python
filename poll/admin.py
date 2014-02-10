from django.contrib import admin
from poll.models import Poll,Choice,State,Saletype

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class PollAdmin(admin.ModelAdmin):
    list_display = ('question',)
    #list_filter = ['pub_date']
    search_fields = ['question']



   # fieldsets = [
    #    (None,               {'fields': ['question']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
   # ]
   # inlines = [ChoiceInline]
   
class StateAdmin(admin.ModelAdmin):
    list_display = ('state_name','state_abbr',)

class SaleAdmin(admin.ModelAdmin):
    list_display = ('name',)



admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)
admin.site.register(State,StateAdmin)
admin.site.register(Saletype,SaleAdmin)
