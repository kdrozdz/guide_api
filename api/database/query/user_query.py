INSERT_USER = """
INSERT INTO users (first_name, last_name, email, location, hashed_password) 
VALUES (%s, %s, %s, %s, %s);"""

CHECK_USER_EMAIL = """
    SELECT id FROM users WHERE email = %s AND disabled = false;
"""

TAKE_HASHED_PASSWORD_FOR_USER_IN_DB = """
    SELECT hashed_password FROM users WHERE email = %s;
"""

GET_USER_ALL_INFO = """
    SELECT users.email, users.first_name, users.last_name, users.location,
     AVG(reputation.rating )::numeric(10,2), COUNT(reputation.rating)
FROM users
JOIN reputation ON users.email = reputation.to_user
WHERE users.email = %s
GROUP BY users.email
;"""

GET_ALL_USERS_ORDER_BY = """
    SELECT first_name, last_name, email, location  FROM users WHERE disabled = false ORDER BY location;
"""
