INSERT_USER = """
INSERT INTO users (first_name, last_name, email, loaction, hashed_password) 
VALUES (%s, %s, %s, %s, %s);"""

CHECK_USER_EMAIL = """
    SELECT id FROM users WHERE email = %s AND disabled = false;
"""

TAKE_HASHED_PASSWORD_FOR_USER_IN_DB = """
    SELECT hashed_password FROM users WHERE email = %s;
"""

GET_USER_ALL_INFO = """
    SELECT first_name, last_name, email, loaction  FROM users WHERE email = %s AND disabled = false;
"""

GET_ALL_USERS_ORDER_BY = """
    SELECT first_name, last_name, email, loaction  FROM users WHERE disabled = false ORDER BY loaction ASC;
"""