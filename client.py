import os
from pysqlcipher3 import dbapi2 as sqlite3

class decryption:
    def __init__(self, key, output, database):
        self.key = key
        self.output = output
        self.database = database

    def decrypt_database(self):
        if os.path.exists(self.output):
            os.remove(self.output)
        with SQLite(self.database) as cursor:
            cursor.execute(f"""PRAGMA key = '{self.key}'""")
            cursor.execute("""PRAGMA cipher_compatibility = 3""")
            cursor.execute(f"""ATTACH DATABASE '{self.output}' AS decrypted KEY""")
            cursor.execute("""SELECT sqlcipher_export('decrypted')""")
            cursor.execute("""DETACH DATABASE decrypted""")
        
class SQLite:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        self.conn.row_factory  = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()
