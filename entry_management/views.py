from django.shortcuts import render
from .models import PlanEntrance
from django.utils.dateparse import parse_date
# Create your views here.
from django.utils.dateparse import parse_date
from django.shortcuts import render
from .models import PlanEntrance  # adjust as needed

def list_entrances(request):
    entrances = PlanEntrance.objects.all().order_by('-entry_exit_date')
    error_message = None  # initialize error message

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    try:
        if start_date:
            parsed_start = parse_date(start_date)
            if parsed_start:
                entrances = entrances.filter(entry_exit_date__date__gte=parsed_start)
            else:
                error_message = "Неверный формат даты для 'С даты'"
        if end_date:
            parsed_end = parse_date(end_date)
            if parsed_end:
                entrances = entrances.filter(entry_exit_date__date__lte=parsed_end)
            else:
                error_message = "Неверный формат даты для 'По дату'"
    except Exception as e:
        error_message = "Произошла ошибка при фильтрации по дате."

    return render(request, 'entrances/list_entrances.html', {
        'entrances': entrances,
        'error_message': error_message
    })



