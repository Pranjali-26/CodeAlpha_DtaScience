
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Unemployment_Rate": [6.1, 5.8, 8.2, 7.9, 6.8]
}

df = pd.DataFrame(data)

plt.plot(df["Year"], df["Unemployment_Rate"], marker='o')
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.title("Unemployment Rate Trend")
plt.show()
