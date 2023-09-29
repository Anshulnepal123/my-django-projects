from django.contrib import admin

from myapp.models import BlogPost, Login

admin.site.register(BlogPost)
admin.site.register(Login)
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id','title','content')

