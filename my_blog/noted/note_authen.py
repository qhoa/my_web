# 1 Decorate the view when you instantiate it in your urls.py (docs)

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('view/',login_required(ViewSpaceIndex.as_view(..)),
    ...
]
The decorator is applied on a per-instance basis, so you can add it or remove it in different urls.py routes as needed.

Decorate your class so every instance of your view is wrapped (docs)

There's two ways to do this:

# 2 Apply method_decorator to your CBV dispatch method e.g.,

 from django.utils.decorators import method_decorator
 from django.contrib.auth.decorators import login_required

 @method_decorator(login_required, name='dispatch')
 class ViewSpaceIndex(TemplateView):
     template_name = 'secret.html'
If you're using Django < 1.9 (which you shouldn't, it's no longer supported) you can't use method_decorator on the class, so you have to override the dispatch method manually:

    from django.contrib.auth.decorators import login_required

    class ViewSpaceIndex(TemplateView):

        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
            return super(ViewSpaceIndex, self).dispatch(*args, **kwargs)
# 3 Use a mixin like django.contrib.auth.mixins.LoginRequiredMixin outlined well in the other answers here:

 from django.contrib.auth.mixins import LoginRequiredMixin

 class MyView(LoginRequiredMixin, View):

     login_url = '/login/'
     redirect_field_name = 'redirect_to'
Make sure you place the mixin class first in the inheritance list (so Python's Method Resolution Order algorithm picks the Right Thing).

The reason you're getting a TypeError is explained in the docs:

Note: method_decorator passes *args and **kwargs as parameters to the decorated method on the class. If your method does not accept a compatible set of parameters it will raise a TypeError exception.