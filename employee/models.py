from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=25)  
    epaciente = models.CharField(max_length=250)  
    # efechahora = models.DateTimeField()  
    emedico = models.CharField(max_length=250) 
    edistri = models.CharField(max_length=250)
    ecolor = models.CharField(max_length=250)

    def __str__(self):
        return "%s " %(self.epaciente) 
    class Meta:  
        db_table = "employee"  

class Proveedores(models.Model):
    codigo = models.CharField(max_length=250)
    proveedore = models.CharField(max_length=250)
    contacto_tel = models.CharField(max_length=250)
    correo = models.CharField(max_length=250)

    def __str__(self):
        return "%s " %(self.proveedore)
    class Meta:
        db_table = "proveedores"