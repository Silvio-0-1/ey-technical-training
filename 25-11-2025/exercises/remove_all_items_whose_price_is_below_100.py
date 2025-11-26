items_prices = {
    "apple": 150,
    "banana": 20,
    "orange": 130,
    "grapes": 60,
    "mango": 180
}

del_items = []

for i,j in items_prices.items():
    if j < 100:
        del_items.append(i)
        
for i in del_items:
        del items_prices[i]
        
print(items_prices)
