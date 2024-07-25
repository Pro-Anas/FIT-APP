from django.shortcuts import render

#EbVDWGD8qM8pSCbBl6hRnA==Sr1Y4HBxqGgD2BTd
# Create your views here.
def home(request):
    import requests
    import json
    
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get (api_url + query, headers = {'X-Api-Key': 'EbVDWGD8qM8pSCbBl6hRnA==Sr1Y4HBxqGgD2BTd'})
        try:
            api = json.loads{api_request.content}
            print(api_request.content)
            
    return render(request, 'home.html')