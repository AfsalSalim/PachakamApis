from django.db import models




class Ingridient(models.Model):

    """ 
        This holdes the ingriedent
    """

    name = models.CharField(max_length =250, unique=True)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ingridient"
        verbose_name_plural = "Ingridients"




class Dish(models.Model):

    """ 
        This holds the details of the dish 
    """
    
    name = models.CharField(max_length=150,unique=True)
    total_time = models.FloatField()
    image = models.ImageField(blank=True, null=True)
    type_choice = ((0, "vegeterian"),(1, "non-vegeterian"),(2,"eggiterian"))
    category = models.IntegerField(default=0,choices=type_choice)
    book = models.ForeignKey('appuser.Kitchen', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes" 


class step(models.Model):

    """ 
        This holds the details of the step for the dish
    """

    step_name = models.CharField(max_length=150)
    time = models.FloatField()
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    description = models.TextField(null=True, default=None)

    def __str__(self):
        return self.dish.name + " " + self.step_name
        
    class Meta:
        unique_together = ('dish', 'step_name')
