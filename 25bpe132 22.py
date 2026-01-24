def calculate_net_sales(gross_sales):
    discount = gross_sales * 0.10
    net_sales = gross_sales - discount
    return discount, net_sales

gross = float(input("Enter Gross Sales: "))

discount, net = calculate_net_sales(gross)

print("Discount (10%):", discount)
print("Net Sales:", net)
