from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    query = '1lb brisket and fries'
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'yHk5grW8pkVr7MXyZQytZg==RkzMMKohDBMFXg8y'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

    return render(request, 'index.html')