from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=55)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

class Item(models.Model):
    category = models.ForeignKey(Category,related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    created_by = models.ForeignKey('auth.User',related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name