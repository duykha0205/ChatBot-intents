import pickle


with open('classes.pkl', 'rb') as f:
    data = pickle.load(f)

    print(data)