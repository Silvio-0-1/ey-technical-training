# Read a CSV file orders.csv containing columns: item, quantity, price.
# Generate an invoice file that lists all items and the final total.
total = 0

with open("invoice.txt", "w") as h:
    h.write("Invoice: \n\n")
    with open("orders.csv", "r") as f:
        content = f.read().split("\n")
        h.write("Item\tQuantity\tPrice\n")
        for i in content:
            order_details = i.split(",")
            h.write(f"{order_details[0]}\t{order_details[1]}\t{order_details[2]}\n")
            total = total + (int(order_details[1]) * float(order_details[2]))
        h.write(f"Total: {total}")
print("Report Generated!")
