from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home page"""
    template_name = "home/index.html"
