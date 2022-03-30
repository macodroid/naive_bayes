import pandas as pd
from pgmpy.models import NaiveBayes
from pgmpy.inference import VariableElimination

# Lod dataset
exams = pd.read_csv('exams.csv')

model = NaiveBayes()
# add all independent evidence features
model.add_edges_from([('passed', 'has_time'), ('passed', 'wants_to'), ('passed', 'studying')])

# train the model to classify the 'passed' variable
# for other variables you might want to change the model
model.fit(exams, 'passed')

# predict most probable outcome based on evidence
inference = VariableElimination(model)
prediction = inference.map_query(['passed'], evidence={'has_time': 1, 'wants_to': 1, 'studying': 1})
print("Prediction (passed):", prediction)

# look at the conditional probabilities. Think about last week exercise.
# How you can calculate the probabilities you want?
for cpd in model.get_cpds():
    print(cpd)