import pickle

if __name__ == '__main__':
    with open('model_pkl', 'rb') as f:
        model = pickle.load(f)

    print(model.predict([[5000]]))