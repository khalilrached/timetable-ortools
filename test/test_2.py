from src.core.timetable_data import *
from src.core.model import *

if __name__ == '__main__':
    data =  TimetableData('./csv/template.csv')
    model = TimetableCpModel(data)
    model.solve()