"""Example of a simple nurse scheduling problem."""
from ortools.sat.python import cp_model
from src.utils import TimetablePartialSolutionPrinter
from src.core.timetable_data import TimetableData
def main():
    
    data = TimetableData('./csv/template.csv')
    
    # Data.
    num_teachers = data.get_data()['teachers_l']
    num_rooms = data.get_data()['rooms_l']
    num_courses = data.get_data()['courses_l']
    num_hours = 28

    #num_teachers = ['teachers_l']
    #num_rooms = ['rooms_l']
    #num_courses = ['courses_l']
    #num_hours = 28

    all_teachers = range(num_teachers) # range(len(num_teachers))
    all_rooms = range(num_rooms)
    all_courses = range(num_courses)
    all_hours = range(num_hours)

    # Creates the model.
    model = cp_model.CpModel()

    timetable = {}

    for h in all_hours:
        for c in all_courses:
            for r in all_rooms:
                for t in all_teachers:
                    timetable[(h, c, r, t)] = model.NewBoolVar(
                        f"h{h}_c{c}_r{r}_t{t}")

    # constraint 1
    for t in all_teachers:
        for h in all_hours:
            model.AddAtMostOne(timetable[(h, c, r, t)]
                               for r in all_rooms for c in all_courses)

    # constraint 2
    for r in all_rooms:
        for h in all_hours:
            model.AddAtMostOne(timetable[(h, c, r, t)]
                               for t in all_teachers for c in all_courses)

    # constraint 3
    for c in all_courses:
        for h in all_hours:
            model.AddAtMostOne(timetable[(h, c, r, t)]
                               for t in all_teachers for r in all_rooms)
    
    # constraint: all courses must be studied at least once 
    for c in all_courses:
        model.AddAtLeastOne(timetable[(h, c, r, t)] for t in all_teachers for h in all_hours for r in all_rooms 
                            )
    # constraint: use the maximum hours
    for h in all_hours: 
        model.AddAtLeastOne(timetable[(h, c, r, t)] for c in all_courses for r in all_rooms for t in all_teachers)


    # Creates the solver and solve.
    solver = cp_model.CpSolver()
    solver.parameters.linearization_level = 0
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True

    # Display the first five solutions.
    solution_limit = 10
    solution_printer = TimetablePartialSolutionPrinter(
        timetable, num_teachers, num_hours, num_rooms, num_courses, solution_limit
    )

    solver.Solve(model, solution_printer)

    # Statistics.
    print("\nStatistics")
    print(f"  - conflicts      : {solver.NumConflicts()}")
    print(f"  - branches       : {solver.NumBranches()}")
    print(f"  - wall time      : {solver.WallTime()} s")
    print(f"  - solutions found: {solution_printer.solution_count()}")


if __name__ == "__main__":
    main()
