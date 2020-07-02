import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

import fasttext
model = fasttext.load_model('DLModel/fast_text_model/testModel.ftz')

def getSuggestions(request):
    global model
    if request.method == 'GET':
        try:
            keyword = request.GET.get('keyword')
            if keyword is None:
                raise Exception('Missing keyword')

            result = model.predict(keyword, k=5)
            print(result)
            raw_suggestions = list(result[0])
            suggestions = []
            for rs in raw_suggestions:
                suggestions.append(rs.split('__')[2])

            data = {
                'code': '200',
                'suggestions': suggestions,
                'reason': 'OK'
            }
        except Exception as e:
            print(e)
            data = {
                'code': '500',
                'reason': 'Server Error',
                'error': e
            }

        return JsonResponse(data)
    else:
        data = {
            'code': '400',
            'reason': 'Not a GET request'
        }
        return JsonResponse(data)


def index(request):
    return render(request, 'show.html')
