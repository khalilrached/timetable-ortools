from ortools.sat.python import cp_model

class TimetablePartialSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, timetable, num_teachers, num_hours, num_rooms, num_courses, limit):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self._timetable = timetable
        self._num_hours = num_hours
        self._num_teachers = num_teachers
        self._num_rooms = num_rooms
        self._num_courses = num_courses
        self._solution_count = 0
        self._solution_limit = limit

    def on_solution_callback(self):
        self._solution_count += 1
        print(f"Solution {self._solution_count}")
        for h in range(self._num_hours):
            for t in range(self._num_teachers):
                for r in range(self._num_rooms):
                    for c in range(self._num_courses):
                        if self.Value(self._timetable[(h, c, r, t)]):
                            print(
                                f"hour: {h}, teacher: {t}, course {c}, room {r}.")
        if self._solution_count >= self._solution_limit:
            print(f"Stop search after {self._solution_limit} solutions")
            self.StopSearch()

    def solution_count(self):
        return self._solution_count
