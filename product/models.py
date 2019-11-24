from django.db import models


class Category(models.Model):

    CellPhone = 1
    Laptop = 2
    types = [(CellPhone, 'cell_phone'), (Laptop, 'laptop')]

    name = models.CharField(max_length=25)
    cat_type = models.IntegerField(choices=types)

    def __str__(self):
        return str(self.pk) + " => " + self.name


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    Category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category")
    price = models.IntegerField()
    weight = models.PositiveIntegerField()

    def __str__(self):
        return  str(self.pk) + " => "+self.name
