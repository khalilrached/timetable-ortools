from ortools.sat.python import cp_model
from src.core.timetable_data import TimetableData
from src.core import TimetableCpModel


def constraint_1(data: TimetableData, timetable):
    for t in data.get_data()['teachers_r']:
        print(f"here ........... {t}")
        for h in data.get_data()['hours_r']:
            TimetableCpModel.model.AddAtMostOne(timetable[(h, c, r, t)] for r in data.get_data()[
                               'rooms_r'] for c in data.get_data()['courses_r'])

def constraint_2(data: TimetableData, timetable):
    for r in data.get_data()['rooms_r']:
        for h in data.get_data()['hours_r']:
            TimetableCpModel.model.AddAtMostOne(timetable[(h, c, r, t)] for t in data.get_data()[
                               'teachers_r'] for c in data.get_data()['courses_r'])

def constraint_3(data: TimetableData, timetable):
    for c in data.get_data()['courses_r']:
        for h in data.get_data()['hours_r']:
            TimetableCpModel.model.AddAtMostOne(timetable[(h, c, r, t)] for t in data.get_data()[
                               'teachers_r'] for r in data.get_data()['rooms_r'])


def constraint_4(data: TimetableData, timetable):
    for c in data.get_data()['courses_r']:
        TimetableCpModel.model.AddAtMostOne(timetable[(h, c, r, t)] for t in data.get_data()[
                           'teachers_r'] for h in data.get_data()['hours_r'] for r in data.get_data()['rooms_r'])


def constraint_5(data: TimetableData, timetable):
    for h in data.get_data()['hours_r']:
        TimetableCpModel.model.AddAtMostOne(timetable[(h, c, r, t)] for t in data.get_data()[
                           'teachers_r'] for c in data.get_data()['courses_r'] for r in data.get_data()['rooms_r'])
