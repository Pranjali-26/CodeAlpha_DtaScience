
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = {
    "Mileage": [20000, 30000, 40000, 50000, 60000],
    "Horsepower": [150, 140, 130, 120, 110],
    "Price": [20000, 18000, 16000, 14000, 12000]
}

df = pd.DataFrame(data)

X = df[["Mileage", "Horsepower"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print("Mean Squared Error:", mse)
