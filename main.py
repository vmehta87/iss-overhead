import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 45.529972
MY_LNG = -73.564376
my_email = '87vmehta.test@gmail.com'
password = 'uznaelgyfuhxpgwz'


def its_here():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if iss_latitude in range(MY_LAT - 5, MY_LAT + 5) and iss_longitude in range(MY_LNG - 5, MY_LNG + 5):
        print('its fuckin here!!')
        return


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if sunset < time_now < sunrise:
        return


while True:
    time.sleep(60)
    if is_night() and its_here():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='test.87vmehta@gmail.com',
                msg=f"Subject:It's on top now! and its dark so u can see it! email sent by coding\n\n "
                    f"it actualy did come, this program worked.")
