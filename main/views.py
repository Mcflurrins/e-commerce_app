from django.shortcuts import render, redirect  # Add import redirect at this line
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import datetime
import json
from django.http import JsonResponse

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = Product.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            description=data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@login_required(login_url='/login')
def show_main(request):
    context = {
        'app_name' : 'Upcycle Shop',
        'name': request.user.username,
        'class': 'KKI',
        'last_login': request.COOKIES.get('last_login', 'Not set'),
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductForm(request.POST or None) 

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.filter(user=request.user) #get the products where the user attribute is equal to the current user
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml") #convert data to xml

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id) #get the products by their id
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id): 
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request): 
    form = UserCreationForm() #define type of form 

    if request.method == "POST": 
        form = UserCreationForm(request.POST) #request.POST contains the form data
        if form.is_valid():
            form.save() #save into database if the form is valid
            messages.success(request, 'Your account has been successfully created!')  #this message will be passed into login.html
            return redirect('main:login') #redirect to the login function
    context = {'form':form} #else reload the page with an empty form 
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST) #take the form data

      if form.is_valid():
        user = form.get_user() #get the user in the form data 
        login(request, user) #login the user 
        response = HttpResponseRedirect(reverse("main:show_main")) #direct the user to the main page
        response.set_cookie('last_login', str(datetime.datetime.now())) #set a last login cookie
        return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context) #else reload the page with an empty form 

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = Product.objects.get(pk = id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    # Return to home page
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    description = strip_tags(request.POST.get("description")) # strip HTML tags!
    price = request.POST.get("price")
    user = request.user

    if name and price and description:
        new_product = Product(
            name= name, 
            description=description,
            price=price,
            user=user
        )
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    else:
        return HttpResponse('Missing fields', status=400)
    
