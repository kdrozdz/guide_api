
INSERT_ADVERTISEMENT = """
INSERT INTO advertisement (text, created_time, location, owner, language) 
VALUES (%s, %s, %s, %s, %s);"""