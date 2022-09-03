from django import forms

class CasaFormulario(forms.Form):

      numero= forms.IntegerField()
      categoria= forms.CharField()     
      domicilio= forms.CharField()       
      tipo= forms.CharField()        
      fecha_disponible= forms.DateField()  
      detalle= forms.CharField()

class FichaFormulario(forms.Form):
      obra= forms.CharField()
      ubicacion= forms.CharField()    
      superficie= forms.IntegerField()    
      construccion= forms.DateField()  
      plazos= forms.CharField()

class ClientesFormulario(forms.Form):
     apellido_y_nombre= forms.CharField()
     referencia= forms.CharField()
     telefono= forms.IntegerField()
     domicilio_legal= forms.CharField()