import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

iris = load_iris()

X = iris.data
y = to_categorical(iris.target)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = Sequential()

model.add(Dense(10, input_dim=4, activation="tanh"))
model.add(Dense(8, activation="relu"))
model.add(Dense(3, activation="softmax"))

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

history = model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=10,
    validation_split=0.2,
    verbose=1
)

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print("Accuracy:", accuracy)

prediction = model.predict(X_test[:5])
print("Prediction")
print(np.argmax(prediction, axis=1))

model.summary()

plt.plot(history.history["loss"])
plt.title("Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()

plt.plot(history.history["accuracy"])
plt.title("Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.show()