from django.db import models

class Category(models.Model):

    """ This holds the category detail of the food"""

    name = models.CharField(max_length =150, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

 
class Unit(models.Model):

    """ This holdes the measurement unit"""
    name = models.CharField(max_length =150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Measure"
        verbose_name_plural = "Measurements"


class Ingridient(models.Model):

    """ This holdes the ingriedent"""

    name = models.CharField(max_length =150, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ingridient"
        verbose_name_plural = "Ingridients"

class IngridientList(models.Model):
    """This holds the list of ingridinets """
    ingridient = models.ForeignKey(Ingridient)
    unit = models.ForeignKey(Unit)
    dish = models.ForeignKey('Dish')

    def __str__(self):
        return self.dish.name

    class Meta:
        verbose_name = "Ingridient List"
        verbose_name_plural = "Ingridient Lists"


class Dish(models.Model):
    """ This holds the details of the dish """
    name = models.CharField(max_length=150,unique=True)
    total_time = models.FloatField()
    # image = models.ImageField(upload_to="media")
    category = models.ForeignKey(Category)
    type_choice = ((0, "veg"),(1, "non-veg"))
    type = models.IntegerField(default=0,choices=type_choice)
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes" 


class step(models.Model):
    """ This holds the details of the step for the dish"""

    step_name = models.CharField(max_length=150)
    time = models.FloatField()
    dish = models.ForeignKey(Dish)
    def __str__(self):
        return self.dish.name + " " + self.step_name
    class Meta:
        unique_together = ('dish', 'step_name')
