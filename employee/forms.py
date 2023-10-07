from django import forms  
from employee.models import Employee, Proveedores
from django.forms import fields

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  

class ProveedoresForm(forms.ModelForm):
    class Meta: 
        model = Proveedores
        fields = "__all__"