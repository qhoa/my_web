Django Search Tutorial
 Last updated Dec 8, 2022
Note: I gave a version of this tutorial at DjangoCon US 2019. You can see the video here:


I also have a Django Chat podcast episode all about search in discussion with Django Fellow Carlton Gibson.

To start let's create a new Django project (see here if you need help with this). I've done so in a directory called search. On your command line, enter the following commands to install the latest version of Django, create a project called citysearch_project, set up the initial database via migrate, and then start the local web server with runserver.

> cd onedrive\desktop\code
> mkdir search
> cd search
> python -m venv .venv
> .venv\Scripts\Activate.ps1
(.venv) > python -m pip install django~=4.0.0
(.venv) > django-admin startproject citysearch_project .
(.venv) > python manage.py migrate
(.venv) > python manage.py runserver

# macOS
% cd ~/desktop/code
% mkdir search
% cd search
% python3 -m venv .venv
% source .venv/bin/activate
(.venv) % python3 -m pip install django~=4.0.0
(.venv) % django-admin startproject citysearch_project .
(.venv) > python manage.py migrate
(.venv) > python manage.py runserver
If you navigate to http://127.0.0.1:8000/ you'll see the Django welcome page which confirms everything is configured properly.

Django welcome page

Cities app
Now we'll create a single app called cities to store a list of city names. We're keeping things intentionally basic. Stop the local server with Control+c and use the startapp command to create this new app.

(.venv) $ python manage.py startapp cities
Then update INSTALLED_APPS within our settings.py file to notify Django about the app.

# citysearch_project/settings.py
INSTALLED_APPS = [
    ...
    "cities",  # new
]
Now for the models. We'll call our single model City and it will have just two fields: name and state. Since the Django admin will be default pluralize the app name to Citys we'll also set verbose_name_plural. And finally set __str__ to display the name of the city.

# cities/models.py
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name
Ok, all set. We can create a migrations file for this change, then add it to our database via migrate.

(.venv) $ python manage.py makemigrations cities
(.venv) $ python manage.py migrate
There are multiple ways to populate a database but the simplest, in my opinion, is via the admin. Create a superuser account so we can log in to the admin.

(.venv) $ python manage.py createsuperuser
Now we need to update cities/admin.py to display our app within the admin.

# cities/admin.py
from django.contrib import admin

from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state",)

admin.site.register(City, CityAdmin)
Start up the server again with python manage.py runserver and navigate to the admin at http://127.0.0.1:8000/admin and log in with your superuser account.

Admin Homepage

Click on the cities section and add several entries. You can see my four examples here.

Admin Cities

Homepage and Search Results Page
We have a populated database but there are still a few steps before it can be displayed on our Django website. Ultimately we only need a homepage and search results page. Each page requires a dedicated view, url, and template. The order in which we create these doesn't really matter; all must be present for the site to work as intended.

Generally I prefer to start with the URLs, add the views, and finally the templates so that's what we'll do here.

First, we need to add a URL path for our cities app which can be done by importing include and setting a path for it.

# citysearch_project/urls.py
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cities.urls")), # new
]
Second, we need a urls.py file within the cities app however Django doesn't create one for us with the startapp command. Create cities/urls.py with your text editor and within this file we'll import yet-to-be-created views for each--HomePageView and SearchResultsView--and set a path for each. Note as well that we set an optional URL name for each.

Here's what it looks like:

# cities/urls.py
from django.urls import path

from .views import HomePageView, SearchResultsView

urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", HomePageView.as_view(), name="home"),
]
Third, we need to configure our two views. The homepage will just be a template with, eventually, a search box. Django's TemplateView works nicely for that. The search results page will list the results we want which is a good fit for ListView.

# cities/views.py
from django.views.generic import TemplateView, ListView

from .models import City


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'
Fourth and finally, we need our templates. We could add the templates within our cities app but I find that creating a project-level templates folder instead is a simpler approach.

(.venv) $ mkdir templates
Note that we also need to update our settings.py file to tell Django to look for this project-level templates folder. This can be found in the TEMPLATES section.

