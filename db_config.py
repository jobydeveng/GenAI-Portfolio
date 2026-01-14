"""
Database configuration and connection management

This project originally used MySQL (local / Railway).
It is now migrated to PostgreSQL (Neon – free tier).

⚠ IMPORTANT:
- MySQL code is KEPT for reference / fallback
- PostgreSQL (Neon) is the ACTIVE connection
"""

import os
from dotenv import load_dotenv

# --- MySQL imports (KEPT for reference) ---
# import mysql.connector
# from mysql.connector import Error as MySQLError

# --- PostgreSQL imports (ACTIVE) ---
import psycopg2
from psycopg2 import Error as PostgresError

# Load environment variables from .env
load_dotenv()


def get_db_connection():
    """
    Create and return a database connection.

    CURRENT ACTIVE DB:
    - PostgreSQL (Neon)

    To switch back to MySQL:
    - Comment Postgres section
    - Uncomment MySQL section
    """
    try:
        # =====================================================
        # MySQL CONNECTION (LOCAL / RAILWAY) - DISABLED
        # =====================================================
        """
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", 3306)),
            database=os.getenv("DB_NAME", "portfolio"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "")
        )

        if connection.is_connected():
            return connection
        """

        # =====================================================
        # POSTGRESQL CONNECTION (NEON) - ACTIVE
        # =====================================================
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", 5432)),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            sslmode=os.getenv("DB_SSLMODE", "require")  # Neon requires SSL
        )

        return connection

    except PostgresError as e:
        print(f"Error connecting to PostgreSQL (Neon): {e}")
        return None

    # except MySQLError as e:
    #     print(f"Error connecting to MySQL: {e}")
    #     return None


def close_connection(connection):
    """
    Close the database connection safely.

    Works for:
    - PostgreSQL (Neon)
    - MySQL (if re-enabled)
    """
    if connection:
        connection.close()
