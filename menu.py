# sodas = [
#     ('Fanta',300),
#     ('Coke',300),
#     ('Pepsi',250),
#     ('Sprite',250),
#     ('7up',200),
#     ('Maltina',400),
#     ('Mirinda',250),
#     ('Limca',200)
# ]
# print(sodas)
# alcohols = [
#     ('Trophy',600),
#     ('Heineken',700),
#     ('Goldberg',900),
#     ('333',1500),
#     ('Star',300)
# ]
# print(alcohols)
# wines = [
#     ('Big Veleta',2000),
#     ('Small Veleta',1000)
# ]
# print(wines)

# user = input('''                   WELCOME TO  THE  HOME OF VARIOUS DRINKS
# Which category of drinks do you want to order from?
#     1.sodas 
#     2.alcohols
#     3.wines 
# Option:  ''').strip()
# if user == '1' or user.strip().capitalize() == sodas:
#    user = input()

Phones = [
    ('SAMSUNG',1200000),
    ('IPHONE',300000),
    ('INFINIX',150000),
    ('REDMI',79000),
    ('TECNO',120000),
    ('GIONEE',90000),
    ('VIVO',70000),
    ('OPPO',60000),
    ('ITEL',30000),
    ('HUAWEI',80000)
]
order = []
products = []
prices = []
user_choice1 = input('''
                                        LUXURY PHONE DEPOT
Welcome to the home of different product of phones,what product would you like to purchase?''').strip().upper()
       
for product,price in Phones:
         products.append(product)
         prices.append(price)
if user_choice1  in products:
            #  print(user_choice, 'is available at our store.' )
             _index = products.index(user_choice1)
             _status1 = prices[_index]
             order.append(_status1)
             print('It costs #',_status1)
else:
            print(user_choice1,' is not available in our store at the moment.Check again in few days!')

user = input('Would you like to purchase something else?\n A.)Yes\n B.)No\n Option:')
if user == 'Yes' or user == 'a' or user == 'A'.strip().capitalize():
    user_choice2=(input('Which other product would you like to purchase?')).strip().upper()
    for product,price in Phones:
           products.append(product)
           prices.append(price)
    if user_choice2 in products:
            # print(user_choice, 'is available at our store.' )
            _index = products.index(user_choice2)
            _status2 = prices[_index]
            print('It costs #',_status2)
            order.append(_status2)
            print('Thanks for your patronage sir\ma.Your order are as follows:\n',
                  '1.', user_choice1 ,'>>>>> #', _status1,'.\n',
                  '2.', user_choice2 , '>>>>> #', _status2,'.\n',
                   'The total amount is # ',  sum(order))
            user = input('  Due to the fact that we do not accept transfer here,\n  kindly make your payment to the account number that follows\n  4204816016 (Zenith bank) and input your address: ')
            print (' Wait for your order(s) to be delivered...') 
    else: 
            print(user_choice2,' is not available in our store at the moment.Check again in few days!')
            print('Thanks for your patronage.The total amount is #', _status1)
            user = input('  Due to the fact that we do not accept transfer here,\n  kindly make your payment to the account number that follows\n  4204816016 (Zenith bank) and input your address: ')
            print ('  Wait for your order(s) to be delivered...')
            

             
else:
    print('Thanks for your patronage.The total amount is #', _status1)
    user = input('  Due to the fact that we do not accept transfer here,\n  kindly make your payment to the account number that follows\n  4204816016 (Zenith bank) and input your address: ')
    print ('  Wait for your order(s) to be delivered...')
    exit()
       































# user_choice = input('''
#                               LUXURY PHONE DEPOT
# What product will you like to purchase? ''').strip().upper()
# order =[]
# brands = []
# prices  = []
# for brand,price in Phones:
#     brands.append(brand)
#     prices.append(price)
#     _index = brands.index(user_choice)
#     _status = prices[_index]
#     if user_choice in brands:
#         print(user_choice,' is available in our store at #', _status)
# else:
#     print(user_choice,' is not available in our store at the moment.Check again in few days!')
# _index = brands.index(user_choice)  
# print(_index) 
# _status = prices[_index]
# ............................................................................................
# print(f"The price is # {_status}") 
# # order.append(_status)  
# user = input('Would you like to purchase something else?\n A.)Yes\n B.)No\n Option:')
# if user == 'Yes' or user == 'a' or user == 'A'.strip().capitalize():
#     user_choice=(input('Which other product would you like to purchase?'))   
#     if user_choice in brands:
#         print(user_choice,' is available in our store.')
#     else:
#          print(user_choice,' is not available in our store at the moment.Check again in few days!')
        #  _index = brands.index(user_choice)  
        #  _status = prices[_index]
         

# else:
#      print (sum(order))
#      exit()
   
# order.append(_status)  
# print (sum(order)) 

    # print(brand)
#   yerfb4nf34unrfy342yrf
# choice = 0
# items = ["Toast", "Sandwich", "Ice cream"]
# print("Welcome to the menu! Here are the items available:")
# for item in items:
#   print(item)
# print("Please enter a number to choose an item.")
# choice = int(input(""))

#  bffhjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
# print("Hello, and welcome to the ordering system!")
# print("Please enter your choice:")
# choice = input(" ")
# while choice not in range(1, 101):
#     if choice == "phone":
#         item = "phone"
#         price = "10.00"
#     elif choice == "case":
#         item = "case"
#         price = "5.00"
#     elif choice == "screen protector":
#         item = "screen protector"
#         price = "3.00"
# print("Thank you for using the ordering system! Your total is: ")
# total = item + item * price
# print(f"Total: ${total:.2f}")
# print("Thank you, and have a great day!")
