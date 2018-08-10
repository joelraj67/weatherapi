import requests
import json
count=1
while[ count==0]:
 api_address='http://api.openweathermap.org/data/2.5/weather?appid=1192f6039ff6d2c8987a4ba6a2f4f6ed&q='
 city=input('Enter city_name:')
 url =api_address+city
 json_data =requests.get(url).json()
 format_data=json_data['weather'][0]
 print(format_data)
 print("Enter yes=1,no=0")
 guess=int(input(":"))
 if guess ==1:
   count=count
   print('new')
 else:
  print('OK')
  count=count+1
  exit()
