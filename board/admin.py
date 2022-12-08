from django.contrib import admin

# Register your models here.
from board.models import Category, Subsciber, Tags, Task

admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Task)
admin.site.register(Subsciber)
