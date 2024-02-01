import pandas as pd

fd = pd.read_csv("stock.csv")
yearlist = fd["Year"].tolist()
interest = fd["Interest_Rate"].tolist()
stockint = fd["Stock_Index_Price"].tolist()


print("Year\n",yearlist)
print("Interest Rate\n",interest)
print("Stock_Index_Price\n", stockint)