import pickle
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from sqlalchemy import false

# Create your views here.
def home(request):
    return render(request,'home.html')
   


def result(request):
    
    model = pickle.load(open(r'C:\Users\sudee\Downloads\picklefil.pkl','rb'))
    print(model)
    lis = []
    lis.append(float(request.GET.get('GRE_score', False)))
    lis.append(float(request.GET.get('TOEFL_score', False)))
    lis.append(float(request.GET.get('university_rating', False)))
    lis.append(float(request.GET.get('SOP_score', False)))
    lis.append(float(request.GET.get('LOR_score', False)))
    lis.append(float(request.GET.get('CGPA', False)))
    print(lis)
    result = round(model.predict([lis])[0]*100,2)

    return render(request,'result.html', {'result':result})
