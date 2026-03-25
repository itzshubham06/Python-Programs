import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("Columns in file:", df.columns)

month = [col for col in df.columns if "month" in col][0]
profit = [col for col in df.columns if "profit" in col][0]

plt.figure()
plt.plot(df[month], df[profit], marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.show()

products = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]

plt.figure()
for p in products:
    if p in df.columns:
        plt.plot(df[month], df[p], label=p)

plt.legend()
plt.show()

plt.figure()
if "facecream" in df.columns and "facewash" in df.columns:
    plt.plot(df[month], df["facecream"], label="Face Cream")
    plt.plot(df[month], df["facewash"], label="Face Wash")

plt.legend()
plt.show()

total_sales = []
labels = []

for p in products:
    if p in df.columns:
        total_sales.append(df[p].sum())
        labels.append(p)

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.show()

plt.figure()
explode = [0.1] + [0]*(len(labels)-1)
plt.pie(total_sales, labels=labels, autopct='%1.1f%%', explode=explode, shadow=True)
plt.show()

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)
plt.show()