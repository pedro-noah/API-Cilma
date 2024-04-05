import datetime as dt
import requests
from colorama import Fore, Style

"""
Este programa consulta a API OpenWeatherMap para obter informações climáticas de uma cidade fornecida pelo usuário.

Requerimentos:
    - Uma chave de API da OpenWeatherMap, disponível em http://openweathermap.org/
    - Um arquivo chamado 'api_key' contendo a chave de API, localizado no mesmo diretório que este script.
    - Módulos Python: datetime, requests, colorama
    
Parâmetros:
    - Nenhum

Retornos:
    - Nenhum, o programa imprime as informações climáticas na saída padrão.

Exemplo de uso:
    Execute o script e siga as instruções para inserir o nome da cidade desejada e a opção de visualização das informações climáticas.

Módulos:
    - datetime: Manipulação de objetos de data e hora.
    - requests: Para fazer solicitações HTTP à API OpenWeatherMap.
    - colorama: Para formatar a saída do console com cores.

Funções:
    - kelvin_para_celsius_fahrenheit(kelvin): Converte uma temperatura de Kelvin para Celsius e Fahrenheit.
    - imprimir_titulo(texto): Imprime um título formatado para as informações climáticas.

Variáveis Globais:
    - BASE_URL: URL base da API OpenWeatherMap.
    - API_KEY: Chave de API da OpenWeatherMap, lida a partir de um arquivo chamado 'api_key'.
    - CIDADE: Nome da cidade fornecida pelo usuário.
    - opc: Opção selecionada pelo usuário para visualizar todas as informações de uma vez ou selecionar uma informação específica.
    - menu_info: Opção selecionada pelo usuário para visualizar uma informação específica.

Exemplo:
    $ python clima.py
    Digite a cidade para verificar informações de temperatura: London
    --INFORMAÇÕES CLIMÁTICAS--

    INFORMAÇÕES CLIMÁTICAS PARA LONDON

    Escolha:
    [1] - Pegar todas as informações de uma vez
    [2] - Selecionar uma informação específica
    1
    Temperatura em London: 10.36C ou 50.65F
    Temperatura em London tem sensação térmica de: 7.45C ou 45.41F
    Umidade em London: 76%
    Velocidade de vento em London: 4.47m/s
    Temperatura Geral em London: broken clouds
    Nascer do sol em London: 2024-04-05 05:55:18 (horario local)
    Pôr do sol em London: 2024-04-05 18:19:21 (horario local)
"""


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()

def kelvin_para_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def imprimir_titulo(texto):
    print('\n--INFORMAÇÕES CLIMÁTICAS--\n')
    print(Fore.CYAN + Style.BRIGHT + texto + Style.RESET_ALL)  
    
CIDADE = input('Digite a cidade para verificar informações de temperatura: ').title()

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

imprimir_titulo(f"INFORMAÇÕES CLIMÁTICAS PARA {CIDADE.upper()}")

opc = int(input('''\n
    Escolha:
    [1] - Pegar todas as informações de uma vez
    [2] - Selecionar uma informação específica
                \n'''))
match opc:
    case 1:
        print(f'Temperatura em {CIDADE}: {temperatura_celsius:.2f}C ou {temperatura_fahrenheit:.2f}F')
        print(f'Temperatura em {CIDADE} tem sensação térmica de: {sensacao_celsius:.2f}C ou {sensacao_fahrenheit:.2f}F')
        print(f'Umidade em {CIDADE}: {umidade}%')
        print(f'Velocidade de vento em {CIDADE}: {velocidade_vento}m/s')
        print(F'Temperatura Geral em {CIDADE}: {descricao}')
        print(f'Nascer do sol em {CIDADE}: {nascer_sol} (horario local)')
        print(f'Pôr do sol em {CIDADE}: {por_do_sol} (horario local)')
    case 2:
        menu_info = int(input('''\n
            Digite o número correspondente que deseja:
            [1] - Verificar a temperatura exata
            [2] - Verificar a sensação térmica
            [3] - Verificar a umidade
            [4] - Verificar a velocidade do vento
            [5] - Verificar a descrição da temperatura geral
            [6] - Verificar o horário de nascer do sol
            [7] - Verificar o horário de pôr so sol
                            \n'''))
        match menu_info:
            case 1:
                print(f'Temperatura em {CIDADE}: {temperatura_celsius:.2f}C ou {temperatura_fahrenheit:.2f}F')
            case 2:
                print(f'Temperatura em {CIDADE} tem sensação térmica de: {sensacao_celsius:.2f}C ou {sensacao_fahrenheit:.2f}F')
            case 3:
                print(f'Umidade em {CIDADE}: {umidade}%')
            case 4: 
                print(f'Velocidade de vento em {CIDADE}: {velocidade_vento}m/s')
            case 5:
                print(F'Temperatura Geral em {CIDADE}: {descricao}')
            case 6:
                print(f'Nascer do sol em {CIDADE}: {nascer_sol} (horario local)')
            case 7:
                print(f'Pôr do sol em {CIDADE}: {por_do_sol} (horario local)')
            case _:
                print("Opção Inválida!")
    case _:
        print("Opção Inválida!")
                
                
        
        








