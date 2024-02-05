import pandas as pd

fd = pd.read_csv("stock.csv")
print("---------------")
print(list(fd))
print("---------------")
yearlist = fd["Year"].tolist()
interest = fd["Interest_Rate"].tolist()
stockint = fd["Stock_Index_Price"].tolist()


print("Year\n",yearlist,"\n----------\n")
print("Interest Rate\n",interest,"\n----------\n")
print("Stock_Index_Price\n", stockint,"\n----------\n")