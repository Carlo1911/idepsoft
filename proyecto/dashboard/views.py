from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class DashboardMixin:

    def get_context_data(self, **kwargs):
        user = None
        if self.request.user.is_authenticated():
            user = self.request.user
        context = super(DashboardMixin, self).get_context_data(**kwargs)
        context["usuario"] = user
        return context


class HomeView(DashboardMixin, TemplateView):

    """docstring for ClassName"""
    template_name = "home.html"
