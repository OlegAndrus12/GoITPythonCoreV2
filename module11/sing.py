
from datetime import datetime




class Date:
    MIN_YEAR = 1900

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    # regular method
    def get_month(self):
        return self.month

    #classmethod
    @classmethod
    def parse_eu_format(cls, date_as_string):
        day, month, year = [int(i) for i in date_as_string.split("-")]
        return cls(day, month, year)
    
    #static method
    @staticmethod
    def is_valid_date():
        print(Date.MIN_YEAR)

d = Date(12,31, 2)
d.is_valid_date()
Date.is_valid_date()