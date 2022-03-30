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


def probability_of_one_event(event) -> float:
    """
    Calculate probability of event with specific value. P(A=1) = count(A=1)/count(all).\n
    :param event: (event name, event value)
    :return: probability of event
    """
    len_table = len(table)
    count_event_value = 0
    for row in table:
        if row[event[0]] == event[1]:
            count_event_value += 1
    return count_event_value / len_table


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


def joined_conditional_probability(variable, evidence):
    """

    :param variable:
    :param evidence:
    :return:
    """
    max_value_event = max(item[variable] for item in table)
    probabilities = []
    for i in range(max_value_event + 1):
        probability = probability_of_one_event((variable, i))
        for e in evidence:
            p = conditional_probability((e, evidence[e]), (variable, i))
            if p == 0.0:
                p = 0.001
            probability *= p
        probabilities.append(probability)
    return probabilities


def calculate_alpha(probabilities):
    _sum = sum(probabilities)
    return 1 / _sum


def predict(variable, evidence):
    probabilities = joined_conditional_probability(variable, evidence)
    alpha = calculate_alpha(probabilities)
    return [alpha * p for p in probabilities]


pro = predict('passed', {'has_time': 1, 'wants_to': 1, 'studying': 1})
pass