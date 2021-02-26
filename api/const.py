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


def get_name_of_location(city_id: str):
    for _id, city_name in MAINLY_CITIES:
        if _id == city_id:
            return city_name


MESSAGE_400 = "Check your request data"

USERS_POPULATE = [
    {
        "first_name": "f_name_test_1",
        "last_name": "l_name_test_1",
        "password": "test",
        "location": "1",
        "email": "user1@example.com"
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

ANNOUNCEMENTS_POPULATE = [
    {
        "text": "text_example_1",
        "language": "english",
        "location": "1",
        "owner": "user1@example.com"

    },
    {
        "text": "text_example_2",
        "language": "norwegian",
        "location": "1",
        "owner": "user2@example.com"

    },
    {
        "text": "text_example_3",
        "language": "norwegian",
        "location": "1",
        "owner": "user1@example.com"

    },
    {
        "text": "text_example_4",
        "language": "spanish",
        "location": "1",
        "owner": "user3@example.com"

    },
    {
        "text": "text_example_5",
        "language": "engilsh",
        "location": "2",
        "owner": "user3@example.com"

    },
    {
        "text": "text_example_6",
        "language": "norwegian",
        "location": "2",
        "owner": "user4@example.com"

    },
    {
        "text": "text_example_7",
        "language": "german",
        "location": "3",
        "owner": "user5@example.com"

    },
    {
        "text": "text_example_8",
        "language": "english",
        "location": "4",
        "owner": "user6@example.com"

    },
]

ANSWER_POPULATE = [
    {
        "text": "text_1",
        "owner": "user1@example.com",
        "announcement": 1
    },
    {
        "text": "text_2",
        "owner": "user2@example.com",
        "announcement": 1
    },
    {
        "text": "text_3",
        "owner": "user1@example.com",
        "announcement": 1
    },
    {
        "text": "text_4",
        "owner": "user2@example.com",
        "announcement": 2
    },
    {
        "text": "text_5",
        "owner": "user2@example.com",
        "announcement": 3
    },
    {
        "text": "text_6",
        "owner": "user3@example.com",
        "announcement": 2
    },
    {
        "text": "text_7",
        "owner": "user1@example.com",
        "announcement": 4
    },
    {
        "text": "text_8",
        "owner": "user6@example.com",
        "announcement": 5
    },
    {
        "text": "text_9",
        "owner": "user6@example.com",
        "announcement": 1
    },
    {
        "text": "text_10",
        "owner": "user4@example.com",
        "announcement": 1
    },
    {
        "text": "text_11",
        "owner": "user3@example.com",
        "announcement": 2
    },
]

REPUTATION_POPULATE = [
    {
        "rating": 5,
        "text": "reputation_1",
        "from_user": "user1@example.com",
        "to_user": "user2@example.com",
    },
    {
        "rating": 7,
        "text": "reputation_2",
        "from_user": "user3@example.com",
        "to_user": "user2@example.com",
    },
    {
        "rating": 2,
        "text": "reputation_3",
        "from_user": "user4@example.com",
        "to_user": "user2@example.com",
    },
    {
        "rating": 7,
        "text": "reputation_4",
        "from_user": "user2@example.com",
        "to_user": "user1@example.com",
    },
    {
        "rating": 5,
        "text": "reputation_5",
        "from_user": "user3@example.com",
        "to_user": "user1@example.com",
    },
    {
        "rating": 8,
        "text": "reputation_6",
        "from_user": "user4@example.com",
        "to_user": "user1@example.com",
    },
    {
        "rating": 3,
        "text": "reputation_7",
        "from_user": "user5@example.com",
        "to_user": "user1@example.com",
    },
    {
        "rating": 6,
        "text": "reputation_8",
        "from_user": "user1@example.com",
        "to_user": "user3@example.com",
    },
]
