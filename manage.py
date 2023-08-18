import os
import sys
import psycopg2
import time
from django.conf import settings

MAX_RETRIES = 5  # Define the maximum number of reconnection attempts

def check_database_connection():
    """Check if the PostgreSQL database is connected."""
    retries = 0
    while retries < MAX_RETRIES:
        try:
            conn = psycopg2.connect(
                dbname=settings.DATABASES['default']['NAME'],
                user=settings.DATABASES['default']['USER'],
                password=settings.DATABASES['default']['PASSWORD'],
                host=settings.DATABASES['default']['HOST'],
                port=settings.DATABASES['default']['PORT'],
            )
            conn.close()
            print("Database connected successfully!")
            break  # Break out of the loop on successful connection
        except Exception as e:
            print("Database connection attempt failed:", e)
            retries += 1
            print(f"Retrying ({retries}/{MAX_RETRIES})...")
            time.sleep(2)  # Wait for a moment before retrying

    if retries >= MAX_RETRIES:
        print(f"Failed to connect to the database after {MAX_RETRIES} attempts.")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
    
    check_database_connection()
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
