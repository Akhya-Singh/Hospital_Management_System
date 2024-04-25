from django.shortcuts import render,redirect
from .models import Patient

# Create your views here.
def home(request):
    regs=Patient.objects.all()
    return render(request,"regs/home.html", {'regs':regs}) 

def regs_add(request):
    if request.method=='POST':
        print("Added")
        regs_pid=request.POST.get("reg_pid")
        regs_name=request.POST.get("reg_name")
        regs_phone=request.POST.get("reg_phone")
        regs_condition=request.POST.get("reg_condition")
        regs_prescription=request.POST.get("reg_prescription")

        p=Patient()
        p.pid=regs_pid
        p.name=regs_name
        p.phone=regs_phone
        p.condition=regs_condition
        p.prescription=regs_prescription

        p.save()
        return redirect("/regs/home")


    return render(request,"regs/add_regs.html",{})    

def delete_regs(request,pid):
    p=Patient.objects.get(pk=pid)
    p.delete()

    return redirect("/regs/home")

def update_regs(request,pid):
    regs=Patient.objects.get(pk=pid)

    return render(request,"regs/update_regs.html",{'regs': regs})

def do_update_regs(request,pid):
    regs_pid=request.POST.get("reg_pid")
    regs_name=request.POST.get("reg_name")
    regs_phone=request.POST.get("reg_phone")
    regs_condition=request.POST.get("reg_condition")
    regs_prescription=request.POST.get("reg_prescription")

    r=Patient.objects.get(pk=pid)

    r.pid=regs_pid
    r.name=regs_name
    r.phone=regs_phone
    r.condition=regs_condition
    r.prescription=regs_prescription

    r.save()
    return redirect("/regs/home")


        
     
