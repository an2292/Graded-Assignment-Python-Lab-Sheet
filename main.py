import sqlite3
import os


def run_sql(cursor, filepath):
    """Run SQL statements from a file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"SQL file {filepath} does not exist.")

    with open(filepath, "r") as file:
        sql_script = file.read()

    # Run all SQL statements in the file
    cursor.executescript(sql_script)


def create_databases():
    """Create databases for the application and seed them with test data."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    try:
        # Create tables
        run_sql(cursor, "./create-table.sql")
        print("Tables created.")

        run_sql(cursor, "./populate-table.sql")
        print("Tables populated with test data.")

        conn.commit()

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()

    finally:
        conn.close()


if __name__ == "__main__":
    create_databases()
