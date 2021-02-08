
INSERT_ADVERTISEMENT = """
INSERT INTO advertisement (text, created_time, loaction, owner, language) 
VALUES (%s, %s, %s, %s, %s);"""