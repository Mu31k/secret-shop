from django.contrib import admin
from .models import Articles

admin.site.register(Articles)

class AuthorAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


