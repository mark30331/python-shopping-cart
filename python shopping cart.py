print("Welcome  to the shopping cart Program!")
shopping_cart =[]
prices = []
def main():    
    print("""
Please select one of the following:
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit 
        """)
    selection = input("Please enter an action: ")
    
    if selection == "1":
        add_item(shopping_cart, prices)

    elif selection == "2":
        view_cart(shopping_cart, prices)

    elif selection == "3":
        remove_item(shopping_cart, prices)

    elif selection == "4":
        compute_total(prices)

    elif selection == "5":
        quit()

    else:
        print("Invalid command")

def add_item(shopping_cart, prices):
    item = input("What item would you like to add? ")
    price = input("What is the price of the "+item+"? ")
    price = float(price)
    shopping_cart.append(item)
    prices.append(price)    
    print(item,"has been added to the cart")

def view_cart(shopping_cart, prices):
    print("The contents of the shopping carts are: ")    
    count = 0    
    for item in shopping_cart:
        price = prices[count]
        print(str(count+1)+".",item,"- $"+str(price))
        count += 1

def remove_item(shopping_cart, prices):
    count = 1
    while count > 0:
        try:
            item = int(input("Which item would you like to remove: "))            
            temp_variable = shopping_cart[item-1]
            del prices[item-1]
            del shopping_cart[item-1]   
            print(temp_variable,"has been removed")    
            count -= 1        
        except Exception as e:
            print("There is no such item")
           
def compute_total(prices):
    total = 0
    for x in prices:
        total += x    
    tax_rate = 0.06
    tax = tax_rate * total   
    print("Your tax was $"+str(tax))
    print("Your total price was $"+str(total))
    total = total+tax
    print("The total price of the items including taxes in the shopping cart was $"+str(round(total, 2)))
    
def quit():
    print("Thank you! Goodbye.")
    exit()

if __name__ == "__main__":
    while True:        
        main()
