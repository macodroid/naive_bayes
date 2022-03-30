import csv
import string

csv_name = 'exams.csv'
data = []
table = []
with open(csv_name, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        data.append(row)

for row in data:
    table_row = {}
    for r in range(len(row)):
        table_row[header[r]] = int(row[r])
    table.append(table_row)


def conditional_probability(event_a, event_b) -> float:
    """
    Calculate condition probability P(event_a|event_b)\n
    :param event_a: (name of event, event value)
    :param event_b: (name of event, event value)
    :return: probability P(event_a|event_b). Float number
    """
    count_event_b_value = 0
    count_a_b = 0
    for row in table:
        if row[event_b[0]] == event_b[1]:
            count_event_b_value += 1
            if row[event_a[0]] == event_a[1]:
                count_a_b += 1
    return count_a_b / count_event_b_value


def joined_conditional_probability():
    pass


f = conditional_probability(('has_time', 0), ('passed', 1))
pass
