from django.db import models

class Tree(models.Model):
    species_name = models.CharField(max_length=255)
    number_of_trees = models.IntegerField()
    age = models.IntegerField()
    height = models.FloatField()
    width = models.FloatField()

    def __str__(self):
        return self.species_name
