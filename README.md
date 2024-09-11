Explain how you implemented the checklist above step-by-step (not just following the tutorial).

First, I made a repository on Github for this assignment. Then, I made a local directory on my computer for this project and connected it to the new github repo I just made through the 'git init' 
and 'git remote add url..' commands. I made the readme file along with it and a new directory for my django project within it. I followed this by setting up a virtual enviornment and setting up dependencies with requirements.txt, then I used the command 'django-admin startproject mental_health_tracker .' to create a new django project I can use as a base for this assignment. 
I then made a 'main' directory in here with the command 'python manage.py startapp main' and put a main.html file in it within a new templates directory. This will decide the appearance of the Django webpage. I also added a model called 'Product' to my Django project, and added the mandatory attributes as mentioned in the assignment. After that, I created and applied my migrations to the local database. The next step is integrating the MVT components by configuring the views.py file and making a 'show_main' function which will tie in with the html we made earlier. I also made changes to main.html to display data from the model and also to experiment and put in some bits of CSS into it to make it look nicer :). After, I started configuring the URL routings by adding 'path('', include('main.urls'))' to urlpatterns in urls.py, so that the webpage will be directed to the main view.

Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.
![WhatsApp Image 2024-09-10 at 20 56 07_dd3c227c](https://github.com/user-attachments/assets/f9a746b9-978e-4b30-8d84-bca6e5097cf0)
Relationship between urls.py, views.py, models.py, and the html file:
urls.py redirects HTTP requests to the appropriate view based on the URL from the client. It basically determines which function in views.py should handle the request. views.py will then return HTTP responses and it also accesses any data that might be needed in the request using models.py. The formatting of this HTTP response is then left to the template, or the html file, which decides the appearance of the webpage. 

Explain the use of git in software development!

Git allows for efficient and convenient source code management for even very large projects. It also allows for multiple programmers to work on the same project together more easily. With git, 
programmers can get an entire copy of the code in their local systems and also neatly update the code from their computers. It's easier to track any changes that are made to the code by others, as the history 
can be easily viewed from Github. Through the help of Git and the Github platform, programmers can now also gain inspiration from others' source codes and coding projects. Apart from that, non-linear project development
is also allowed in Git with its multiple branches. 

In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?

First of all, Django is written in Python, which is a simple programming language that is also often used by people who have just gotten into programming. 
Likewise, it has HTML, CSS and Javascript support for people who come from a we. development background. Besides that, Django is well-established and there's a lot of forums on the 
internet where you can get help if you're ever stuck programming a Django project. Django also shines in its popularity and usefulness because is used by internet giants, like Instagram, Spotify etc.

Why is the Django model called an ORM?

The Django model is called an ORM, which stands for Object-Relational Mapper. ORM is a technique where you can manipulate data from a database using object-oriented concepts. With an ORM library, 
you can manipulate the data in your original language without SQL. Likewise, in Django, you can edit the data in the model with Python (no SQL!). From what I've learned in tutorial 1, the Django model
uses classes to store data, which is why this ties back in with the object-oriented paradigm.

