from django.db import models

# Create your models here.
# Model parent class from models
# เป็นการสร้างตารางฐานข้อมูล data table


class Post(models.Model):
    # field_name = models.FieldType()
    # variable name
    # title shouldn't greater than 80 character.
    title = models.CharField(max_length=80)
    # google suggest 160 character.
    description = models.TextField(max_length=160)
    body = models.TextField()  # content
    # creat and update time
    # autofill datetime => add argument auto_now_add=True
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title