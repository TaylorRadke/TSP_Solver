try:
    import mysql.connector
    import mysql.connector.errors
except ImportError:
    raise ImportError

class Database(object):
    def __init__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    def connect(self):
        """Connect to the database"""
        try:
            return mysql.connector.connect(
                host="mysql.ict.griffith.edu.au",
                user="s5094922",
                password="hib9bkip",
                database="s5094922db"
            )
        except:
            print("Failed to connect to the database")
    
    def query(self,query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            raise e

    def insert(self,query):
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as e:
            raise e

    def save(self):
        self.connection.commit()
    
    def close(self):
        self.connection.close()
