
INSERT_ANNOUNCEMENT = """
INSERT INTO announcement (text, created_time, location, owner, language) 
VALUES (%s, %s, %s, %s, %s);"""


GET_SPECIFIC_ANNOUNCEMENT = """
SELECT * FROM announcement
WHERE id = %s;
"""

GET_LIST_OF_ANNOUNCEMENT_OWNER = """
SELECT language, owner, location FROM announcement
WHERE owner = %s;
"""

GET_LIST_OF_ANNOUNCEMENT_LOCATION = """
SELECT language, owner, location FROM announcement
WHERE location = %s;
"""