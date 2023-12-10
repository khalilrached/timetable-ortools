"""Example of a simple nurse scheduling problem."""
from ortools.sat.python import cp_model
from src.utils import TimetablePartialSolutionPrinter

def main():
    # Data.
    num_teachers = 5
    num_rooms = 2
    num_courses = 7
    num_hours = 4

    all_teachers = range(num_teachers)
    all_rooms = range(num_rooms)
    all_courses = range(num_courses)
    all_hours = range(num_hours)

    # Creates the model.
    model = cp_model.CpModel()

    # Creates shift variables.
    # shifts[(n, d, s)]: nurse 'n' works shift 's' on day 'd'.
    timetable = {}

    for h in all_hours:
        for c in all_courses:
            for r in all_rooms:
                for t in all_teachers:
                    timetable[(h, c, r, t)] = model.NewBoolVar(
                        f"h{h}_c{c}_r{r}_t{t}")

    # Each shift is assigned to exactly one nurse in the schedule period.
    for t in all_teachers:
        for h in all_hours:
            model.AddAtMostOne(timetable[(h, c, r, t)]
                               for r in all_rooms for c in all_courses)

    # Each shift is assigned to exactly one nurse in the schedule period.
    for r in all_rooms:
        for h in all_hours:
            model.AddAtMostOne(timetable[(h, c, r, t)]
                               for t in all_teachers for c in all_courses)

    for c in all_courses:
        for h in all_hours:
            model.AddAtMostOne(timetable[(h, c, r, t)]
                               for t in all_teachers for r in all_rooms)
    
    for c in all_courses:
        model.AddAtLeastOne(timetable[(h, c, r, t)] for t in all_teachers for h in all_hours for r in all_rooms 
                            )

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
