from django.views.generic import TemplateView


# Create your views here.
class login(TemplateView):
    template_name = 'login.html'
