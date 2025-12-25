
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Advertising_Spend": [1000, 1500, 2000, 2500, 3000],
    "Sales": [12000, 15000, 18000, 21000, 25000]
}

df = pd.DataFrame(data)

X = df[["Advertising_Spend"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X, y)

future_sales = model.predict([[3500]])
print("Predicted Sales:", future_sales[0])
