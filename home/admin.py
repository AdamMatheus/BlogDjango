from django.contrib import admin

# Register your models here.
from .models import BlogModel,Profile,Comment,Like


admin.site.register(BlogModel)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)
