from mysql.connector import connection

auth = connection.MySQLConnection(
    user = 'sajid',
    password = 'P@ssw0rd',
    host = 'host.docker.internal',                        # Connect with docker container - host.docker.internal
    database = 'pySQL_TODO'
)

