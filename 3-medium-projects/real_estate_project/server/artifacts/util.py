import json
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names")

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, total_sqft, bedroom, bath):
    try:
        location_index = __data_columns.index(location.lower())
    except:
        location_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bedroom

    if location_index >= 0:
        x[location_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    if __locations is None:
        return []
    return __locations

def load_saved_artifacts():
    print('loading saved artifacts... start')
    global __data_columns
    global __locations

    with open('./columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
        # print(f'Loaded locations: {__locations}')

    global __model
    with open('./apartment_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('loading artifacts... done!')

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))