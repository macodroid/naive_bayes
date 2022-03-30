import csv

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
                p = 0.000001
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


pass_test_prob1 = predict('passed', {'has_time': 1, 'wants_to': 1, 'studying': 1})
pass_test_prob2 = predict('passed', {'has_time': 0, 'wants_to': 1, 'studying': 0})
has_time_test_prob = predict('has_time', {'passed': 1, 'wants_to': 0, 'studying': 0})
want_to_test_prob = predict('wants_to', {'passed': 0, 'has_time': 1, 'studying': 2})
studying_test_prob = predict('studying', {'passed': 1, 'has_time': 1, 'wants_to': 0})

print(f'1. Will student pass exam if he has time to study, he wants to study, he will study just enough?')
if pass_test_prob1[0] > pass_test_prob1[1]:
    print(f'Student will fail exam with {round(pass_test_prob1[0], 2)*100}%.\n')
else:
    print(f'Student will pass exam with {round(pass_test_prob1[1], 2)*100}%.\n')

print(f'2. Will student pass exam if he has no time to study, he wants to study, he will study just little?')
if pass_test_prob2[0] > pass_test_prob2[1]:
    print(f'Student will fail exam with {round(pass_test_prob2[0], 2)*100}%.\n')
else:
    print(f'Student will pass exam with {round(pass_test_prob2[1], 2)*100}%.\n')

print(
    f'3. Did the student has time to learn or not if he passed the exam '
    f'but he studied just a little and did not want to learn?')
if has_time_test_prob[0] > has_time_test_prob[1]:
    print(f'Student did not have time to study for exam with {round(has_time_test_prob[0], 2)*100}%.\n')
else:
    print(f'Student did have time to study for exam with {round(has_time_test_prob[1], 2)*100}%.\n')

print(
    '4. Did the student want to learn or not if he does not pass the exam '
    'but he studied a lot and had time to learn?')
if want_to_test_prob[0] > want_to_test_prob[1]:
    print(f'Student did not want to study for exam with {round(want_to_test_prob[0], 2)*100}%.\n')
else:
    print(f'Student did want to study for exam with {round(want_to_test_prob[1], 2)*100}%.\n')

print('5. How much did the student study if he passes the exam but he didnt want to learn and he had time to learn?')
if studying_test_prob[0] > studying_test_prob[1]:
    print(f'Student was studying little but for exam with {round(studying_test_prob[0], 2)*100}%.\n')
elif studying_test_prob[1] > studying_test_prob[2]:
    print(f'Student was studying just enough for exam with {round(studying_test_prob[1], 2)*100}%.\n')
else:
    print(f'Student was studying a lot for exam with {round(studying_test_prob[2], 2)*100}%.\n')
