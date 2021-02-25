
INSERT_ANNOUNCEMENT = """
INSERT INTO announcement (text, created_time, location, owner, language) 
VALUES (%s, %s, %s, %s, %s);"""

GET_SPECIFIC_ANNOUNCEMENT = """
SELECT * 
FROM announcement
WHERE id = %s;
"""

GET_LIST_OF_ANNOUNCEMENT_OWNER = """
SELECT language, owner, location, id
FROM announcement
WHERE owner = %s;
"""

GET_LIST_OF_ANNOUNCEMENT_LOCATION = """
SELECT language, owner, location, id
FROM announcement
WHERE location = %s;
"""

GET_LIST_OF_ANNOUNCEMENT_LANGUAGE = """
SELECT language, owner, location, id
FROM announcement
WHERE language LIKE %s
;"""

GET_LIST_OF_ANNOUNCEMENT_LOCATION_AND_LANGUAGE = """
SELECT language, owner, location, id
FROM announcement
WHERE language LIKE %s AND location=%s
;"""

DELETE_ANNOUNCEMENT = """
DELETE FROM announcement
WHERE id = %s
"""

UPDATE_ANNOUNCEMENT = """
UPDATE announcement 
SET created_time=%s, language=%s, text=%s, location=%s
WHERE id=%s 
"""
