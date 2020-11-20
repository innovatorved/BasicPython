import requests
res=requests.get('https://api.thingspeak.com/channels/967543/feeds.json?api_key=N4SBSBE6FXGC4Y1J&results=2')
print(res.json())

r=requests.post(' https://api.thingspeak.com/update?api_key=42VSPVO6T55NVVLK&field1=0')
field1=12
print(r.json())
