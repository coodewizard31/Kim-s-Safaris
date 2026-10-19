from sqlalchemy import text
from database import engine


def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT version();")
            )

            print("Database connection successful!")
            print("PostgreSQL version:", result.scalar())

    except Exception as error:
        print("Database connection failed!")
        print("Error type:", type(error).__name__)


if __name__ == "__main__":
    test_connection()