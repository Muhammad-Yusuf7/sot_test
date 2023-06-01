from django.shortcuts import render
from . import bot
# Create your views here.

def index(request):
    if request.method == "POST":
        message = request.POST["message"]
        bot.send(message)
    return render(request,"index.html")

