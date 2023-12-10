from ortools.sat.python import cp_model
from src.core.timetable_data import TimetableData


def constraint_1(data: TimetableData, model: cp_model.CpModel, timetable):
    for t in data.get_data()['teachers_r']:
        print(f"here ........... {t}")
        for h in data.get_data()['hours_r']:
            model.AddAtMostOne(timetable[(h, c, r, t)] for r in data.get_data()[
                               'rooms_r'] for c in data.get_data()['courses_r'])
    

def constraint_2(data: TimetableData, model: cp_model.CpModel, timetable):
    for r in data.get_data()['rooms_r']:
        for h in data.get_data()['hours_r']:
            model.AddAtMostOne(timetable[(h, c, r, t)] for t in data.get_data()[
                               'teachers_r'] for c in data.get_data()['courses_r'])

def constraint_3(data: TimetableData, model: cp_model.CpModel, timetable):
    for c in data.get_data()['courses_r']:
        for h in data.get_data()['hours_r']:
            model.AddAtMostOne(timetable[(h, c, r, t)] for t in data.get_data()[
                               'teachers_r'] for r in data.get_data()['rooms_r'])


def constraint_4(data: TimetableData, model: cp_model.CpModel, timetable):
    for c in data.get_data()['courses_r']:
        model.AddAtMostOne(timetable[(h, c, r, t)] for t in data.get_data()[
                           'teachers_r'] for h in data.get_data()['hours_r'] for r in data.get_data()['rooms_r'])


def constraint_5(data: TimetableData, model: cp_model.CpModel, timetable):
    for h in data.get_data()['hours_r']:
        model.AddAtMostOne(timetable[(h, c, r, t)] for t in data.get_data()[
                           'teachers_r'] for c in data.get_data()['courses_r'] for r in data.get_data()['rooms_r'])
