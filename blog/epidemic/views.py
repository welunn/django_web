from django.shortcuts import render
from django.views import View


# Create your views here.

class IndexView(View):
    def get(self, request):
        print("get......")
        return render(request, "epidemic/index.html")


    def post(self, request):
        username = request.POST.get("username")
        print(username)
        return render(request, "epidemic/main.html")

