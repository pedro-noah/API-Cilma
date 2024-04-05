import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()
CIDADE = "Curitiba"

def kelvin_para_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit    

url = BASE_URL + "appid=" + API_KEY + "&q=" + CIDADE

resposta = requests.get(url).json()

temperatura_kelvin = resposta['main']['temp']
temperatura_celsius, temperatura_fahrenheit = kelvin_para_celsius_fahrenheit(temperatura_kelvin)
sensacao_kelvin = resposta['main']['feels_like']
sensacao_celsius, sensacao_fahrenheit = kelvin_para_celsius_fahrenheit(sensacao_kelvin)
velocidade_vento = resposta['wind']['speed']
umidade = resposta['main']['humidity']
descricao = resposta['weather'][0]['description']
nascer_sol = dt.datetime.utcfromtimestamp(resposta['sys']['sunrise'] + resposta['timezone'])
por_do_sol = dt.datetime.utcfromtimestamp(resposta['sys']['sunset'] + resposta['timezone'])


print(f'Temperatura em {CIDADE}: {temperatura_celsius:.2f}C ou {temperatura_fahrenheit:.2f}F')
print(f'Temperatura em {CIDADE} tem sensação térmica de: {sensacao_celsius:.2f}C ou {sensacao_fahrenheit:.2f}F')
print(f'Umidade em {CIDADE}: {umidade}%')
print(f'Velocidade de vento em {CIDADE}: {velocidade_vento}m/s')
print(F'Temperatura Geral em {CIDADE}: {descricao}')
print(f'Nascer do sol em {CIDADE}: {nascer_sol} (horario local)')
print(f'Pôr do sol em {CIDADE}: {por_do_sol} (horario local)')