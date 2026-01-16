# 16. Sort by Sales descending.
df.sort_values("Sales", ascending = False)


# 17. Sort by ProfitMargin.
df.sort_values("ProfitMargin", ascending = True)


# 18. Sort by Region then City.
df.sort_values(["Region", "City"], ascending = False)


# 19. Sort by ShippingDays largest to smallest.
df.sort_values(["ShippingDays"], ascending = False)


# 20. Sort by CustomerName alphabetical.
df.sort_values(["CustomerName"], ascending = True)
