import mysql.connector
from src.helpers.logger import Logger


class MysqlDb:
    def __init__(self, host, user, password, database):
        self.cursor = None
        self.connection = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.logger = Logger()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            self.logger.info("Connected to the database.")
        except mysql.connector.Error as error:
            self.logger.error(f"Error connecting to the database: {error}")

    def create_table_if_not_exists(self):
        table_create_query = """CREATE TABLE IF NOT EXISTS coins (
                                `id` INT AUTO_INCREMENT PRIMARY KEY, 
                                `name` VARCHAR(100) NOT NULL,
                                `symbol` VARCHAR(20) NOT NULL,
                                `rank` INT NULL,
                                `watchlist` INT NULL,
                                `logo` VARCHAR(255) DEFAULT NULL,
                                `entry_datetime` DATETIME NOT NULL
                            );"""
        self.cursor.execute(table_create_query)
        self.connection.commit()

    def insert_data(self, entries):
        insert_query = """INSERT INTO coins (`name`, `symbol`, `rank`, `watchlist`, `logo`, `entry_datetime`)
                      VALUES (%s, %s, %s, %s, %s, %s)"""
        self.cursor.executemany(insert_query, entries)
        self.connection.commit()
        self.logger.info(f"Inserted {self.cursor.rowcount} rows into the table.")

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        self.logger.info("Connection closed.")

