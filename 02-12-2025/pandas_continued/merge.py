merged = df.merge(customers, on = "CustomerType", how = "left")
print(merged)