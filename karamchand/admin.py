from django.contrib import admin
from .models import Case


# Register your models here.

class CaseModelAdmin(admin.ModelAdmin):
    list_display = ['entity', 'website', 'seeker_email', 'timestamp']
    list_display_links = ['website']
    list_filter = ['seeker_email', 'timestamp']
    search_fields = ['website', 'seeker_email', 'address1', 'city', 'state', 'country', 'entity']

    class Meta:
        model = Case


admin.site.register(Case, CaseModelAdmin)
