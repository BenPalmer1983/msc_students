import MySQLdb

class Conn():
    
    @staticmethod
    def get_password():

        # Stored in the level above
        fh = open("../password.txt")

        password = None
        for line in fh:
            password = line.strip()
            break

        fh.close()

        return password
    

    @staticmethod
    def connect():     

        # Get password
        password = Conn.get_password()

        # Set up configuration (user, password, host and database)
        config = {
            'user': 'dba',
            'password': password,
            'host': 'localhost',
            'database': 'msc_students'
        }

        # Try to connect or exit
        try:
            conn = MySQLdb.connect(**config)

        except Exception as e:
            print("Unable to connect to database.")
            print("Error: ", e)
            exit(99)

        return conn



