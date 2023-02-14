from django.contrib import admin
from .models import *

from django_summernote.admin import SummernoteModelAdmin
# from .models import SomeModel

# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['title','date_created','date_updated']

# เข้าถึงผ่าน .
# Register your models here.

# เพื่อให้แสดงใน admin
admin.site.register(Post,PostAdmin)
admin.site.register(ProductDemo)
admin.site.register(Contact)
admin.site.register(Book)
