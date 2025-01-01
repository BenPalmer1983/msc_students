import MySQLdb

class Conn():
    
    def connect():
        # Modify these as necessary
        config = {
            'user': 'dba',
            'password': '',
            'host': 'localhost',
            'database': 'msc_students'
        }

        try:
            conn = MySQLdb.connect(**config)

        except Exception as e:
            print("Error: ", e)

        return conn



