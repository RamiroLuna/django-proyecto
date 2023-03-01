from django.db import models

# Create your models here.
class informacionPersonal(models.Model):
    nombre = models.CharField(max_length=30)
    apellidoPaterno = models.CharField(max_length=25)
    apellidoMaterno = models.CharField(max_length=25)
    fechaNacimiento = models.DateField()
    edad = models.PositiveSmallIntegerField()
    correoElectronico = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        texto = "{0} {1} {2} {3} {4} {5} {6}"
        return texto.format(self.nombre, self.apellidoPaterno, self.apellidoMaterno, self.fechaNacimiento, self.edad, self.correoElectronico, self.telefono)
