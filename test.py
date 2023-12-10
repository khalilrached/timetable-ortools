from src.core import TimetableData,TimetableCpModel


def test_read_csv_file():
    data = TimetableData('/home/khalil/www/timetable-ortools/csv/template.csv')
    model = TimetableCpModel(data)
    model.solve()


if __name__ == '__main__':
    test_read_csv_file()
