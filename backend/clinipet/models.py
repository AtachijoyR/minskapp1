from django.db import models

# Create your models here.

class Pet(models.Model):

    pet_choices = (
        ('0', 'Sano'),
        ('1', 'En Pabellon'),
        ('2', 'En Observacion'),
        ('3', 'Otro')
    )



    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age_months = models.IntegerField()
    weight = models.IntegerField()
    status = models.CharField('Estado', max_length=1,choices = pet_choices)
    specie = models.CharField(max_length=50)
    rut_owner = models.CharField(max_length=12)
    description = models.CharField(max_length=120, blank = True)
