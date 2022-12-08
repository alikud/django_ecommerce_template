from django.db import models
from users.models import User
# Create your models here.
import uuid

class Category(models.Model):
    """Canban column category, e.g to-do, on review"""
    name = models.CharField(max_length=36)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    """Canban tag to task, e.g frontend, mobile, bug"""
    name = models.CharField(max_length=36)

    def __str__(self):
        return self.name


class AbstractTask(models.Model):
    """Общая абстрактная модель объявления"""
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_add_post = models.DateTimeField(auto_now_add=True, blank=True)
    date_correct = models.DateTimeField(auto_now=True, blank=True)
    tags = models.ManyToManyField(Tags)
    text = models.TextField(blank=True)

    class Meta:
        abstract = True


class Task(AbstractTask):
    def __str__(self):
        return 'name:{} , category is: {}, tags is: {} uuid: {}'.format(self.name,
                                                                        self.category,
                                                                        self.tags,
                                                                        self.uuid)

class Subsciber(models.Model):
    """Модель подписчика на объявления"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscriber_of = models.ForeignKey(Task, max_length=255, on_delete=models.CASCADE)
