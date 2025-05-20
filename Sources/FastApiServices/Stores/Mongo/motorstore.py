
import motor.motor_asyncio
from Utils.ConfigParserUtil import ConfigParserUtil


class MotorConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_connection()
        return cls._instance

    def _init_connection(self):
        self.config = ConfigParserUtil()
        host = self.config.getValue("MongoDB", "Host")
        port = self.config.getValue("MongoDB", "Port")
        username = self.config.getValue("MongoDB", "Username")
        password = self.config.getValue("MongoDB", "Password")
        server_timeout = int(self.config.getValue("MongoDB", "ServerTimeOut"))
        db_name = self.config.getValue("MongoDB", "DatabaseName")
        use_ssl = self.config.getValue("MongoDB", "UseSSL").lower() == "true"
        auth_source = "admin"

        mongo_uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource={auth_source}"

        if use_ssl:
            ssl_ca_file = self.config.getValue("MongoDB", "SSLCAFile")
            self.client = motor.motor_asyncio.AsyncIOMotorClient(
                mongo_uri,
                tls=True,
                tlsCAFile=ssl_ca_file,
                serverSelectionTimeoutMS=server_timeout
            )
        else:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(
                mongo_uri,
                serverSelectionTimeoutMS=server_timeout
            )

        self._db = self.client[db_name]
        self._RegressionConfigcollection = self._db["RegressionConfig_TBD"]