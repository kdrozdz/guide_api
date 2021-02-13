
INSERT_ANNOUNCEMENT = """
INSERT INTO announcement (text, created_time, location, owner, language) 
VALUES (%s, %s, %s, %s, %s);"""