
CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    loaction CHAR NOT NULL,
    hashed_password VARCHAR NOT NULL,
    disabled boolean DEFAULT false);"""

CREATE_ADVERTISEMENT_TABLE = """CREATE TABLE IF NOT EXISTS advertisement (
    id SERIAL PRIMARY KEY,
    text VARCHAR NOT NULL,
    created_time REAl NOT NULL,
    loaction SMALLINT NOT NULL,
    owner INTEGER NOT NULL REFERENCES  users ON DELETE CASCADE
    );"""
CREATE_ADVICES_TABLE = """CREATE TABLE IF NOT EXISTS advices (
    id SERIAL PRIMARY KEY,
    text VARCHAR NOT NULL,
    created_time REAl NOT NULL,
    owner INTEGER NOT NULL REFERENCES users ON DELETE CASCADE,
    advertisement INTEGER NOT NULL REFERENCES advertisement ON DELETE CASCADE
    );"""

CREATE_REPUTATIONS_TABLE = """CREATE TABLE IF NOT EXISTS reputations (
    id SERIAL PRIMARY KEY,
    from_user INTEGER NOT NULL REFERENCES users ON DELETE CASCADE,
    to_user INTEGER NOT NULL REFERENCES users ON DELETE CASCADE,
    created_time REAl NOT NULL,
    UNIQUE (from_user, to_user)
    );"""

