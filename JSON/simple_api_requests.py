import requests
import time

# req = requests.get("https://kalob.io")
# print(req.status_code)

#A status code of 200 means that the website is up and running

while True:
    req = requests.get("https://courses.codingforeverybody.com")
    print(req.status_code)
    if req.status_code != 200:
        #Notify me
        pass
    time.sleep(60)