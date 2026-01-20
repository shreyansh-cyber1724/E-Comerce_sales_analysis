import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Amazon Sale Report.csv")

#inspect
print(df.head())
print(df.shape)
print(df.info())

#inspecting missing valye
missing_value = df.isnull().sum()
print(missing_value/df.shape[0] *100)

print(df.duplicated().sum()) #0 duplicated data represent no duplicasy


print(df["Amount"].describe())

df=df.dropna(subset="Amount")
df=df.dropna(subset="currency")
df=df.dropna(subset="ship-city")
df=df.dropna(subset="Courier Status")

df=df.drop(columns=["Unnamed: 22","fulfilled-by"])


print(df.isnull().sum()/df.shape[0] *100)

df["Date"]=df["Date"].astype(str).str.strip()
df["Date"]=pd.to_datetime(df["Date"], errors="coerce")

df["month"]=df["Date"].dt.month
df["Courier Status"] = (
    df["Courier Status"]
    .astype(str)
    .str.strip()
    .str.title()
)
g1 =(
    df[df["Courier Status"].isin(["Shipped","Unshipped"])]
    .groupby("month")["Courier Status"]
    .value_counts()
    .unstack(fill_value=0)
)


g1["Unshipped_pct"] = (
    g1["Unshipped"] / (g1["Shipped"] + g1["Unshipped"]) * 100
)# in month 6 the logistic performance is worts
#and logistic is not getting batter


g2 = df.groupby("month")["B2B"].value_counts().unstack(fill_value=0)

#print(df["currency"].value_counts())


g3 = (df[df["currency"].isin(["INR"])]
    .groupby("month",as_index=True)["Amount"]
    .sum()
    .sort_index()
)#from month 4 got very much growth in revenue amount
g3 = g3.sort_index()
g4 = df.groupby("month")["Amount"].mean()
#all the month of observation got no profit per order growth
print(g1)
print(g2)
print(g3)
print(g4)
g3_million = g3 / 1_000_000

plt.figure(figsize=(10,6))
plt.plot(g3_million.index, g3_million.values, marker="o")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue (Million INR)", fontsize=12)
plt.title("Monthly Revenue Trend", fontsize=14)

# with the monthly revenue the trend show how the revenue growth peak in 2nd month and then it slight down
plt.figure(figsize=(8,6))
plt.plot(g4.index,g4.values)
plt.xlabel("month")
plt.ylabel("Revenue per order")
plt.title("Monthly revenue per order")

plt.show()