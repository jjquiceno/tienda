from django.shortcuts import render
from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm, ProveedoresForm 
from employee.models import Employee, Proveedores 
 
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  

def menu(request):  
    employees = Employee.objects.all()  
    return render(request,"menu.html",{'employees':employees}) 

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")

# --------------------------------------------------------------------------
def emp2(request):
    if request.method == "POST":  
        form = ProveedoresForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/shp')  
            except:  
                pass  
    else:  
        form = ProveedoresForm()  
    return render(request,'regpro.html',{'form':form})  

def shp(request):
    proveedor = Proveedores.objects.all()  
    return render(request,"shp.html",{'proveedoress':proveedor})  

def edit2(request, id):  
    proveedor = Proveedores.objects.get(id=id)  
    return render(request,'edit2.html', {'proveedores':proveedor})  

def update2(request, id):  
    proveedore = Proveedores.objects.get(id=id)  
    form = ProveedoresForm(request.POST, instance = proveedore)  
    if form.is_valid():  
        form.save()  
        return redirect("/shp")  
    return render(request, 'edit2.html', {'proveedores': proveedore})  

def destroy2(request, id):  
    proveedor = Proveedores.objects.get(id=id)  
    proveedor.delete()  
    return redirect("/shp")
