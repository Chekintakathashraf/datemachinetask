
from django.shortcuts import render
from .forms import DateRangeForm
from datetime import timedelta

def date_range(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date1 = form.cleaned_data['startingdate']
            date2 = form.cleaned_data['endingdate']
            Daily_dates = []
            Weekly_dates = []
            Monthly_dates = []
            Annual_dates = []
            current_date = date1
            while current_date <= date2:
                Daily_dates.append(current_date)
                if current_date.weekday() == 6:  
                    Weekly_dates.append(current_date)
                if current_date.day == 1:  
                    Monthly_dates.append(current_date)
                if current_date.month == 1 and current_date.day == 1:  
                    Annual_dates.append(current_date)
                current_date += timedelta(days=1)
            return render(request, 'datem.html', {
                'form': form,
                'Daily_dates': Daily_dates,
                'Weekly_dates': Weekly_dates,
                'Monthly_dates': Monthly_dates,
                'Annual_dates': Annual_dates,
            })
    else:
        form = DateRangeForm()
    return render(request, 'datem.html', {'form': form})
