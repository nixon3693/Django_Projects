import re
from os import path
import pandas as pd


MAX_LINE = 100
FILE_PATH = path.join(
        "D:\\", "Django_Projects", "django_projects", "syslog.txt"
    )


class ProcessSyslog:

    def __init__(self, filepath=FILE_PATH):
        self.filepath = filepath

    def process_syslog(self):
        with open(self.filepath, "r") as rd:
            messages = rd.readlines()
        month = r"(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) "
        date = r"(?P<date>[0-2][0-9]|30|31) "
        time = r"(?P<time>[0-2][0-9]:[0-5][0-9]:[0-5][0-9]\.\d{3}) "
        remaining = r"(?P<host>\w+) (?P<type>.+:) (?P<alert>.*)"
        ptn = month + date + time + remaining
        data = {
            "datetime": [], "host": [], "type": [], "alert": []
        }
        for line in messages:
            op = re.search(ptn, line)
            if op:
                data["datetime"].append(
                    op.group("month") + " " + op.group("date") +
                    " " + op.group("time")
                )
                data["host"].append(op.group("host"))
                data["type"].append(op.group("type"))
                data["alert"].append(op.group("alert"))
        df = pd.DataFrame.from_dict(data)
        return df

    @staticmethod
    def get_columns_from_df(data_frame=pd.DataFrame()):
        return data_frame.columns.to_list()

    @staticmethod
    def get_row_values_from_df(data_frame=pd.DataFrame()):
        return data_frame.values


if __name__ == "__main__":
    OBJ = ProcessSyslog()
    # print(OBJ.process_syslog())
    pd_data_frame = OBJ.process_syslog()
    # print(pd_data_frame.to_dict('records'))
    print(pd_data_frame[
              pd_data_frame["datetime"].str.lower().str.contains("jul 31")
          ].values)
    # print(OBJ.get_columns_from_df(pd_data_frame))
    # print(OBJ.get_row_values_from_df(pd_data_frame))
