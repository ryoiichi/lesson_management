from django.shortcuts import render
from django.http import HttpResponse
from sample.models import lesson

# Create your views here.
def index(request):
    lessons = lesson.objects.all().order_by('id') #値を取得
    return render(request, 'sample/index.html', {'lessons':lessons}) #Templateに値を渡す
