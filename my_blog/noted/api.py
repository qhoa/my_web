To create an API endpoint for creating new posts in Django, you can follow these steps:

1. Install the Django REST Framework (DRF) if you haven't already. You can install it using pip:

```bash
pip install djangorestframework
```

2. Add `'rest_framework'` to the `INSTALLED_APPS` list in your project's settings (`settings.py`).

```python
INSTALLED_APPS = [
    # Other installed apps...
    'rest_framework',
]
```

3. Create a serializer to define the structure of the data that will be sent and received in the API:

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
```

In the serializer, `PostSerializer` is defined based on the `Post` model. It includes all fields of the model (`'__all__'`), but you can specify specific fields if needed.

4. Create a view using Django's Class-based views or Function-based views. Here's an example using Class-based views:

```python
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

In the view, `PostCreateAPIView` is defined as a subclass of `generics.CreateAPIView`. It sets the `queryset` attribute to retrieve all `Post` objects and the `serializer_class` attribute to use the `PostSerializer` for serialization and deserialization.

5. Include the API endpoint in your project's URLs (`urls.py`):

```python
from django.urls import path
from .views import PostCreateAPIView

urlpatterns = [
    # Other URLs...
    path('api/posts/create/', PostCreateAPIView.as_view(), name='api_post_create'),
]
```

In the above example, a path is defined for the API endpoint at `api/posts/create/`, and it is mapped to the `PostCreateAPIView` view.

Make sure to adjust the code according to your specific project structure, model names, and URL configuration.

With these steps, you have an API endpoint at `/api/posts/create/` that accepts POST requests to create new posts. The data sent in the request body will be validated and saved as a new `Post` object. The response will include the serialized data of the created post.

To extend the API for retrieving, updating, and deleting posts, you can modify the code as follows:

1. Retrieve a single post using GET:
```python
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```
In the above code, `PostRetrieveAPIView` is defined as a subclass of `generics.RetrieveAPIView`. It retrieves a single post using the `queryset` attribute and serializes it using the `PostSerializer`.

2. Update a post using PUT:
```python
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```
Here, `PostUpdateAPIView` is defined as a subclass of `generics.UpdateAPIView`. It updates a post using the `queryset` attribute and the `PostSerializer` for serialization and deserialization.

3. Delete a post using DELETE:
```python
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```
In the above code, `PostDeleteAPIView` is defined as a subclass of `generics.DestroyAPIView`. It deletes a post using the `queryset` attribute and the `PostSerializer`.

4. Include the new API endpoints in your project's URLs:
```python
from django.urls import path
from .views import (
    PostCreateAPIView,
    PostRetrieveAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
)

urlpatterns = [
    # Other URLs...
    path('api/posts/create/', PostCreateAPIView.as_view(), name='api_post_create'),
    path('api/posts/<int:pk>/', PostRetrieveAPIView.as_view(), name='api_post_retrieve'),
    path('api/posts/<int:pk>/update/', PostUpdateAPIView.as_view(), name='api_post_update'),
    path('api/posts/<int:pk>/delete/', PostDeleteAPIView.as_view(), name='api_post_delete'),
]
```
The above code adds three new URL patterns for retrieving, updating, and deleting posts. `<int:pk>` captures the post's primary key, and it is passed as a parameter to the corresponding view.

Now, you have the following API endpoints:
- `api/posts/create/`: POST request to create a new post
- `api/posts/<int:pk>/`: GET request to retrieve a single post
- `api/posts/<int:pk>/update/`: PUT request to update a post
- `api/posts/<int:pk>/delete/`: DELETE request to delete a post

Make sure to adjust the code based on your project structure, model names, and URL configuration.