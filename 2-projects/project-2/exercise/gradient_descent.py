import numpy as np

def gradient_descent(x, y):

    m_curr = b_curr = 0 # they start at zero just like how the 3D-function was demostrated
    learning_rate = 0.001
    iterations, n = 100, len(x)
    
    for _ in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([values ** 2 for values in (y - y_predicted)])
        dm = -(2/n) * sum(x * (y - y_predicted))
        db = -(2/n) * sum((y - y_predicted))
        m_curr = m_curr - learning_rate * dm
        b_curr = b_curr - learning_rate * db
        print(f'cost: {cost} | b_curr: {b_curr} | m_curr: {m_curr}')

if __name__ == '__main__':
# Load CSV into a NumPy array, skipping the header and excluding the first column
    data = np.genfromtxt('test_scores.csv', delimiter=',', skip_header=1)

    # Assign the second and third columns to x and y
    x = data[:, 1]  # Second column (index 1)
    y = data[:, 2]  # Third column (index 2)

    gradient_descent(x, y)
