import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("covid_data.csv")
df.read()
df.info()
df.describe()
df.isnull().sum()
df.dropna(inplce = True)
df.fillna(0, inplace = True)

df['date'] = pd.to_datetime(df['date'])
df.sort_values('date', inplace = True)
df.groupby('date')['cases'].sum().plot()
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel("Date")
plt.ylabel("Cases")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

df.groupby('date')['recovered','deaths'].sum().plot()
plt.title("Recoveries vs Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Number of people")
plt.legend(["Recovered", "Deaths"])
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()