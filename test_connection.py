from database import get_db_connection


try:
    connection = get_db_connection()

    if connection.is_connected():
        print("SUCCESS: Connected to MySQL database!")

        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")

        database_name = cursor.fetchone()[0]
        print(f"Connected database: {database_name}")

        cursor.close()
        connection.close()

except Exception as error:
    print("ERROR:", error)