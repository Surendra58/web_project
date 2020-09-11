#from django.shortcuts import render
# Create your views here.
#from django.http import HttpResponse
#def home(request):
#    text="Hello and Welcome to my first Application"
    #return HttpResponse("Hello, Django!")
#    return HttpResponse(text)
    
#   Code changes here to make a calendar

#from django.shortcuts import render
#from django.http import HttpResponse
#import datetime
#import calendar
#from calendar import HTMLCalendar
#def index(request):
#    year = datetime.date.today().year
#    month = datetime.date.today().month
#    month_name=calendar.month_name[month]
#    title = f"Web Project calendar for the month of  {month_name}:{year}"
#    cal = HTMLCalendar().formatmonth(year,month)
    #return HttpResponse(cal)
#    return render(request,'base.html',{'title':title,'cal':cal})
    
#  User can show calender of any year
#  Here user can view any calendar for any year and month between 1980 to 2099:e.g.:http://127.0.0.1:8000/cal/2019/08
from django.shortcuts import render
from django.http import HttpResponse
import datetime
import calendar
from calendar import HTMLCalendar
def index(request,year=datetime.date.today().year,month=datetime.date.today().month):
    year=int(year)
    month=int(month)
    if year < 1980 or year > 2099:
        year = datetime.date.today().year
    month_name=calendar.month_name[month]
    title = f"Web Project calendar for the month of  {month_name}:{year}"
    cal = HTMLCalendar().formatmonth(year,month)
    return render(request,'base.html',{'title':title,'cal':cal})



