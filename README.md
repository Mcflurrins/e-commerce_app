# PWS Deployment Site:
http://flori-andrea-ecommerceapp.pbp.cs.ui.ac.id/ 

# WEEK 2
### Explain why we need data delivery in implementing a platform.
JSON is better than XML because it’s easier to understand (readable) for me. JSON is popular because it uses less syntax, which data more compact and faster to parse. Unlike XML’s heavy use of tags, JSON is clean and straightforward, focusing on key-value pairs. This simplicity leads to better performance, especially in web APIs, where speed and efficiency are crucial. JSON’s object model aligns well with most programming languages, making it a natural choice for developers to handle structured data.

### Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.
The is_valid() method runs a validation routine for all of the fields in a Django form, and when this method finds valid data in all the fields, then it will return True and place the form’s data in its cleaned_data attribute. This is essential in forms because it ensures that the user input has the correct data type and the data is clean.

### Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?
A unique CSRF token is generated by Django whenever an authenticated user surfs on the website, and this can be used in forms or requests made by the user, then checked by the server to ensure an authenticated user made the request, not a malicious source. CSRF protection mainly focuses on protecting against malicious attacks that makes changes to data, and if we don't make use of the CSRF token properly, it might lead our website to become more susceptible to Cross Site Request Forgery, where an attacker sends an authenticated user a link through sms or email. This link has a request that the attacker wants to have performed. By the time the user clicks on the link, the request is completed because they are already authenticated on the website. This can be used for transfer of funds, or malicious altering of data in favor of the attacker.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
#### 1. Set up the base template
To implement the skeleton of a view, I made a direcctory templates in the root folder and created base.html as a base template to be used as a generic view for other web pages in this project. Also, I adjusted settings.py to recognize this as a template file.
#### 2. Changing the primary key
I then modified models.py so that it would have a unique uuid for every form entry, ensuring security in this Django application.
#### 3. Making forms
I made a file, forms.py, to create a structure of the form I'm going to use.
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]
```
Then, I made a new function in views.py so that users can make a new form entry on the website. 
```
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
urls.py should then also be modified to accommodate for the function we just created. I also made create_product_entry.html to display the form fields in the site.

#### 4. Adding views
For this step, I first add the HttpResponse and Serializer imports into views.py, which helps me make the 4 functions I need to add the views XML, JSON, XML_by_id, JSON_by_id, like below:
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
#### Creating URL routings for the views

### Access the four URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.
![image](https://github.com/user-attachments/assets/1943b6b4-6fb4-4ebd-a5c8-80ee2805bc12)
![image](https://github.com/user-attachments/assets/6698afa2-43be-485a-a8bc-d25702effece)
![image](https://github.com/user-attachments/assets/341de937-910f-453b-901b-be4b6efb0374)
![image](https://github.com/user-attachments/assets/63e6e4fb-bc8b-4393-abe2-dc0c5753d852)

# WEEK 1
### Explain how you implemented the checklist above step-by-step (not just following the tutorial).

First, I made a repository on Github for this assignment. Then, I made a local directory on my computer for this project and connected it to the new github repo I just made through the 'git init' 
and 'git remote add url..' commands. I made the readme file along with it and a new directory for my django project within it. I followed this by setting up a virtual enviornment and setting up dependencies with requirements.txt, then I used the command 'django-admin startproject mental_health_tracker .' to create a new django project I can use as a base for this assignment. 
I then made a 'main' directory in here with the command 'python manage.py startapp main' and put a main.html file in it within a new templates directory. This will decide the appearance of the Django webpage. I also added a model called 'Product' to my Django project, and added the mandatory attributes as mentioned in the assignment. After that, I created and applied my migrations to the local database. The next step is integrating the MVT components by configuring the views.py file and making a 'show_main' function which will tie in with the html we made earlier. I also made changes to main.html to display data from the model and also to experiment and put in some bits of CSS into it to make it look nicer :). After, I started configuring the URL routings by adding 'path('', include('main.urls'))' to urlpatterns in urls.py, so that the webpage will be directed to the main view.

### Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.
![WhatsApp Image 2024-09-10 at 20 56 07_dd3c227c](https://github.com/user-attachments/assets/f9a746b9-978e-4b30-8d84-bca6e5097cf0)
#### Relationship between urls.py, views.py, models.py, and the html file:
urls.py redirects HTTP requests to the appropriate view based on the URL from the client. It basically determines which function in views.py should handle the request. views.py will then return HTTP responses and it also accesses any data that might be needed in the request using models.py. The formatting of this HTTP response is then left to the template, or the html file, which decides the appearance of the webpage. 

### Explain the use of git in software development!

Git allows for efficient and convenient source code management for even very large projects. It also allows for multiple programmers to work on the same project together more easily. With git, 
programmers can get an entire copy of the code in their local systems and also neatly update the code from their computers. It's easier to track any changes that are made to the code by others, as the history 
can be easily viewed from Github. Through the help of Git and the Github platform, programmers can now also gain inspiration from others' source codes and coding projects. Apart from that, non-linear project development
is also allowed in Git with its multiple branches. 

### In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?

First of all, Django is written in Python, which is a simple programming language that is also often used by people who have just gotten into programming. 
Likewise, it has HTML, CSS and Javascript support for people who come from a we. development background. Besides that, Django is well-established and there's a lot of forums on the 
internet where you can get help if you're ever stuck programming a Django project. Django also shines in its popularity and usefulness because is used by internet giants, like Instagram, Spotify etc.

### Why is the Django model called an ORM?

The Django model is called an ORM, which stands for Object-Relational Mapper. ORM is a technique where you can manipulate data from a database using object-oriented concepts. With an ORM library, 
you can manipulate the data in your original language without SQL. Likewise, in Django, you can edit the data in the model with Python (no SQL!). From what I've learned in tutorial 1, the Django model
uses classes to store data, which is why this ties back in with the object-oriented paradigm.

