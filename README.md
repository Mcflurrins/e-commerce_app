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

  In CSS, margin, border, and padding are used to control the space around and inside elements. Margin is the space outside the element, separating it from other elements. Padding is the space inside the element, between its content and its border. Border is the line that surrounds the padding and content. For example, to implement these in CSS, we could do something like this:

  ```
  element {
    margin: 10px;   /* space outside the element */
    border: 2px solid black;  /* border around the element */
    padding: 20px;  /* space inside, around the content */
  }
  ```

  ![image](https://github.com/user-attachments/assets/22118366-2e53-4444-a6c5-fb116017e032)

  The box model is a very helpful diagram that shows where the margin, border and padding are located.

  ### Explain the concepts of flex box and grid layout along with their uses!

  Flexbox and grid layout are used for creating responsive layouts. Flexbox is one-dimensional and arranges elements either in a row or column. It's good for aligning simple items within a container, such as navigation bars or horizontally centered content. Grid layout is two-dimensional and allows for more precise placement of items both in rows and columns, making it suitable for more complex layouts such as dashboards or image galleries. 
  
  ### Explain how you implemented the checklist above step-by-step (not just following the tutorial)!
  #### 1. Adding Tailwind CSS to the Project
  To integrate Tailwind CSS with the Django template, we can use the CDN (Content Delivery Network) by including the Tailwind CDN link in the `<head>` section of the `base.html` template.
  ```
  <head>
  {% block meta %}
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1">
  {% endblock meta %}
  <script src="https://cdn.tailwindcss.com">
  </script>
  </head>
  ```
  #### 2. Adding Edit Product and Delete Product features
   I add the following functions into views.py:
   ```
   def edit_product(request, id):
    product = Product.objects.get(pk = id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
   ```

   ```
   def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    # Return to home page
    return HttpResponseRedirect(reverse('main:show_main'))
     ```

  The edit_product function in Django allows users to modify an existing product's details. It first retrieves the product using its primary key (id) via Product.objects.get(pk=id). This product instance is then used to populate a form, ProductForm, which is initialized with either the submitted POST data or the current product details if no data has been submitted yet. The function checks if the form is valid upon a POST request. If the form is valid, it saves the changes to the database and redirects the user to the home page. If the form is not valid or when first loaded, it renders the edit_product.html template, providing the form for the user to edit.
  
  The delete_product function retrieves the product instance using Product.objects.get(pk=id) based on the provided ID and then calls the delete() method on that instance to remove it. After successfully deleting the product, the function redirects the user back to the home page using HttpResponseRedirect(reverse('main:show_main')). 

  #### 3. Adding a Navigation Bar 
  First, modify main.html to include the navigation bar.
  ```
  {% extends 'base.html' %}
  {% block content %}
  {% include 'navbar.html' %}
  ...
  {% endblock content%}
  ```
  Then, I make a file called navbar.html, which is styled as follows:
```
<nav class="bg-amber-400 shadow-lg fixed top-0 left-0 z-40 w-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <h1 class="text-2xl font-bold text-center text-green-800">Upcycle Shop</h1>
        </div>
        <div class="hidden md:flex items-center">
          {% if user.is_authenticated %}
            <span class="text-white mr-4">Welcome, {{ user.username }}</span>
            <a href="{% url 'main:logout' %}" class="text-center bg-green-800 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Logout
            </a>
          {% else %}
            <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Register
            </a>
          {% endif %}
        </div>
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button">
            <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
    <!-- Mobile menu -->
    <div class="mobile-menu hidden md:hidden  px-4 w-full md:max-w-full">
      <div class="pt-2 pb-3 space-y-1 mx-auto">
        {% if user.is_authenticated %}
          <span class="block text-white-300 px-3 py-2">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:logout' %}" class="block text-center bg-green-700 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
    </div>
    <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
    
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
  </nav>
  ```

  #### 4. Configure Static Files
  ```
  ...
  MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'whitenoise.middleware.WhiteNoiseMiddleware', # Add it directly under SecurityMiddleware
      ...
  ]
  ...
  ```

  ```
  ...
  STATIC_URL = '/static/'
  if DEBUG:
      STATICFILES_DIRS = [
          BASE_DIR / 'static' # refers to /static root project in development mode
      ]
  else:
      STATIC_ROOT = BASE_DIR / 'static' # refers to /static root project in production mode
  ...
  ```

#### 5. External css 
I modify the base html to be like so: 
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
  </head>
  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
Then, I add custom styling in global.css.
```
.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}
.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #174130;
    box-shadow: 0 0 0 3px #15584e;
}
@keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}
.animate-shine {
    background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
    background-size: 200% 100%;
    animation: shine 3s infinite;
}
```
After that, I style my login page like this:
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center w-screen bg-yellow-50 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8">
    <div>
      <h2 class="mt-6 text-center text-green-900 text-3xl font-extrabold text-gray-900">
        Login to your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST" action="">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        <div>
          <label for="username" class="sr-only">Username</label>
          <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-green-800 placeholder-amber-600 text-gray-900 rounded-t-md focus:outline-none focus:ring-amber-700 focus:border-amber-700 focus:z-10 sm:text-sm" placeholder="Username">
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-green-800 placeholder-amber-600 text-gray-900 rounded-b-md focus:outline-none focus:ring-amber-700 focus:border-amber-700 focus:z-10 sm:text-sm" placeholder="Password">
        </div>
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-800 hover:bg-green-950 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-700">
          Sign in
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      {% if message.tags == "success" %}
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% elif message.tags == "error" %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% else %}
            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-green-900 ">
        Don't have an account yet?
        <a href="{% url 'main:register' %}" class="font-medium text-amber-600 hover:text-amber-300">
          Register Now
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```
I also style the register page: 
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-yellow-50 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 form-style">
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-green-800">
        Create your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
              {{ field.label }}
            </label>
            <div class="relative">
              {{ field }}
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                {% if field.errors %}
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                {% endif %}
              </div>
            </div>
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-800 hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-800">
          Register
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-green-800 hover:text-green-800">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```
I style the main page too, which is connected to images in the static/image directory in the project root. This is how the sad face becomes shown when there are no entries in the website.

