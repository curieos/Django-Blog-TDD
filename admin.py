from django.db import models
from django.contrib import admin
from markdownx.widgets import AdminMarkdownxWidget

from .models import Tag, Post

class MyModelAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': AdminMarkdownxWidget},
	}

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, MyModelAdmin)
