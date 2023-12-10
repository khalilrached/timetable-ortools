from ortools.sat.python import cp_model

if __name__ == '__main__':
    num_teachers = 2
    num_rooms = 2
    num_courses = 2
    num_hours = 48

    all_teachers = range(num_teachers)
    all_rooms = range(num_rooms)
    all_courses = range(num_courses)
    all_hours = range(num_hours)

    # Creates the model.
    model = cp_model.CpModel()

    # Creates shift variables.
    # shifts[(n, d, s)]: nurse 'n' works shift 's' on day 'd'.
    shifts = {}
    for n in all_teachers:
        for d in all_rooms:
            for s in all_courses:
                shifts[(n, d, s)] = model.NewBoolVar(f"shift_n{n}_d{d}_s{s}")

    print(shifts)
    # Each shift is assigned to exactly one nurse in the schedule period.
    for d in all_rooms:
        for s in all_courses:
            print(f"test: {[shifts[(n, d, s)] for n in all_teachers]}")
