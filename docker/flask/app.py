from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '2ad207f1576cc623c5396f3df877c5d7'  # Получите API-ключ на openweathermap.org

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return render_template('weather.html', city=city, weather_description=weather_description, temperature=temperature)
    else:
        return render_template('index.html', error=data['message'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
