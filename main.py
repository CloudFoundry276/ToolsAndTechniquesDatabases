import sqlite3


def create_table():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
        CREATE TABLE "Seat" (
            "seat_id" TEXT, 
            "taken" INTEGER, 
            "price" REAL
        );
    """)
    connection.commit()
    connection.close()


def insert_record():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
    INSERT INTO "Seat" ("seat_id", "taken", "price") VALUES 
    ("A1", 0, 90), 
    ("A2", 1, 100), 
    ("A3", 0, 80)
    """)
    connection.commit()
    connection.close()


def select_all():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM "Seat"
    """)
    result = cursor.fetchall()
    connection.close()
    return result


def select_specific_columns():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT "seat_id", "price" FROM "Seat"
        """)
    result = cursor.fetchall()
    connection.close()
    return result


def select_with_condition():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT "seat_id", "price" FROM "Seat" WHERE "price" > 80
        """)
    result = cursor.fetchall()
    connection.close()
    return result


def update_value():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
    UPDATE "Seat" SET "taken" = 0 WHERE "seat_id" = "A3"
    """)
    connection.commit()
    connection.close()


def delete_record():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
    DELETE FROM "Seat" WHERE "seat_id" = "A3"
    """)
    connection.commit()
    connection.close()


def query_parameters(occupied, seat_id):
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
    UPDATE "Seat" SET "taken" = ? WHERE "seat_id" = ?
    """, [occupied, seat_id])
    connection.commit()
    connection.close()


# Execute following statements one after the other to check output
create_table()
insert_record()
print(select_all())
print(select_specific_columns())
print(select_with_condition())
update_value()
delete_record()
query_parameters(occupied=0, seat_id="A2")
