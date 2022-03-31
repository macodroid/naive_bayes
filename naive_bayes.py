import csv


class NaiveBayes:
    def __init__(self, csv_name):
        self.csv_name = csv_name
        self.data = []
        self.table = []
        self.__read_data()

    def __read_data(self):
        with open(self.csv_name, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                self.data.append(row)

        for row in self.data:
            table_row = {}
            for r in range(len(row)):
                table_row[header[r]] = int(row[r])
            self.table.append(table_row)

    def __probability_of_one_event(self, event) -> float:
        """
        Calculate probability of event with specific value. P(A=1) = count(A=1)/count(all).\n
        :param event: (event name, event value)
        :return: probability of event
        """
        len_table = len(self.table)
        count_event_value = 0
        for row in self.table:
            if row[event[0]] == event[1]:
                count_event_value += 1
        return count_event_value / len_table

    def __conditional_probability(self, event_a, event_b) -> float:
        """
        Calculate condition probability P(event_a|event_b)\n
        :param event_a: (name of event, event value)
        :param event_b: (name of event, event value)
        :return: probability P(event_a|event_b). Float number
        """
        count_event_b_value = 0
        count_a_b = 0
        for row in self.table:
            if row[event_b[0]] == event_b[1]:
                count_event_b_value += 1
                if row[event_a[0]] == event_a[1]:
                    count_a_b += 1
        return count_a_b / count_event_b_value

    def __joined_conditional_probability(self, variable, evidence):
        """
        Calculate probability P(variable, evidence).\n
        :param variable:
        :param evidence:
        :return:
        """
        max_value_event = max(item[variable] for item in self.table)
        probabilities = []
        for i in range(max_value_event + 1):
            probability = self.__probability_of_one_event((variable, i))
            for e in evidence:
                p = self.__conditional_probability((e, evidence[e]), (variable, i))
                if p == 0.0:
                    p = 0.000001
                probability *= p
            probabilities.append(probability)
        return probabilities

    def predict(self, variable, evidence):
        probabilities = self.__joined_conditional_probability(variable, evidence)
        alpha = 1 / sum(probabilities)
        return [alpha * p for p in probabilities]
