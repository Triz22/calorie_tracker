from django.shortcuts import render

# Create your views here.

def home(request):
    import requests

    url = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"

    querystring = {"query":"1lb brisket with fries"}

    headers = {
	    "x-rapidapi-key": "6506df8921msh4ee0bc6580683d6p15dc39jsn37bad2b71c7c",
	    "x-rapidapi-host": "nutrition-by-api-ninjas.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

    return render(request, 'index.html')