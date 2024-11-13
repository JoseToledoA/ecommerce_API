from typing import Optional, List, Dict, Union, Any, Tuple
import psycopg2
from psycopg2 import pool


class POSTGRESSQL_DB:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(POSTGRESSQL_DB, cls).__new__(cls)
            cls._instance.pool = psycopg2.pool.SimpleConnectionPool(
                minconn=1,
                maxconn=10,
                host="localhost",
                port=5432,
                database="ecommerce_db",
                user="postgres",
                password="33pelu07",
            )
        return cls._instance

    def execute_query(
        self, query: str, params: Optional[Tuple] = None, return_id: bool = False
    ) -> None:

        connection = self.pool.getconn()
        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            id_of_new_row = None
            if return_id:
                id_of_new_row = cursor.fetchone()[0]
            connection.commit()
            return id_of_new_row

        except Exception as e:
            print(f"Error executing query: {e}")
            connection.rollback()
        finally:
            cursor.close()
            self.pool.putconn(connection)

    def fetch_all_data(
        self, query: str, params: Optional[Tuple] = None
    ) -> Optional[List[Tuple]]:
        connection = self.pool.getconn()

        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error fetching results: {e}")
            return None
        finally:
            cursor.close()
            self.pool.putconn(connection)

    def fetch_one_data(
        self, query: str, params: Optional[Tuple] = None
    ) -> Optional[List[Tuple]]:

        connection = self.pool.getconn()

        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error fetching results: {e}")
            return None
        finally:
            cursor.close()
            self.pool.putconn(connection)

    def close_connection_pool(self) -> None:

        self.pool.closeall()
