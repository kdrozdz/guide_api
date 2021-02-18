INSERT_ANSWER = """
INSERT INTO answer (text, created_time, owner, announcement) 
VALUES (%s, %s, %s, %s);"""


GET_ALL_ANSWER_FOR_ANNOUNCEMENT = """
SELECT text, created_time, owner FROM answer
WHERE announcement = %s
ORDER BY id DESC
;"""

DELETE_ANSWER = """
DELETE FROM answer
WHERE id = %s  
;"""

UPDATE_ANSWER = """
UPDATE answer SET created_time=%s, text=%s
WHERE id=%s
;"""