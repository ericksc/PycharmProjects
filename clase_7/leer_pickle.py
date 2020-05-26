import pickle

with open('mis_variables.pickle', 'rb') as f:
    agenda_profe = pickle.load(f)

data = '-'.join(agenda_profe[1][:2])
d = data.upper()
pass