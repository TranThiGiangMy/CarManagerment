from django.http import HttpResponse
from django.test import TestCase

# Create your tests here.
from django.views import View


class TestView(View):
    def get(self, request):
        return HttpResponse ("WELCOM")

    def post(self, request):
        pass
