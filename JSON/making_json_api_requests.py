import requests
import json

#API stands for Application Programming Interface. Basically, it is a database on the web. To use the data in your code, you have to import a module called requests. 
#You can request data from an API, and when you do that, it will go to that website and retrieve the data. Using the .json() function, you cn turn that data into a 
#Python dicionary. Then you can access that data in your program, like shown in the first example. If you just copy the data from an API, like I did in the second example, 
#then you have to use json.loads() and json.dumps()(import json first!). json.loads() takes JSON and converts it into a Python dictionary. Then you can make changes to 
#the dictionary, and to "save it", you would use json.dumps() to make sure your changes are in the dictionary. 

req = requests.get("https://swapi.dev/api/people/2/")
person = req.json()
print(person)
print(f"Name is\t\t\t{person['name']}")
print(f"Birth Year is\t\t{person['birth_year']}")

for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print(f"{person['name']} is in the movie {film['title']}")

luke = '''{
	"name": "Luke Skywalker",
	"height": "172",
	"mass": "77",
	"hair_color": "blond",
	"skin_color": "fair",
	"eye_color": "blue",
	"birth_year": "19BBY",
	"gender": "male",
	"homeworld": "https://swapi.dev/api/planets/1/",
	"films": [
		"https://swapi.dev/api/films/2/",
		"https://swapi.dev/api/films/6/",
		"https://swapi.dev/api/films/3/",
		"https://swapi.dev/api/films/1/",
		"https://swapi.dev/api/films/7/"
	],
	"species": [
		"https://swapi.dev/api/species/1/"
	],
	"vehicles": [
		"https://swapi.dev/api/vehicles/14/",
		"https://swapi.dev/api/vehicles/30/"
	],
	"starships": [
		"https://swapi.dev/api/starships/12/",
		"https://swapi.dev/api/starships/22/"
	],
	"created": "2014-12-09T13:50:51.644000Z",
	"edited": "2014-12-20T21:17:56.891000Z",
	"url": "https://swapi.dev/api/people/1/"
}'''

luke = json.loads(luke)
luke['name'] = "Skywalker Luke"

luke_str = json.dumps(luke)
print(luke_str)

print(luke['name'])