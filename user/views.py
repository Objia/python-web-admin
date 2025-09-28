from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class Testview(View):
    def get(self, request):
        return JsonResponse({'code':200,'info':'测试！'})