products = {
    "Laptop": 55000,
    "Headphones": 1500,
    "Keyboard": 1200,
    "Monitor": 9000,
    "Mouse": 600
    

}

higest_products=max(products,key=products.get) #find the higest value in the dictionary
higest_price=products[higest_products]
print("product with highest price:",higest_products)
print("highest price is:",higest_price)