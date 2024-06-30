# data/db_utils.py
import sys
import mysql.connector
sys.path.insert(0, 'C:\\Users\\Lenovo\\Desktop\\youtube_data_analysis\\src')


from src.db_operations import create_connection, execute_query, fetch_data
from data.sql_queries import INSERT_QUERY, SELECT_ALL_QUERY

def create_connection(host_name, user_name, user_password, db_name):
    try:
        connection = mysql.connector.connect(
            host='DESKTOP-B2E6EGI',
            user='root',
            passwd='1234',
            database='youtube_data_db'
        )
        print("Connection to MySQL DB successful")
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL DB: {e}")
        return None

def execute_query(connection, query, data=None):
    try:
        cursor = connection.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")

def fetch_data(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print("Data fetched successfully")
        return result
    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
        return None
