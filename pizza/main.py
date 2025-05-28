# pizzas sizes and price
small = 100.00
medium = 125.00
large = 150.00
family = 200.00

# sides and prices
small_pepperoni = 20
medium_large = 40
family_pepperoni = 50
cheese = 20

# total_bill
total_bill = 0
print("***welcome to pizza joint***")
menu_choice = input("Enter/n"
                    "s for small\n"
                    "m for medium\n"
                    "l for large\n"
                    "f for family:\n")


try:
    if menu_choice == "s":
        total_bill += small
        extra_pepperoni = input("would you add extra pepperoni? 'y' or 'n'\n").lower()
        if extra_pepperoni == "y":
           total_bill += small_pepperoni
        extra_cheese = input("would you add extra cheese: 'y' or no\n").lower()
        if extra_cheese == "y":
            total_bill += cheese
        print(f"Total bill Ghc{total_bill}")
    elif menu_choice == "m":
        total_bill += medium
        extra_pepperoni = input("would you add extra pepperoni? 'y' or 'no'\n").lower()
        if extra_pepperoni == "y":
            total_bill += medium_large
        extra_cheese = input("would you add extra cheese: 'y' or 'n'\n").lower()
        if extra_cheese == "y":
            total_bill += cheese
        print(f"Total bill Ghc{total_bill}")
    elif menu_choice == "l":
        total_bill += large
        extra_pepperoni = input("would you add extra pepperoni? 'y' or 'n'\n").lower()
        if extra_pepperoni == "y":
         total_bill += medium_large
         extra_cheese = input("would you add extra cheese: 'y' or 'n'\n").lower()
         if extra_cheese =="y":
             total_bill += cheese
         print(f"Total bill Ghc {total_bill}")    
    elif menu_choice == "f":
        total_bill += family
        extra_pepperoni =input("would you add extra pepperoni? 'y' or 'n'\n").lower()
        if extra_pepperoni == "y":
            total_bill += family_pepperoni
        extra_cheese = input("would you add extra cheese? 'y' or 'n'\n").lower()
        if extra_cheese == "y":
            total_bill += cheese
        print(f"Total bill Ghc{total_bill}")
    else:
        print("kindy provide an option from the menu!!!" )
except ValueError:
    print("kindy enter a vaild value")




       

