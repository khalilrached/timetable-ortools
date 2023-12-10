from ortools.sat.python import cp_model
from src.utils.process_data import process_data


class TimetableData:
    headers = ['teachers', 'courses', 'rooms', 'hours']
    __data_headers = ['teachers', 'courses', 'rooms']
    __hours_per_week = 4
    __data_map = {}

    def __init__(self, filepath) -> None:
        raw_data = open(filepath, 'r').read()
        self.__data_map = process_data(raw_data, self.__data_headers)
        self.__data_map['hours'] = [
            hour for hour in range(self.__hours_per_week)]

    def create_timetable(self, model: cp_model.CpModel):
        __temp_timetable = {}
        for h, _ in enumerate(self.__data_map['hours']):
            for c, _ in enumerate(self.__data_map['courses']):
                for r, _ in enumerate(self.__data_map['rooms']):
                    for t, _ in enumerate(self.__data_map['teachers']):
                        __temp_timetable[(h, c, r, t)] = model.NewBoolVar(
                            f"h{h}_c{c}_r{r}_t{t}")
        return __temp_timetable

    def get_data(self):
        """
            return dict of type 
            {
                hours_l: int
                courses_l: int
                teachers_l: int
                rooms_l: int
                hours_r: int
                courses_r: int
                teachers_r: int
                rooms_r: int
            }
        """
        return {
            'hours_l': len(self.__data_map['hours']),
            'courses_l': len(self.__data_map['courses']),
            'teachers_l': len(self.__data_map['teachers']),
            'rooms_l': len(self.__data_map['rooms']),
            'hours_r': range(len(self.__data_map['hours'])),
            'courses_r': range(len(self.__data_map['courses'])),
            'teachers_r': range(len(self.__data_map['teachers'])),
            'rooms_r': range(len(self.__data_map['rooms']))
        }
