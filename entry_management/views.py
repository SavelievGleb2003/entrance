from django.shortcuts import render
from .models import PlanEntrance

# Create your views here.
def list_entrances(request):
    entrances = PlanEntrance.objects.filter()
    return render(request, 'entrances/list_entrances.html', {'entrances': entrances})
