from django.db import models

# Create your models here.
class Servicio(models.Model):
    id_servicio     =models.AutoField(db_column='idSERVICIO', primary_key=True)
    precio          =models.IntegerField()
    foto            =models.ImageField(upload_to="servicios", null=True)
    descripcion     =models.CharField(max_length=200)

    def _str_(self):
        return str(self.id_servicio)+" "+str(self.descripcion)