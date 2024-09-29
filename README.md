# PWS Deployment Site:
http://flori-andrea-ecommerceapp.pbp.cs.ui.ac.id/

<details>
  <summary>WEEK 4</summary>

  ### If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!
  Every CSS selector has a place in the specificity hierarchy, with the four categories ranked below:
  
  1. Inline styles - E.g. < h1 style="color: pink'; >
  2. IDs - E.g. #navbar
  3. Classes, pseudo-classes, attribute selectors - E.g. .test, :hover, [href]
  4. Elements and pseudo-elements - E.g. h1, ::before

  Different selectors have different specificity values, and these can be calculated. The selector with the highest specificity value wins over the others and takes effect.

  ### Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!
  Responsive design ensures a website or application provides an good viewing experience across various devices, like desktops, tablets, and smartphones. With the variety of screen sizes and resolutions, users expect ease of access and viewing regardless of the device they use. Applications like Google and Tokopedia have implemented responsive design nicely, allowing their interfaces to adapt smoothly to different devices. Older websites or applications that haven't updated, such as some legacy government sites, may not have implemented responsive design, resulting in poor usability on smaller screens. Here's a real life example of a website with no responsive design: https://dequeuniversity.com/library/responsive/1-non-responsive 
  
  ### Explain the differences between margin, border, and padding, and how to implement these three things!

  In CSS, margin, border, and padding are used to control the space around and inside elements. Margin is the space outside the element, separating it from other elements. Padding is the space inside the element, between its content and its border. Border is the line that surrounds the padding and content. For example, to implement these in CSS:

  ```
  element {
    margin: 10px;   /* space outside the element */
    border: 2px solid black;  /* border around the element */
    padding: 20px;  /* space inside, around the content */
  }
  ```
  ### Explain the concepts of flex box and grid layout along with their uses!
  ### Explain how you implemented the checklist above step-by-step (not just following the tutorial)!

</details>

<details>
  <summary>WEEK 3</summary>
  
  ### What is the difference between HttpResponseRedirect() and redirect()?
  HttpResponseRedirect() only accepts a url, however redirect() will return a HttpResponseRedirect() that accepts a model, view or url. redirect() is more convenient as it simplifies the redirection process, whereas HttpResponseRedirect() gives more control but requires manual URL handling.

  ### Explain how the MoodEntry model is linked with User!
  The MoodEntry model is connected to the User model in Django using a relationship so that each mood entry is related to a specific user. When a user submits a mood entry via the form, the logged-in user (request.user) is assigned to the user field of the MoodEntry before it is saved to the database. On the main page, only the mood entries belonging to the logged-in user are displayed by filtering the entries using MoodEntry.objects.filter(user=request.user). During migration, existing entries are assigned to a default user (the first user that we register).
  
  ### What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.
  Authentication is the process of verifying the identity of a user so that they are indeed who they claim to be while authorization is the process of determining what permissions a user has to do something. In my code, when a user logs in through the login_user function, the system verifies the submitted credentials using Django's AuthenticationForm module. If it's correct, the get_user() method retrieves the user object, and the login function logs the user into the current session. After a successful login, the user is directed to main.html, with their session tracked through cookies. Django supports authentication through django.contrib.auth, and in terms of authorization it also has decorators like @login_required to restrict certain views only to authenticated users.

  ### How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.
  Django remembers logged-in users through sessions and cookies, where a session ID is stored in a cookie on the user's browser after login. Each time the user makes a request, the session ID cookie is sent back to the server, allowing Django to retrieve the associated session data and recognize the user. Aside that, cookies can store preferences, track user activity, and remember shopping carts. When cookie data falls into the wrong hands, it can be used for malicious purposes. As an example, an attacker might use cookies to make unauthorized requests on behalf of a user without their consent (known as Cross Site Request Forgery).

  ### Explain how did you implement the checklist step-by-step (apart from following the tutorial).
