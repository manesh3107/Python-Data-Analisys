import csv
import numpy as np
import matplotlib.pyplot as plt

class Product:
    def __init__(self, id, name, category, price, stock):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def update_stock(self, new_stock):
        self.stock = new_stock

    def update_price(self, new_price):
        self.price = new_price

class DataAnalysis:
    def __init__(self, file_name):
        self.products = []
        self.file_name = file_name

    def read_data_from_file(self):
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader) # skip the header row
            for row in reader:
                id, name, category, price, stock = row
                price = float(price)
                stock = int(stock)
                self.products.append(Product(id, name, category, price, stock))

    def display_products_by_category(self, category):
        print("List Of ",category," Products")
        for i,product in enumerate(self.products):
            if product.category == category:
                print(i+1,".",product.name)
        print(50*"**")

    def display_out_of_stock_products(self):
        for product in self.products:
            if product.stock == 0:
                print(product.name," is Out Of stock now")
        

    def display_products_by_price_range(self, min_price, max_price):
        print("Products which Price Range is between ",min_price," to ",max_price)
        for i,product in enumerate(self.products):
            if min_price <= product.price <= max_price:
                print(i+1,".",product.name)
        print(50*"*")

    def calculate_revenue(self):
        total_revenue = 0
        for product in self.products:
            total_revenue += product.price * (100 - product.stock)
        return total_revenue
    

    def plot_category_pie(self):
        categories = set([product.category for product in self.products])
        category_counts = {category: 0 for category in categories}
        for product in self.products:
            category_counts[product.category] += 1

        fig, ax = plt.subplots()
        ax.pie(category_counts.values(), labels=category_counts.keys(), autopct='%1.1f%%')
        ax.set_title("Product Categories")
        plt.show()


if __name__ == "__main__":

    data_analysis = DataAnalysis("product.csv")
    data_analysis.read_data_from_file()
    data_analysis.display_products_by_category("Accessories")
    data_analysis.display_out_of_stock_products()
    data_analysis.display_products_by_price_range(3000, 25000)
    revenue = data_analysis.calculate_revenue()
    print("Total revenue:", revenue)
    print(50*"*")

    
    # Using NumPy
    
    def minmax():
    
        prices = np.array([product.price for product in data_analysis.products])
        max_price = np.max(prices)
        min_price = np.min(prices)
        avg_price = np.mean(prices)
        print("Maximum product price:", max_price)
        print("Minimum product price:", min_price)
        print("Average product price:", avg_price)

    # Using mutable and immutable data structures

    def sold_order():
        products_sold = {}
        order_history = []
        for product in data_analysis.products:
            if product.stock > 0:
                order_history.append((product.name, product.price))
                product.update_stock(product.stock - 1)
                if product.name in products_sold:
                    products_sold[product.name] += 1
                else:
                    products_sold[product.name] = 1
        print("Products sold:", products_sold)
        print("Order history:", order_history)

    # Plotting product prices

    def graph_prodect():
        prices = np.array([product.price for product in data_analysis.products])
        plt.hist(prices)
        plt.xlabel("Price")
        plt.ylabel("Frequency")
        plt.title("Distribution of Product Prices")
        plt.show()


    # Plotting revenue by category

    def revenu_graph():
        categories = set([product.category for product in data_analysis.products])
        category_revenue = {category: 0 for category in categories}
        for product in data_analysis.products:
            category_revenue[product.category] += product.price * (100 - product.stock)
        colors=["blue","yellow","green","violet"]
        plt.bar(category_revenue.keys(), category_revenue.values(),color=colors)
        plt.xlabel("Category")
        plt.ylabel("Revenue")
        plt.title("Revenue by Category")
        plt.show()

        

    def choice():
        print("Press 1 to show Minmum and maximum prices")
        print("Press 2 to show Order and sold product data")
        print("Press 3 to show avarage prices graph")
        print("Press 4 to show revenue graph")
        print("Press 5 to show Catogry wise pie chart")

        ch=int(input("enter Number you want to show"))
        if ch==1:
            minmax()

        elif ch==2:
            sold_order()

        elif ch==3:
            graph_prodect()

        elif ch==4:
            revenu_graph()

        elif ch==5:
            data_analysis.plot_category_pie()

        else:
            exit()


    while True:
        choice()
        print("Do you Want to Display other data")
        print("Press 1 to continue press 2 to exit") 
        a=int(input())
        if a==2:
            break

