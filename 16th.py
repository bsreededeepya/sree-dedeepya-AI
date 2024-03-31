import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid activation function
def sigmoid_derivative(x):
    return x * (1 - x)

# Define the feedforward neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.biases_input_hidden = np.random.randn(1, hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.biases_hidden_output = np.random.randn(1, output_size)

    # Forward pass
    def forward(self, X):
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.biases_input_hidden
        self.hidden_output = sigmoid(self.hidden_input)
        self.output = np.dot(self.hidden_output, self.weights_hidden_output) + self.biases_hidden_output
        return self.output

    # Backward pass
    def backward(self, X, y, learning_rate):
        # Compute gradients
        output_error = y - self.output
        output_delta = output_error * sigmoid_derivative(self.output)
        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_output)

        # Update weights and biases
        self.weights_hidden_output += learning_rate * np.dot(self.hidden_output.T, output_delta)
        self.biases_hidden_output += learning_rate * np.sum(output_delta, axis=0)
        self.weights_input_hidden += learning_rate * np.dot(X.T, hidden_delta)
        self.biases_input_hidden += learning_rate * np.sum(hidden_delta, axis=0)

    # Train the neural network
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, learning_rate)

# Example usage
# Define the dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Initialize and train the neural network
input_size = 2
hidden_size = 4
output_size = 1
nn = NeuralNetwork(input_size, hidden_size, output_size)
nn.train(X, y, epochs=10000, learning_rate=0.1)

# Test the trained neural network
print("Predictions after training:")
for x in X:
    print(x, nn.forward(x))


