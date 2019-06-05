from connection_db_oop import *

# Let's imagine we're making calls to db

# northwind_db = Northwind()
#
# northwind_db.find_client('name')
# # >>> all client details
#
# northwind_db.print_all_products('parameters')
#
# etc...

northwind_db = ConnMsSql()

# northwind_db.query("SELECT TOP 10 * FROM Customers")
#
# for x in northwind_db.cursor:
#     print(x)

#northwind_db.print_all_products()

#northwind_db.avg_unit_price()

northwind_db.company_name("Rattlesnake")
print("\n")
northwind_db.cust_country("UK")