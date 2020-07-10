

#BREAK DOWN PROBLEM
#Define function
#Open file of customer data
#Iterate through lines, grab the data per line
#Tokenize each line, unpack or assign to vars per position
#Data in file: Customer number, customer name, Quantity of melons, Total pymt 
#Determine amount customer should have paid, compare with amount paid in file.
#If paid less than expected, report the custome and amount underpaid.
#Call function


#PSEUDOCODE
#customer_orders_log = open("customer-orders.txt")
#for line in customer-orders.txt:
# line = line.rstrip()
# customer_data = line.split("|") (make a tuple)
# customer_number, customer_name, melon_quantity, customer_paid = customer_data
# amount_owed = melon_quantity*melon_cost

#for each customer in customer_data:
#if amount_owed != 
#print(f"{customer1_name[0]} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )


def determine_customer_underpayments(file_path):
  """This function takes in a file of customer orders and prints a list of customers who underpaid."""


  melon_cost = 1.00 #Set price per melon

  customer_orders_log = open(file_path)

  transactions = []
    
  for line in customer_orders_log:
    line = line.rstrip()
    customer_data = (line.split("|")) #Creates a tuple of customer data per customer
    transactions.append(customer_data) #Track all customer transactions in a single list
    customer_number, customer_name, melon_quantity, amount_paid = customer_data # Unpack customer transaction data
    
    customer_name = customer_name.split(" ") #Splitting the name into first name and last name 
    melon_quantity = float(melon_quantity) #Converting to float from string
    amount_paid = float(amount_paid) #Converting to float from string

    amount_owed = melon_quantity*melon_cost #Calculating the amount of money a customer owed for his/her melons 

    if amount_owed != amount_paid:
      print(f"{customer_name[0]} paid ${amount_paid:.2f},",
           f"expected ${amount_owed:.2f}")


determine_customer_underpayments("customer-orders.txt") #Call the function



#Original code in exercise to replace:

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
