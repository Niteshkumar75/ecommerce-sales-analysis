import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Customer": ["Ali", "John", "Sara", "Ali", "Mike", "Anna"],
    "City": ["Berlin", "berlin", "Munich", "Berlin", "Hamburg", "Munich"],
    "Purchase": [100, 200, 150, 100, 300, 250],
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-01", "2024-01-05", "2024-01-06"]
}

# DEBUG CHECK
for key in data:
    print(key, len(data[key]))

# CREATE DATAFRAME
df = pd.DataFrame(data)

print(df)

df["Purchase"] = df["Purchase"].fillna(df["Purchase"].mean())
df = df.dropna(subset=["Customer"])
df["City"] = df["City"].str.upper()
df=df.drop_duplicates()
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df=df.dropna(subset=["Date"])

print("Total Revenue:", df["Purchase"].sum())

revenue_by_city = df.groupby("City")["Purchase"].sum()
print(revenue_by_city)


revenue_by_city.plot(kind="bar")
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.show()

sales_by_date = df.groupby("Date")["Purchase"].sum()
sales_by_date.plot()
plt.title("Sales Over Time")
plt.show()