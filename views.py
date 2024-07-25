from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    context = {}
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'zGwruJqPqw+D+QlL3KkSRA==IDgzHuDRWvtcEy9h'})
        try:
            api = json.loads(api_request.content)
            context['api'] = api
        except Exception as e:
            context['error'] = "Oops! There was an error"
            print(e)
    else:
        context['query'] = 'Enter a valid query'

    return render(request, 'home.html', context)