```

{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>{{ app_name }}</title>
{% endblock meta %}
{% block content %}
{% include 'navbar.html' %}
<div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-yellow-50 flex flex-col">
    <div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-8 bg-yellow-50 flex flex-row space-x-8 items-center">
        <!-- Profile Picture Column -->
        <div class="flex-shrink-0">
          <img src="{% static 'image/profile.png' %}" alt="Profile Picture" class="h-16 w-16 rounded-full object-cover">
        </div>
        
        <!-- Info Card Column -->
        <div class="bg-white p-4 rounded-lg shadow-md">
          <p class="text-lg font-semibold">{{ name }}</p>
          <p class="text-sm">{{ class }}</p>
          <h5 class="text-xs text-gray-500">Last login session: {{ last_login }}</h5>
        </div>
      </div>



<!-- main.html -->
{% if not product_entries %}
<div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
    <img src="{% static 'image/very-sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
    <p class="text-center text-gray-600 mt-4">There is no mood data in product database.</p>
</div>
  <p>There is no product data in Upcycle shop.</p>
{% else %}
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    {% for product_entry in product_entries %}
      {% include 'product_card.html' %}
    {% endfor %}
  </div>
{% endif %}
  
  <div class="fixed bottom-4 right-4 md:px-4 pb-4">
    <a href="{% url 'main:create_product_entry' %}">
        <button class="bg-green-800 text-white h-16 w-16 pb-2 rounded-full flex items-center justify-center shadow-lg hover:bg-green-900 focus:outline-none focus:ring-2 focus:ring-green-300">
            <span class="text-3xl font-bold">+</span>
        </button>
    </a>
</div>
  
{% endblock content %}
```
The home page includes a product card, which is put in another file so as not to clutter main.html.
```
<div class="relative break-inside-avoid">
  <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
  </div>
  <div class="relative top-5 bg-white shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col transform rotate-1 hover:rotate-0 transition-transform duration-300">
    <div class="bg-green-800 text-gray-800 p-4 rounded-t-lg ">
      <h3 class="font-bold text-xl text-white mb-2">{{product_entry.name}}</h3>
      <p class="text-white">${{product_entry.price}}</p>
    </div>
    <div class="p-4">
      <p class="font-semibold text-lg mb-2">Description</p> 
      <p class="text-gray-700 mb-2">
        <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#98a692_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{product_entry.description}}</span>
      </p>
      <div class="mt-4">
        <div class="relative pt-1">
          <div class="flex mb-2 items-center justify-between">
          </div>
          <div class="overflow-hidden h-2 mb-4 text-xs flex rounded">
            <div style="width:{% if product_entry.product_intensity > 10 %}100%{% else %}{{ product_entry.product_intensity }}0%{% endif %}" class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="absolute top-0 -right-4 flex space-x-1">
    <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
      </svg>
    </a>
    <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
    </a>
  </div>
</div>
```

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
