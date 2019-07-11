from django.db import models
from django.contrib import admin

<<<<<<< HEAD
from martor.widgets import AdminMartorWidget

from .models import Tag, Post

class MyModelAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': AdminMartorWidget},
	}

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, MyModelAdmin)
=======
from .models import Tag, Post

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)
>>>>>>> 9004bf328deb9a9a4f46a19a888042c1dfcd492d
