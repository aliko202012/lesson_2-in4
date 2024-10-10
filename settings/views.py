from django.shortcuts import render
from settings.models import Setting

def nok(request):
    setting = Setting.objects.latest("id")
    return render(request, "index.html", locals())