#### 1. Implement the register, login and logout functions.
First, I import the Add UserCreationForm, logout, login_required dan messages modules at the top of my main/views.py file. The UserCreationForm module simplifies creating user registration forms in a web app. Then I add the following functions to this file.
```
def register(request):
form = UserCreationForm()
if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your account has been successfully created!')
        return redirect('main:login')
context = {'form':form}
return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')
```
Then I make a new file called register.html with the following content, and also connect its URL path to urls.py:
```
{% extends 'base.html' %} {% block meta %}
<title>Register</title>
{% endblock meta %} {% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Register" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
I also made a file called login.html with content like below, and also connect it to urls.py.
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
Apart from that, I make a logout button in main.html which is connected through urls.py to the logout function in views.py.
To restrict access to the main page, I add the code snippet @login_required(login_url='/login') above the show_main function so that the main page can only be accessed by authenticated users.

#### 2. Use the Data from the Cookies
For this, I add the imports for HttpResponseRedirect, reverse, and datetime at the top of the views.py file. Then I modify the login and logout functions to make use of the cookies such that they look like this: 
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
I also change the show_main function to display the name of the logged-in user.
```
context = {
    'name': 'Pak Bepe',
    'class': 'PBP D',
    'npm': '2306123456',
    'mood_entries': mood_entries,
    'last_login': request.COOKIES['last_login'],
}
```
Then, I modify the main.html file to display the last login session like so: 
```
...
<h5>Last login session: {{ last_login }}</h5>
...
```

#### 3. Connect the models Product and User and Display the Username on the Main Page
In models.py, I import User from django.contrib.auth.models, then I add this code snippet to it to connect Product to User with a relationship:
```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
...
```
Then, I modify the create_product_entry function in models.py. The `commit=False` parameter stops Django from saving the form's created object to the database right away so that we can modify the object before saving. Then, we assign the `user` field with the `User` object from `request.user`, linking the object to the currently logged-in user.
```
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
Also, modify the show_main function so that it can display the logged in user's username on the main page of the app.
```
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)
    context = {
        'app_name' : 'Upcycle Shop',
        'name': request.user.username,
    ...
    }
```

#### 4. Make two user accounts with three dummy data each, using the model made in the application beforehand so that each data can be accessed by each account locally.
For this step, I accessed the app on my localhost by running python manage.py runserver through http://localhost:8000/. Then, I registered two new users, dummyA and dummyB, then i added three dummy data for each user by creating new product entries. 
  
</details>
<details>
<summary>WEEK 2</summary>
  
#### Explain why we need data delivery in implementing a platform.
Data delivery is important for platform implementation because it ensures efficient communication between the platform's components and users. This allows for the website to make real-time updates and interactions. For large-scale platforms, reliable data delivery is needed to keep performance up under increased demand. It also ensures the secure transmission of data, protecting the platform from breaches, attackers and unauthorized access.

#### In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
JSON is better than XML because it’s easier to understand (readable) for me. JSON is popular because it uses less syntax, which data more compact and faster to parse. Unlike XML’s heavy use of tags, JSON is clean and straightforward, focusing on key-value pairs. This simplicity leads to better performance, especially in web APIs, where speed and efficiency are crucial. JSON’s object model aligns well with most programming languages, making it a natural choice for developers to handle structured data.

### Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.
The is_valid() method runs a validation routine for all of the fields in a Django form, and when this method finds valid data in all the fields, then it will return True and place the form’s data in its cleaned_data attribute. This is essential in forms because it ensures that the user input has the correct data type and the data is clean.

### Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?
A unique CSRF token is generated by Django whenever an authenticated user surfs on the website, and this can be used in forms or requests made by the user, then checked by the server to ensure an authenticated user made the request, not a malicious source. CSRF protection mainly focuses on protecting against malicious attacks that makes changes to data, and if we don't make use of the CSRF token properly, it might lead our website to become more susceptible to Cross Site Request Forgery, where an attacker sends an authenticated user a link through sms or email. This link has a request that the attacker wants to have performed. By the time the user clicks on the link, the request is completed because they are already authenticated on the website. This can be used for transfer of funds, or malicious altering of data in favor of the attacker.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
#### 1. Set up the base template
To implement the skeleton of a view, I made a directory 'templates' in the root folder and created base.html as a base template to be used as a generic view for other web pages in this project. Also, I adjusted settings.py to recognize this as a template file.
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

#### 2. Changing the primary key
I then modified models.py so that it would have a unique uuid for every form entry, ensuring security in this Django application.
```
from django.db import models
import uuid  # add this line at the very top
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # add this line
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
```
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
#### 5. Creating URL routings for the views
Before I start adding more paths into urls.py, I first import the new functions I just made in views.py into this urls.py.
```
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
```
Only then do I add the paths into urlpatterns, illustrated as below: 
```
urlpatterns = [ ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ...]
```
This step concludes it for the site! The results can be seen in the next part, where I access the 4 views I made through Postman.

### Access the four URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.
![image](https://github.com/user-attachments/assets/1943b6b4-6fb4-4ebd-a5c8-80ee2805bc12)
![image](https://github.com/user-attachments/assets/6698afa2-43be-485a-a8bc-d25702effece)
![image](https://github.com/user-attachments/assets/341de937-910f-453b-901b-be4b6efb0374)
![image](https://github.com/user-attachments/assets/63e6e4fb-bc8b-4393-abe2-dc0c5753d852)
</details>
<details>
<summary> WEEK 1
</summary>
  
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
</details>
