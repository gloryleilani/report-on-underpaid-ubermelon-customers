


def determine_customer_underpayments(file_path):
  """Print a list of customers who underpaid. Argument is a file of customer data."""


  melon_cost = 1.00 #Set price per melon

  customer_orders_log = open(file_path)

  transactions = []
    
  for line in customer_orders_log:
    line = line.rstrip()
    customer_data = (line.split("|")) #Creates a tuple of customer data per customer
    #transactions.append(customer_data) #Track all customer transactions in a single list
    customer_number, customer_name, melon_quantity, amount_paid = customer_data # Unpack customer transaction data
    
    customer_name = customer_name.split(" ") #Splitting the name into first name and last name 
    melon_quantity = float(melon_quantity) #Converting to float from string
    amount_paid = float(amount_paid) #Converting to float from string

    amount_owed = melon_quantity*melon_cost #Calculating the amount of money a customer owed for his/her melons 

    if amount_owed != amount_paid:
      print(f"{customer_name[0]} paid ${amount_paid:.2f},",
           f"expected ${amount_owed:.2f}")


determine_customer_underpayments("customer-orders.txt") #Call the function



