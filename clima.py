import requests 
 
def consultar_clima(ciudad, api_key): 
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&un
its=metric' 
 
    print(url) 
    response = requests.get(url) 
    data = response.json() 
 
    if response.status_code == 200: 
        print("hola")