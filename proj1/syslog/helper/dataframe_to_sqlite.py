import sqlite3
import pandas as pd
from .process_syslog import ProcessSyslog


class DataframeToSqlite:

    def __init__(self, data=pd.DataFrame()):
        self.data = data
        self.con = sqlite3.connect("../../db.sqlite3")

    def dataframe_to_sqlite_db(self):
        self.data.to_sql(
            "syslog_syslogmodel",
            con=self.con,
            if_exists="replace",
            index=True
        )
        self.con.close()


if __name__ == "__main__":
    DF = ProcessSyslog().process_syslog()
    DataframeToSqlite(DF).dataframe_to_sqlite_db()
