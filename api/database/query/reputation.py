INSERT_REPUTATION = """
INSERT INTO reputation (from_user, to_user, created_time, rating, text) 
VALUES (%s, %s, %s, %s, %s);"""

CHECK_NO_REPEAT_REPUTATION_FOR_USER = """
SELECT id FROM reputation WHERE from_user=%s AND to_user=%s ;"""

UPDATE_REPUTATION = """
UPDATE reputation SET rating=%s WHERE from_user=%s AND to_user=%s ;"""