import psycopg2

connection = psycopg2.connect(user='postgres',
                                password='admin',
                                host='127.0.0.1',
                                database='kites_db')

cursor = connection.cursor()

cursor.execute("INSERT INTO kites_game_thread VALUES (%s, %s)", ("The passenger door has been left open.Cheryl is nowhere to be seen.", "Page 6 (Empty seat of jeep)"))
connection.commit()