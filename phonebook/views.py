from django.shortcuts import render,redirect,get_object_or_404
from phonebook.forms import ContactsForm
from phonebook.models import Contacts

# Create your views here.
# index View
def index(request):
    return render(request,'index.html')

# Create View
def create(request):
    if request.method =='POST':
        form =ContactsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form =ContactsForm()
    return render(request,'create.html',{'form':form})

# Show
def show(request):
    contactInfo= Contacts.objects.all()
    return render(request,"show.html",{'contactInfo':contactInfo})

# Edit 
def edit(request,id):
    contactInfo= Contacts.objects.get(id=id)
    return render(request,'edit.html',{'contactInfo':contactInfo})


def update(request,id):
    contactInfo=Contacts.objects.get(id=id)
    form = ContactsForm(request.POST,instance=contactInfo)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'contactInfo':contactInfo})

def delete(request,id):
    contact=Contacts.objects.get(id=id)
    contact.delete()
    return redirect('/show')
def deleteAll(request):
    contact=Contacts.objects.all()
    contact.delete()
    return redirect('/show')

