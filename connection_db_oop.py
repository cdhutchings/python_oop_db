import pyodbc

# Our variables consists of all details required to initiate a connection


class ConnMsSql:

    # When we initialise = Make connection

    def __init__(self, server="localhost,1433", database="Northwind", username="SA", password="Passw0rd2018"):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.docker_con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL '
                                'Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        self.cursor = self.docker_con.cursor()

    # clients having access to query anything is quite dangerous, so it would be good to encapsulate it with __

    def __query(self, sql_query):

        return self.cursor.execute(sql_query)
        # ERROR HANDLE

    def print_all_products(self):

        query = self.__query("SELECT * FROM Products")

        for row in query:
            print(row)

    def avg_unit_price(self):

        query = self.__query("SELECT AVG(UnitPrice) FROM Products")

        for x in query:
            result = round(float(''.join(c for c in str(x) if c.isdigit() or c == ".")), 2)
            print("£"+str(result))


# Search and filter products by name
    def product_name(self, name=""):

        if name == "":
            query = self.__query("SELECT * FROM Products "
                                 "ORDER BY ProductName")
        else:
            query = self.__query(f"SELECT * FROM Products "
                                 f"WHERE ProductName LIKE '%{name}%'"
                                 f"ORDER BY ProductName")

        for x in query:
            print(x)

# Filter customers by company names

    def company_name(self, name=""):

        if name == "":
            query = self.__query("SELECT * FROM Customers "
                                "ORDER BY CompanyName")
        else:
            query = self.__query(f"SELECT * FROM Customers "
                                 f"WHERE CompanyName LIKE '%{name}%'"
                                 f"ORDER BY CompanyName")

        for x in query:
            print(x)

# Filter customers by country

    def cust_country(self, name=""):

        if name == "":
            query = self.__query("SELECT * FROM Customers "
                                 "ORDER BY Country")
        else:
            query = self.__query(f"SELECT * FROM Customers "
                                 f"WHERE Country LIKE '%{name}%'"
                                 f"ORDER BY Country")
        for x in query:
            print(x)