# citysearch_project/settings.py
TEMPLATES = [
    {
        ...
        "DIRS": [BASE_DIR / "templates"],  # new
        ...
    }
]
Then with your text editor create two new templates files: templates/home.html and templates/search_results.html. (The homepage will just be a title at this point.

<!-- templates/home.html -->
<h1>HomePage</h1>
Start up the web server again with python manage.py runserver and we can see the homepage now at http://127.0.0.1:8000/.

Homepage

Now for the search results page which will loop over object_list, the default name for the context object ListView returns. Then we'll output both the name and state for each entry.

<!-- templates/search_results.html -->
<h1>Search Results</h1>

<ul>
  {% for city in object_list %}
    <li>
      {{ city.name }}, {{ city.state }}
    </li>
  {% endfor %}
</ul>
And...we're done. Our search results page is available at http://127.0.0.1:8000/search/.

Search Results Page

Forms and Querysets
Ultimately a basic search implementation comes down to a form that will pass along a user query--the actual search itself--and then a queryset that will filter results based on that query.

We could start with either one at this point but'll we configure the filtering first and then the form.

Basic Filtering
In Django a QuerySet is used to filter the results from a database model. Currently our City model is outputting all its contents. Eventually we want to limit the search results page to filter the results outputted based upon a search query.

There are multiple ways to customize a queryset and in fact it's possible to do filtering via a manager on the model itself but...to keep things simple, we can add a filter with just one line. So let's do that!

Here it is, we're updating the queryset method of ListView and adding a hardcoded filter so that only a city with the name of "Boston" is returned. Eventually we will replace this with a variable representing the user search query!

# cities/views.py
class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'
    queryset = City.objects.filter(name__icontains='Boston') # new
Refresh the search results page and you'll see only "Boston" is now visible.

Boston

It's also possible to customize the queryset by overriding the get_queryset() method to change the list of cities returned. There's no real advantage to do so in our current case, but I find this approach to be more flexible than just setting queryset attributes.

# cities/views.py
...
class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'

    def get_queryset(self): # new
        return City.objects.filter(name__icontains='Boston')
Most of the time the built-in QuerySet methods of filter(), all(), get(), or exclude() will be enough. However there is also a very robust and detailed QuerySet API available as well.

Q Objects
Using filter() is powerful and it's even possible to chain filters together. However often you'll want more complex lookups such as using "OR" which is when it's time to turn to Q objects.

Here's an example where we set the filter to look for a result that matches a city name of "Boston" or a state name that contains with "NY". It's as simple as importing Q at the top of the file and then subtly tweaking our existing query.

# cities/views.py
from django.db.models import Q # new
...

class SearchResultsView(ListView):
    model = City
    template_name = "search_results.html"

    def get_queryset(self): # new
        return City.objects.filter(
            Q(name__icontains="Boston") | Q(state__icontains="NY")
        )
Refresh your search results page and we can see the result.

Boston and New York

Now let's turn to our search form to replace the current hardcoded values with search query variables.

Forms
Fundamentally a web form is simple: it takes user input and sends it to a URL via either a GET or POST method. However in practice this fundamental behavior of the web can be monstrously complex.

The first issue is sending the form data: where does the data actually go and how do we handle it once there? Not to mention there are numerous security concerns whenever we allow users to submit data to a website.

There are only two options for "how" a form is sent: either via GET or POST HTTP methods.

A POST bundles up form data, encodes it for transmission, sends it to the server, and then receives a response. Any request that changes the state of the database--creates, edits, or deletes data--should use a POST.

A GET bundles form data into a string that is added to the destination URL. GET should only be used for requests that do not affect the state of the application, such as a search where nothing within the database is changing, we're just doing a filtered list view basically.

If you look at the URL after visiting Google.com you'll see your search query in the actual search results page URL itself.

For more information, Mozilla has detailed guides on both sending form data and form data validation that are worth reviewing if you're not already familiar with form basics.

Search Form
But for our purposes, we can add a basic search form to our existing homepage right now. Here's what it looks like. We'll review each part below.

<!-- templates/home.html -->
<h1>HomePage</h1>

<form action="{% url 'search_results' %}" method="get">
  <input name="q" type="text" placeholder="Search...">
</form>
For the form the action specifies where to redirect the user after submission of the form. We're using the URL name for our search results page here. Then we specify the use of get as our method.

Within our single input--it's possible to have multiple inputs or to add a button here if desired--we give it a name q which we can refer to later. Specify the type which is text. And then add a placeholder value to prompt the user.

That's really it! On the homepage now try inputting a search, for example for "san diego".

San Diego

Upon hitting Return you are redirected to the search results page. Note in particular the URL contains our search query http://127.0.0.1:8000/search/?q=san+diego.

San Diego Search Result

However the results haven't changed! And that's because our SearchResultsView still has the hardcoded values from before. The last step is to take the user's search query, represented by q in the URL, and pass it in.

# cities/views.py
...
class SearchResultsView(ListView):
    model = City
    template_name = "search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list


##############################################

How to Build a Basic Search for a Django Site?
2 years agoby Fahmida Yesmin
A particular content of any site is normally retrieved by the users through Google search. However, if this search option is implemented on the website, then the users can easily find their desired content within the site without using Google search. . Another benefit of adding a search option within a website is that the developer can manage the searching output properly. That means he can control which content of the site will appear or not. This tutorial will show the process of implementing the basic search in the Django site.

Prerequisites:

Before practicing the script of this tutorial, you have to complete the following tasks:

Install the Django version 3+ on Ubuntu 20+ (preferably)
Create a Django project
Run the Django server to check the server is working properly or not.
Setup a Django App:

Run the following command to create a Django app named searchapp.

MY LATEST VIDEOS


$ python3 manage.py startapp searchapp
Run the following command to create the user for accessing the Django database. If you have created the user before then you don’t need to run the command.

$ python3 manage.py createsuperuser
Add the app name in the INSTALLED_APP part of the settings.py file.

INSTALLED_APPS = [

    …..

    'searchapp'

]
Create a folder named templates inside the searchapp folder and set the template’s location of the app in the TEMPLATES part of the settings.py file.


TEMPLATES = [

    {

….

                'DIRS': ['/home/fahmida/django_pro/searchapp/templates'],

                   ….

      },

]
Create Models:

Modify the models.py file with the following script. Here, two classes have been defined to create two relational tables named booktypes and books. The type field of the books table is a foreign key that will appear from booktypes table.


models.py

# Import necessary modules
from django.db import models
from django.urls import  reverse

# Create model gor booktype
class Booktype(models.Model):
    btype = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering=('btype',)

# Create model gor book
class Book(models.Model):
    book_name = models.CharField(max_length=150)
    author_name = models.CharField(max_length=150)
    type = models.ForeignKey(Booktype, on_delete=models.CASCADE)
    price = models.FloatField()
    publication = models.CharField(max_length=100)

    class Meta:
        ordering=('book_name',)

    def __str__(self):
        return self.book_name

    def get_url(self):
       return reverse('book_detail', args=[self.id])
Create Templates for Searching:

Three HTML files are required for you to create the search feature shown in this tutorial. These are book_list.html, book_detail.html, and search.html. The book_list.html will display all records from the books table. The book_detail.html will display the details of a particular book. The search.html will display the search result after submitting the search form.


book_list.html

<html>
<head>
    <title>Book List</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
</head>

<body>
<div class="container">
<div>
    <br/>
    <form action="{% url 'search' %}" class="form-inline" method="get">
       <div class="form-group mb-8">
            <h1>{% if type %}{{ type.name }}{% else %} List of Books {% endif %}</h1>
       </div>
       <div class="form-group mx-sm-3 mb-2">
        <label for="" class="sr-only">search</label>
        <input name="search" type="" class="form-control" id="" placeholder="Keyword">
        </div>
        <button type="submit" class="btn btn-success btn-lg mb-2">Search</button>
   </form>
        <br/>
    {% for x in book %}
    <h3> <a href="{{ x.get_url }}">{{x.book_name}}</a></h3>
    <p class="lead">by {{x.author_name}}</p>
      <p class="lead">${{x.price}}</p>
     <hr>
    {% endfor %}
</div>
</div>
</body>
</html>
book_detail.html

<html>
  <head>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <title>{{book.book_name}}</title>
</head>
<body>
<div class="container">
    <br/><br/>
    <h2 class="text-center"> {{book.book_name}}</h2>
     <hr>
     <p class="lead">Author: {{book.author_name}} </p>
     <p class="lead">Type: {{type}} </p>
     <p class="lead">Publication: {{book.publication}} </p>
     <p class="lead">Price: ${{book.price}} </p>
     <form action="{% url 'book_list' %}" class="form-inline" method="get">
     <button type="submit" class="btn btn-primary btn-lg mb-2">Back</button>
     </form>
  </div>
  </body>
</html>
search.html

<html>
<head>
   <title>Search Result</title>
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
</head>
<body>
<br/></br/>
<div class="container">
   <div class="col-md-8 offset-md-2">
{% if query %}
           <h2>
           {% with results.count as total_results %}
           Found {{ total_results }} result{{ total_results|pluralize }}
           {% endwith %}
           </h2>
   {% for c in results %}
  <a href="{{c.get_url}}"><h3>{{c.book_name}}</h3></a>
  <h3>{{c.author_name}}</h3>

   {% empty %}
   <h3>No results found.</h3>
   {% endfor %}
  {% endif %}
        <form action="{% url 'book_list' %}" class="form-inline" method="get">
        <button type="submit" class="btn btn-primary btn-lg mb-2">Back</button>
        </form>
    </div>
</div>
</body>

<html>
Create View Functions:

Modify the views.py file with the following script. Three functions have been defined in the script. The book_list() function will display the book_list.html file. The book_detail() function will display the book_detail.html. The search() function will search the records based on the data submitted by the search form and display the result into the search.html.


views.py

# Import necessary modules
from django.shortcuts import render,get_object_or_404
from .models import  Book, Booktype
from django.db.models import Q

# Define function to display all books
def book_list(request):
    book = Book.objects.all()
    return render(request, 'book_list.html', {'book': book })

# Define function to display the particular book
def book_detail(request,id):
    book = get_object_or_404(Book, id=id)
    types = Booktype.objects.all()
    t = types.get(id=book.type.id)
    return render(request, 'book_detail.html', {'book': book, 'type': t.btype})

# Define function to search book
def search(request):
    results = []

    if request.method == "GET":
        query = request.GET.get('search')

        if query == '':
            query = 'None'

        results = Book.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query) | Q(price__icontains=query) )

    return render(request, 'search.html', {'query': query, 'results': results})
Set Paths to Call View Functions:

Modify the urls.py file of the Django project with the following script. Four paths have been defined in the script. ‘admin/’ path is used to open the Django Administrative Dashboard. The empty path(‘’) is used to call the book_list() function. ‘<int:id>/’ path is used to call the book_detail() function. ‘search/’ path is used to call the search() function.


urls.py

# Import admin module
from django.contrib import admin

# Import path module
from django.urls import path

# Import view
from searchapp import views

# Define paths
urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.book_list, name='book_list'),
     path('/', views.book_detail, name='book_detail'),
     path('search/', views.search, name='search'),
]
Run the App from the Browser:

Run the following command to run Django server.


$ python3 manage.py runserver
Run the following URL from any browser to display the list of the books from the table.

http://localhost:8000




If the user clicks on the link, “PHP and MySQL for Dynamic Web Sites” then the details of this book will appear in the browser.




If the user searches the word, physics in the browser then the following search result will display in the browser.




Conclusion:

A Django app with the basic search option has been implemented in this tutorial by using database tables. The new Django developers will be able to implement the search feature in their website after reading this tutorial.

django
