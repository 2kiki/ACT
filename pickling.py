import pickle

# Save
dictionary_data = [{"name": "froggie", "Height": "Six Foot", "HP": 100}, {'name': "kiki", "Height": "Syvanian Family size", "HP": 2}]

a_file = open("data.pkl", "wb")
pickle.dump(dictionary_data, a_file)

a_file.close()

# Load
a_file = open("data.pkl", "rb")
output = pickle.load(a_file)

for d in output:
    print(d)

a_file.close()
