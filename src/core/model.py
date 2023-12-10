from ortools.sat.python import cp_model
from src.core.timetable_data import *
from src.core.constraints import *
from src.utils.printer import TimetablePartialSolutionPrinter
from typing import Callable


class TimetableCpModel:
    model: cp_model.CpModel = cp_model.CpModel()
    __timetable = {}
    __constraints = [constraint_1, constraint_2,
                     constraint_3, constraint_4, constraint_5]
    __solver = cp_model.CpSolver()

    def __init__(self, data: TimetableData) -> None:
        self.__data = data
        self.__timetable = self.__data.create_timetable(self.model)
        self.__apply_constraints__()
        self.__solver.parameters.linearization_level = 0
        self.__solver.parameters.enumerate_all_solutions = True
        

    def __apply_constraints__(self):
        for constraints_function in self.__constraints:
            constraints_function(self.__data, self.__timetable)

    def solve(self):
        print(self.__data.get_data())
        solution_limit = 10
        solution_printer = TimetablePartialSolutionPrinter(
            self.__timetable,
            self.__data.get_data()['teachers_l'],
            self.__data.get_data()['hours_l'],
            self.__data.get_data()['rooms_l'],
            self.__data.get_data()['courses_l'],
            solution_limit
        )
        self.__solver.Solve(self.model, solution_printer)

        # Statistics.
        print("\nStatistics")
        print(f"  - conflicts      : {self.__solver.NumConflicts()}")
        print(f"  - branches       : {self.__solver.NumBranches()}")
        print(f"  - wall time      : {self.__solver.WallTime()} s")
        print(f"  - solutions found: {solution_printer.solution_count()}")
