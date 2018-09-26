from django.contrib import admin

from .models import News, Comments

admin.site.register(News)
admin.site.register(Comments)
admin.site.site_url = 'http://localhost:3000/home/'
