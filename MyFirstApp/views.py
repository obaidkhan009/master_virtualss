from django.shortcuts import render, HttpResponse , redirect
from .forms import ClientForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required

from .models import Client

# Create your views here.
def home(request):
    context={
        "var1":"55",
        "var2":"77"
    }
    #return render(request,'home.html',context)
    #this is for form 
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('home')  # Redirect to the home page after successful submission
    else:
        form = ClientForm()
    return render(request, 'home.html', {'form': form})

def about(request):
   # return HttpResponse("this is about page")
    return render(request, 'about.html')

def contact(request):
    #return HttpResponse("this is contact page")
    return render(request, 'contact.html')

def services(request):
    #return HttpResponse("this is services page")
    return render(request, 'services.html') 

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('client_forms')  # Redirect to the client_forms view
        else:
            # Invalid credentials, show error message or handle as needed
            pass
    return render(request, 'login.html')

@login_required  # Ensures only logged-in admins can access this view
def client_forms(request):
    clients = Client.objects.all()
    return render(request, 'client_forms.html', {'clients': clients})

def create_admin(request):
    return render(request, 'create_admin.html')

def login_view(request):
    return render(request, 'login.html')



    












