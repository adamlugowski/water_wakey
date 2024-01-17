import sqlite3
from app import main, db_init


if __name__ == "__main__":
    print('This simple app keep your body hydrated!')
    print('This app will ask you to drink water each 30 minutes')
    print("Type 'ok' when you already drunk a cup and the information will be added to database")
    with sqlite3.connect('hydration.db') as init_database:
        cursor = init_database.cursor()
        db_init(cursor)
        main()
