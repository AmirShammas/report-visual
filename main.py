import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(
    description="Pass the report")

parser.add_argument("-r", "--report", type=int,
                    help="Display the Count/Product and Order/Month and Total Price/Month diagrams")

args = parser.parse_args()

df = pd.read_csv("data.csv")

if (args.report == 1):
    grouped_data = df.groupby('Product')['Count'].sum()
    descending_grouped_data = grouped_data.sort_values(ascending=False)
    descending_grouped_data[:5].plot(kind='bar', width=0.1)
    plt.xlabel('Product')
    plt.ylabel('Count')
    plt.title('5 best seller Products during 1 year')
    plt.show()
elif (args.report == 2):
    grouped_data = df.groupby('Month')['ID'].count()
    grouped_data.plot(kind='line')
    plt.xlabel('Month')
    plt.xticks(range(1, 13))
    plt.ylabel('Orders Number')
    plt.title('Orders Number/Month during 1 year')
    plt.show()
elif (args.report == 3):
    grouped_data = df.groupby('Month')['Total Price'].sum()
    grouped_data.plot(kind='line', c="red")
    plt.xlabel('Month')
    plt.xticks(range(1, 13))
    plt.ylabel('Total Price')
    plt.title('Total Price/Month during 1 year')
    plt.show()
else:
    print("Please pass the correct -r flag (1 or 2 or 3)!")
