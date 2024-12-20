# -*- coding: utf-8 -*-
"""Level-1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E-UYXWcQpwuBqdBM9RrR7jB5Nt4MXBCd
"""



import torch
import torchvision
import torchvision.transforms as transforms
from efficientnet_pytorch import EfficientNet
import torch.nn as nn
from torch.optim import Adam
from sklearn.metrics import accuracy_score
from torch.utils.data import DataLoader

# Fine-tuned EfficientNetB0 Model (with final classifier for MNIST)
class FineTunedEfficientNetB0Model(nn.Module):
    def __init__(self):
        super(FineTunedEfficientNetB0Model, self).__init__()
        self.model = EfficientNet.from_pretrained('efficientnet-b0')
        # Modify the final fully connected layer to match the MNIST dataset (10 classes)
        self.model._fc = nn.Linear(self.model._fc.in_features, 10)

    def forward(self, x):
        return self.model(x)

# Load MNIST dataset
def load_data(transform):
    train_dataset = torchvision.datasets.MNIST(root="./data/mnist", train=True, download=True, transform=transform)
    test_dataset = torchvision.datasets.MNIST(root="./data/mnist", train=False, download=True, transform=transform)
    return train_dataset, test_dataset

# Training the model
def train_model(train_loader, model, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    for data, target in train_loader:
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        # Calculate accuracy
        _, predicted = torch.max(output, 1)
        total += target.size(0)
        correct += (predicted == target).sum().item()

    epoch_loss = running_loss / len(train_loader)
    epoch_accuracy = 100 * correct / total
    return epoch_loss, epoch_accuracy

# Testing the model
def test_model(test_loader, model, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            _, predicted = torch.max(output, 1)
            total += target.size(0)
            correct += (predicted == target).sum().item()

    test_accuracy = 100 * correct / total
    return test_accuracy

# Centralized training process
def centralized_learning():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    transform = transforms.Compose(
        [transforms.Grayscale(num_output_channels=1),  # Use single channel for MNIST
         transforms.Resize((128, 128)),  # Resize to smaller size
         transforms.Lambda(lambda x: x.convert("RGB")),  # Convert grayscale to RGB (3 channels)
         transforms.ToTensor(),
         transforms.Normalize((0.5,), (0.5,))])  # Normalize for 3 channels

    train_dataset, test_dataset = load_data(transform)

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)

    # Fine-tuned EfficientNet model
    model = FineTunedEfficientNetB0Model().to(device)

    # Define loss function and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = Adam(model.parameters(), lr=0.0001)

    # Training loop
    num_epochs = 10
    for epoch in range(num_epochs):
        train_loss, train_accuracy = train_model(train_loader, model, criterion, optimizer, device)
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {train_loss:.4f}, Accuracy: {train_accuracy:.2f}%")

    # Test the model
    test_accuracy = test_model(test_loader, model, device)
    print(f"Test Accuracy: {test_accuracy:.2f}%")

    # Save the fine-tuned model
    torch.save(model.state_dict(), 'fine_tuned_efficientnet_b0_mnist.pth')
    print("Training completed and model saved.")

if __name__ == '__main__':
    centralized_learning()

