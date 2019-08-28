from django.db import models
from django.shortcuts import reverse

SIZE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('X', 'X Size'),
    ('XXL', 'XXL Size')
)
COLOR_CHOICES = (
    ('R', 'Red'),
    ('B', 'BLUE'),
    ('BL', 'BLACK'),
    ('O', 'Orange'),
    ('P', 'Purple')
)
CATEGORY_CHOICES = (
    ('WT', 'Watches'),
    ('CL', 'Clothing'),
    ('JW', 'Jewelry'),
    ('SH', 'Shoes')
)


class Products(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.FloatField(max_length=5, blank=False)
    description = models.TextField(max_length=200, blank=False)
    size = models.CharField(max_length=3, null=True, choices=SIZE_CHOICES)
    color = models.CharField(choices=COLOR_CHOICES, max_length=2)
    slug = models.SlugField(max_length=10)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    ratings = models.IntegerField()
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shops:product", kwargs={
            'slug': self.slug
        })
