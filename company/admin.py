from django.contrib import admin
from .models import Post
# เข้าถึงผ่าน .
# Register your models here.

# เพื่อให้แสดงใน admin
admin.site.register(Post)
