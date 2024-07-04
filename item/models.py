from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    def __str__(self):
        return self.name 