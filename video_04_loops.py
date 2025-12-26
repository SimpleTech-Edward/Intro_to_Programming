"""
WHILE LOOPS - condition controlled loops

FOR LOOPS - count controlled loops

LISTS AND TUPLES
Using diagram display the nature of how lists and tuples are created.
"""

keep_going = "y"
commission_rate = 0.1
total_commission = 0

while keep_going.lower() == "y":
    sales_amount = int(input("Enter amount of sales: $"))
    commission = sales_amount * commission_rate
    total_commission += commission
    keep_going = input("Do you have more sales to enter? y/n: ")


for i in [1,2,3,4,5]:
    print(i)


number_list = [1,2,3,4,5]
name_list = ["John", "Jane", "Steve", "Sarah"]

for number in number_list:
    print(number)

for name in name_list:
    print(name)