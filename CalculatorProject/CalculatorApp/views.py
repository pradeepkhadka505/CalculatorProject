from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit_query(request):
    q = request.GET['query']

    try:
        ans = eval(q)
        my_dict = {
            "q" : q,
            "ans": ans,
            "error": False,
            "result" : True

        }
        return render(request, 'index.html', context = my_dict)
    except:
        my_dict ={
            "error": True,
            "result": False

        }
        return render(request, 'index.html', context= my_dict)
