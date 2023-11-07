from django.db import models

# Create your models here.
# Here we create our models to be used in html
# The class represents a table in database, after this, we will migrate our class to a database, with commando line python manage.py makemigrations and then command migrate

class Fotografia(models.Model):
    nome = models.CharField(max_length= 100, null = False, blank = False)
    legenda = models.CharField(max_length= 150, null = False, blank = False)
    descricao = models.TextField(null=False, blank = False)
    foto = models.CharField(max_length= 100, null = False, blank = False)

    # Creating a good practice
    def __str__(self):
        return f'Fotografia [nome={self.nome}]'