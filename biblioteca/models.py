from django.db import models

class autor(models.Model):
    nombre = models.CharField()
    lugar_nacimiento = models.CharField()
    fecha_nacimiento = models.DateTimeField()
    
    def __str__(self):
        return self.nombre
    
class libro(models.Model):
    titulo = models.CharField()
    descripcion = models.TextField()
    autor_id = models.ForeignKey(autor,primary_key=id,on_delete=models.CASCADE)
    def __srt__(self):
        return self.Titulo
    
    
    
    
