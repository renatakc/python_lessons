import ConfigParser

class ConnectionDetails:
    server=''
    user=''
    password=''
    database=''

    def __init__(self):
        Config = ConfigParser.ConfigParser()
        Config.read("conn.ini")
        self.server = Config.get("connections", "server")
        self.user = Config.get("connections", "user")
        self.password = Config.get("connections", "password")
        self.database = Config.get("connections", "database")
