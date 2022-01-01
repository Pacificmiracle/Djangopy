
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Home.models import Entry
# Create your views here.
def home (request):
    return render(request,"home.html")

def show (request):
    data = Entry.objects.all()
    return render(request,"show.html",{'data': data })

def send (request):
    if request.method == 'POST':
        ID = request.POST['id']
        name = request.POST['Name']
        number =request.POST['Number']
        Entry(ID = ID, Name = name, Number = number).save()
        msg = "Data Saved Successfully" 
        return render(request,"home.html",{'msg':msg})
    else:
        return HttpResponse("<h1> NOT Found 404</h1>")
    
def delete(request):
    ID = request.GET['id']
    Entry.objects.filter(ID = ID).delete()
    return HttpResponseRedirect("show")

def edit(request):
    ID = request.GET['id']
    name = number = "NOT_AVAILABLE"
    for data in Entry.objects.filter( ID = ID ):
        name = data.name
        number = data.number  
    return render(request,"edit.html",{'ID':ID,'name':name, 'number':number})

def RecordEdited(request):
    if request.method == 'POST':
        ID = request.POST['id']
        name = request.POST['name']
        number = request.POST['number'] 
        Entry.object.filter(ID = ID).update(name = name, number = number)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1> 404 NOT Found </h1>")
    
        


    