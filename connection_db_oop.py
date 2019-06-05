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
           result = round(float(''.join(c for c in str(x) if c.isdigit() or c == ".")),2)
           print("£"+str(result))