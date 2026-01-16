# 15. Use method chaining to:
# remove rows with Quantity < 2
# filter Category = Apparel
# compute TotalValue = Quantity * UnitPrice
# sort TotalValue descending
# reset index
# Return the final DataFrame.


import pandas as pd
df = pd.read_csv("customer.csv")

final_df = (
    df[df["Quantity"] >= 2]                      # Remove rows where Quantity < 2
      .query("Category == 'Apparel'")            # Filter Category = Apparel
      .assign(TotalValue=lambda x: x["Quantity"] * x["UnitPrice"])  # Compute TotalValue
      .sort_values("TotalValue", ascending=False) # Sort by TotalValue descending
      .reset_index(drop=True)                    # Reset index
)

print(final_df)
