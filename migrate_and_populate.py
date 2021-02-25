from api.database.populate import populate
from api.database.migration import run_create_tables

if __name__ == "__main__":
    run_create_tables()
    populate()
