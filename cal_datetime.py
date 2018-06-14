import time
import datetime
import math


class DiffDatetime:
    def __init__(self, datetime1, datetime2):
        self.datetime1 = datetime1
        self.datetime2 = datetime2
        self.diff_seconds = (datetime1 - datetime2).seconds
        self.d_days = (datetime1 - datetime2).days
        self.diff_datetime()
    

    def diff_datetime(self):
        self.d_hours = math.floor(self.diff_seconds/(3600))

        leave1 = self.diff_seconds%(3600)
        self.d_minutes = math.floor(leave1/(60))

        leave2 = leave1%(60)
        self.d_seconds = round(leave2)


    def to_str(self):
        return '{0}天{1}小時{2}分鐘{3}秒 前'.format(
            str(self.d_days), str(self.d_hours), str(self.d_minutes), str(self.d_seconds))
        

    def to_str_simplify(self):
        output = ""

        if self.d_days!=0:
            output = str(self.d_days)+"天"

        elif self.d_hours!=0:
            output = str(self.d_hours)+"小時"

        elif self.d_minutes!=0:
            output = str(self.d_minutes)+"分鐘"
            
        elif self.d_seconds!=0:
            output = str(self.d_seconds)+"秒"

        return output + ' 前'

