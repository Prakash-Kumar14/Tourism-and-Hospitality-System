from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('report.urls')),
]
 create urls in report app

urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='memddddd'),
]

3) views.py

from django.shortcuts import render
import requests  # Add this import statement

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=YOUR_API_KEY'

    if request.method == 'POST':
        city = request.POST.get('city')
        response = requests.get(url.format(city)).json()
        if response['cod'] == 200:  # Check if the response is successful
            weather_data = {
                'city': city,
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description']
            }
        else:
            weather_data = None  # In case of an unsuccessful response, set weather_data to None

        return render(request, 'index.html', {'weather_data': weather_data})

    return render(request, 'index.html')


4) create the templates folder under the app

templates----->index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Weather App</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-image: url('https://png.pngtree.com/thumb_back/fh260/background/20220217/pngtree-blue-atmospheric-weather-forecast-illustration-background-image_948664.jpg'); /* Set background image */
            background-size: cover;
            background-position: center;
            color: #333; /* Set front color */
            font-family: Arial, sans-serif;
        }

        #weatherData {
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <form id="weatherForm">
        <label for="cityInput">Enter City Name:</label>
        <input type="text" id="cityInput" name="cityInput">
        <button type="submit">Submit</button>
    </form>

    <div id="weatherData">
        <h2>Weather Information</h2>
        <p>Date: <span id="date"></span></p>
        <p>Temperature: <span id="temperature"></span></p>
        <p>Description: <span id="description"></span></p>
    </div>

    <script>
        const form = document.getElementById('weatherForm');
        form.addEventListener('submit', async function(event) {
            event.preventDefault();
            const city = document.getElementById('cityInput').value;
            // Simulate random temperature and description
            const randomTemp = Math.floor(Math.random() * 50); // Generate a random temperature between 0 and 50
            const randomDescription = ['Clear', 'Cloudy', 'Rainy', 'Sunny'][Math.floor(Math.random() * 4)]; // Randomly select a description
            document.getElementById('date').textContent = new Date().toLocaleDateString();
            document.getElementById('temperature').textContent = randomTemp + "°C";
            document.getElementById('description').textContent = randomDescription;
        });
    </script>
</body>
</html>rom django.shortcut import render


