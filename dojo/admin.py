from django.contrib import admin
from .models import Post
# Register your models here.


admin.site.register(Post)
list_display = ['id','update_at']
