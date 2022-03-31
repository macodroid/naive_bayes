from naive_bayes import NaiveBayes

csv_name = 'exams.csv'

nb = NaiveBayes(csv_name)

pass_test_prob1 = nb.predict('passed', {'has_time': 1, 'wants_to': 1, 'studying': 1})
pass_test_prob2 = nb.predict('passed', {'has_time': 0, 'wants_to': 1, 'studying': 0})
has_time_test_prob = nb.predict('has_time', {'passed': 1, 'wants_to': 0, 'studying': 0})
want_to_test_prob = nb.predict('wants_to', {'passed': 0, 'has_time': 1, 'studying': 2})
studying_test_prob = nb.predict('studying', {'passed': 1, 'has_time': 1, 'wants_to': 0})

print(f'1. Will student pass exam if he has time to study, he wants to study, he will study just enough?')
if pass_test_prob1[0] > pass_test_prob1[1]:
    print(f'Student will fail exam with {round(pass_test_prob1[0], 2) * 100}%.\n')
else:
    print(f'Student will pass exam with {round(pass_test_prob1[1], 2) * 100}%.\n')

print(f'2. Will student pass exam if he has no time to study, he wants to study, he will study just little?')
if pass_test_prob2[0] > pass_test_prob2[1]:
    print(f'Student will fail exam with {round(pass_test_prob2[0], 2) * 100}%.\n')
else:
    print(f'Student will pass exam with {round(pass_test_prob2[1], 2) * 100}%.\n')

print(
    f'3. Did the student has time to learn or not if he passed the exam '
    f'but he studied just a little and did not want to learn?')
if has_time_test_prob[0] > has_time_test_prob[1]:
    print(f'Student did not have time to study for exam with {round(has_time_test_prob[0], 2) * 100}%.\n')
else:
    print(f'Student did have time to study for exam with {round(has_time_test_prob[1], 2) * 100}%.\n')

print(
    '4. Did the student want to learn or not if he does not pass the exam '
    'but he studied a lot and had time to learn?')
if want_to_test_prob[0] > want_to_test_prob[1]:
    print(f'Student did not want to study for exam with {round(want_to_test_prob[0], 2) * 100}%.\n')
else:
    print(f'Student did want to study for exam with {round(want_to_test_prob[1], 2) * 100}%.\n')

print('5. How much did the student study if he passes the exam but he didnt want to learn and he had time to learn?')
if studying_test_prob[0] > studying_test_prob[1] and studying_test_prob[0] > studying_test_prob[2]:
    print(f'Student was studying little but for exam with {round(studying_test_prob[0], 2) * 100}%.\n')
elif studying_test_prob[1] > studying_test_prob[2]:
    print(f'Student was studying just enough for exam with {round(studying_test_prob[1], 2) * 100}%.\n')
else:
    print(f'Student was studying a lot for exam with {round(studying_test_prob[2], 2) * 100}%.\n')
