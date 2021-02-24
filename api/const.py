MAINLY_CITIES = [
    ("1", "Białystok"),
    ("2", "Bydgoszcz"),
    ("3", "Gdańsk"),
    ("4", "Gorzów Wielkopolski"),
    ("5", "Katowice"),
    ("6", "Kielce"),
    ("7", "Kraków"),
    ("8", "Lublin"),
    ("9", "Łódź"),
    ("10", "Olsztyn"),
    ("11", "Opole"),
    ("12", "Poznań"),
    ("13", "Rzeszów"),
    ("14", "Szczecin"),
    ("15", "Toruń"),
    ("16", "Warszawa"),
    ("17", "Wrocław"),
    ("18", "Zielona Góra"),
]
MAINLY_CITIES_BLANK = MAINLY_CITIES.copy()
MAINLY_CITIES_BLANK.append(("", ""))

def get_name_of_location(city_id:str):
    for _id, city_name in MAINLY_CITIES:
        if _id == city_id:
            return city_name


MESSAGE_400 = "Check your request data"

users_populate=[
    {
    "first_name":"f_name_test_1",
    "last_name":"l_name_test_1",
    "password":"test",
    "location":"1",
    "email":"user1@example.com"
     },
    {
    "first_name": "f_name_test_2",
    "last_name": "l_name_test_2",
    "password": "test",
    "location": "1",
    "email": "user2@example.com"
     },
    {
    "first_name": "f_name_test_3",
    "last_name": "l_name_test_3",
    "password": "test",
    "location": "1",
    "email": "user3@example.com"
     },
    {
    "first_name": "f_name_test_4",
    "last_name": "l_name_test_4",
    "password": "test",
    "location": "2",
    "email": "user4@example.com"
     },
    {
    "first_name": "f_name_test_5",
    "last_name": "l_name_test_5",
    "password": "test",
    "location": "2",
    "email": "user5@example.com"
     },
    {
    "first_name": "f_name_test_6",
    "last_name": "l_name_test_6",
    "password": "test",
    "location": "3",
    "email": "user6@example.com"
     }
    ]