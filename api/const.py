MAINLY_CITIES = (
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
)


def get_name_of_location(city_id):
    for _id, city_name in MAINLY_CITIES:
        if _id == city_id:
            return city_name

