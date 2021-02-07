INSERT_USER = """
INSERT INTO users (first_name, last_name, email, loaction, hashed_password) 
VALUES (%s, %s, %s, %s, %s);"""

CHECK_USER_EMAIL = """
    SELECT id FROM users WHERE email = %s;
"""
