from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query'
        api_request = requests.get(api_url + query, headers ={'X-Api-Key':'yHk5grW8pkVr7MXyZQytZg==RkzMMKohDBMFXg8y'})

    return render(request, 'index.html')