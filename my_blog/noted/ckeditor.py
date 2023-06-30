How to integrate CKEditor to your Django Admin and form fields
In this article, we'll be integrating CKEditor into your Django admin and form fields with in just simple steps.
 8 min read
 

In this article, we'll be integrating a rich WYSIWYG editor into your Django application within just a few steps. Django-CKEditor is one of the best editors which comes with lots of useful functionalities for creating rich HTML content. So let's see how can we integrate CKEditor into your Django application.

Table of Contents:
Installing CKEditor
Adding path for media files
Setup URLs
Change in the model
Configuring CKEditor
Creating model form

Installing CKEditor

The first step is to install the Django-CKEditor. You can directly install using pip,

$ pip3 install django-ckeditor

 After installation, you need to add the CKEditor to the installed_apps in settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor', # CKEditor config
    'ckeditor_uploader', # CKEditor media uploader
]

Here we are adding ckeditor and ckeditor_uploader to the installed_apps for handling CKEditor and CKEditor media files. 
Adding path for media files

For enabling the file upload feature you'll need to specify the place and the path where all the media files want to be stored. In the settings.py you can add the path and root folder for this.

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#ckeditor upload path
CKEDITOR_UPLOAD_PATH="uploads/"

Django will create a folder media in your base directory where you can find all the media files including images, videos, audios, etc that are uploaded via CKEditor.
Setup URLs

In the project urls.py, we need to add two things. First is the CKEditor URL and the path of the media files where Django can identify the location of media files.  

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path

]

# Path of media files
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
Change in the model

For our CKEditor to work in both admin and form fields, we must change the body of the model field from the raw text field to CKEditor rich text field. Head over to models.py and make these changes.

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=255)
    #body = models.TextField() 
    body = RichTextUploadingField() # CKEditor Rich Text Field

    def __str__(self):
        return self.title

The model has been changed from raw text field to CKEditor rich text and uploading field. Now let's run our migrations.

run all migrations

$ python manage.py makemigrations

and migrate the changes

$ python manage.py migrate

Don't forget to add your model to admin.py else it will not show on your Django admin panel.

Run the development server using the "python manage.py runserver" command and go to localhost:8000/admin, click on the post and you can see the CKEditor rich text is being added in the body field.

CKEditor Django

Configuring CKEditor

The CKEditor you'll see is the default, you can add more functionalities and extra plugins by configuring CKEditor in the

settings.py. Anyway here is the advanced CKEditor configuration.


CKEDITOR_CONFIGS = {
    'default': {
     
        'toolbar_Custom': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Youtube','Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['CodeSnippet']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'Custom',  # put selected toolbar config here
        'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        'height': 400,
        # 'width': '100%',
        'filebrowserWindowHeight': 725,
        'filebrowserWindowWidth': 940,
        'toolbarCanCollapse': True,
        'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'codesnippet',
        ]),
    }
}



You can add these configurations to your CKEditor and it will reflect in your admin panel.
Creating model form

So we successfully added CKEditor to our admin panel, but let's suppose you are willing to make it public for everyone to write a post on your blog, you can use Django forms.

In order to use Django forms, first, you need to create a forms.py file in the blog directory, and then add the model fields inside the form just like this:


from django.forms import ModelForm
from.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']

To show these form fields in your template, go to views.py and pass the form data to the template.

from django.shortcuts import render
from.models import Post
from.forms import PostForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):

    form = None
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:

        form = PostForm()
    return render(request, 'index.html',{'form':form})

The above function will save the form to the database and also pass the form fields to the 'index.html' template. Here we are using the POST method to send the data that needs to be stored in the database.

index.html

<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Page Title</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
</head>

<body>
    
    <form method="post">
        {% csrf_token %}
    <div class="form-outline">
        {{form.as_p}}
        <br>
    </div>  
    <!--Blog Text Area-->
        {{form.media}}
        <input type="submit">
    </form>

</body>
</html>

After adding the forms to your template as shown above you'll see the forms field appeared on your template.