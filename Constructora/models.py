from django.db import models

# Create your models here.
class Casa(models.Model):
    numero= models.IntegerField()
    categoria= models.CharField(max_length=2)     
    domicilio= models.CharField(max_length=30)       
    tipo= models.CharField(max_length=30)         
    fecha_disponible= models.DateField()  
    detalle= models.CharField(max_length=300) 

    def __str__(self):
        return f"Numero: {self.numero} - Categoria:{self.categoria} - Domicilio:{self.domicilio} - Tipo:{self.fecha_disponible} - Detalle:{self.detalle}"

class Ficha_Tecnica(models.Model):
    obra= models.CharField(max_length=40)
    ubicacion= models.CharField(max_length=30)    
    superficie= models.IntegerField()    
    construccion= models.DateField()  
    plazos= models.CharField(max_length=20)

    def __str__(self):
        return f"Obra:{self.obra} - Ubicacion:{self.ubicacion} - Superficie:{self.superficie} - Construccion:{self.construccion} - Plazos:{self.plazos}"


class cliente(models.Model):
    apellido_y_nombre= models.CharField(max_length=40)
    referencia= models.CharField(max_length=20)
    telefono= models.IntegerField()
    domicilio_legal= models.CharField(max_length=30)

    def __str__(self):
        return f"Apellido y Nombre: {self.apellido_y_nombre} - Referencia: {self.referencia} - Telefono: {self.telefono} - Domicilio legal: {self.domicilio_legal}"
