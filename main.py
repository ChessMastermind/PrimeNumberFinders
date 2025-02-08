import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Feature extraction functions
def extract_features(num):
    # Extract neutral features for the number
    features = {
        "raw": num,
        "normalized": num / 1e6,  # Normalize by a large value
        "digit_sum": sum(int(d) for d in str(num)),
        "digit_product": np.prod([int(d) for d in str(num) if d != '0']),
        "digit_count": len(str(num)),
        "first_digit": int(str(num)[0]),
        "last_digit": int(str(num)[-1]),
        "mod_10": num % 10,
        "sqrt": np.sqrt(num),
        "log": np.log(num) if num > 0 else 0,
    }
    return np.array(list(features.values()), dtype=np.float32)

# Check if a number is prime
def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

# Generate dataset
def create_dataset(limit):
    data = []
    labels = []
    for num in range(2, limit):
        features = extract_features(num)
        label = is_prime(num)
        data.append(features)
        labels.append(label)
    return np.array(data), np.array(labels)

# Neural network model
class PrimeClassifier(nn.Module):
    def __init__(self, input_size):
        super(PrimeClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 128)
        self.fc3 = nn.Linear(128, 128)
        self.fc4 = nn.Linear(128, 64)
        self.output = nn.Linear(64, 1)
        self.sigmoid = nn.Sigmoid()
        

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.relu(self.fc4(x))
        return self.sigmoid(self.output(x))

# Training the model
def train_model(model, data, labels, epochs=100, batch_size=10000, lr=0.001):
    dataset = torch.utils.data.TensorDataset(
    torch.tensor(data, dtype=torch.float32), 
    torch.tensor(labels, dtype=torch.float32).unsqueeze(1)
    )
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        for batch_data, batch_labels in dataloader:
            optimizer.zero_grad()
            predictions = model(batch_data)
            loss = criterion(predictions, batch_labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.6f}")

# Main execution
if __name__ == "__main__":
    limit = 50000  # Generate dataset up to this number
    data, labels = create_dataset(limit)

    # Normalize data (optional, but often useful for better training)
    data = (data - data.mean(axis=0)) / data.std(axis=0)

    # Initialize and train the model
    input_size = data.shape[1]
    model = PrimeClassifier(input_size)
    train_model(model, data, labels)

    # Test the model
    while True:
        test_number = int(input("> "))  # Example test
        test_features = torch.tensor([extract_features(test_number)])
        prediction = model(test_features).item()
        print(f"Number: {test_number}, Prime Probability: {prediction:.2f}")
