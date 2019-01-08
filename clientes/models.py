from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photos = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    #Ao invés de exibir no django admin "object1, object2, etc" exibe nome e sobrenome ou o dado que eu quiaser
    def __str__(self):
        return self.first_name + ' ' + self.last_name