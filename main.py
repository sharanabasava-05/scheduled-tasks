import os

APIKEY = os.environ.get("APIKEY")
phone_num = os.environ.get('phone_num')
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
parm={
     "lat":15.139393,
    "lon": 76.921440,
    "appid":APIKEY,
    "cnt":4
}
respone = requests.get(OWM_endpoint,params=parm)
respone.raise_for_status()
weather_data = respone.json()
weather_data_list=[]


will_rain = False
for i in range(len(weather_data["list"])):
    condition_code = weather_data["list"][i]["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body = "It's going to rain today. Remember to take an umbrella☂️",
        to = phone_num
    )
