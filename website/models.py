from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return f'{self.name} || {self.category.name}'


class Design(models.Model):
    subcategory = models.ManyToManyField(SubCategory)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    price = models.FloatField(null=True)
    image = models.ImageField(upload_to='designs/', null=True)
    delivery_fee = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.description[:50]
