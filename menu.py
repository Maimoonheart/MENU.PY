# Phones = [
#     ('SAMSUNG',1200000),
#     ('IPHONE',300000),
#     ('INFINIX',150000),
#     ('REDMI',79000),
#     ('TECNO',120000),
#     ('GIONEE',90000),
#     ('VIVO',70000),
#     ('OPPO',60000),
#     ('ITEL',30000),
#     ('HUAWEI',80000)
# ]
# order = []
# products = []
# prices = []
# for product,price in Phones:
#          products.append(product)
#          prices.append(price)
#          print(product)
# user_choice1 = input('''
#                                         LUXURY PHONE DEPOT
# Welcome to the home of different product of phones,what product would you like to purchase?''').strip().upper()
       

# if user_choice1  in products:
#             #  print(user_choice, 'is available at our store.' )
#              _index = products.index(user_choice1)
#              _status1 = prices[_index]
#              order.append(_status1)
#              print('It costs #',_status1)
# else:
#             print(user_choice1,' is not available in our store at the moment.Check again in few days!')

# user = input('Would you like to purchase something else?\n A.)Yes\n B.)No\n Option:')
# if user == 'Yes' or user == 'a' or user == 'A'.strip().capitalize():
#     user_choice2=(input('Which other product would you like to purchase?')).strip().upper()
#     for product,price in Phones:
#            products.append(product)
#            prices.append(price)
#     if user_choice2 in products:
#             # print(user_choice, 'is available at our store.' )
#             _index = products.index(user_choice2)
#             _status2 = prices[_index]
#             print('It costs #',_status2)
#             order.append(_status2)
#             print('Thanks for your patronage sir\ma.Your order are as follows:\n',
#                   '1.', user_choice1 ,'>>>>> #', _status1,'.\n',
#                   '2.', user_choice2 , '>>>>> #', _status2,'.\n',
#                    'The total amount is # ',  sum(order))
#             user = input('  Due to the fact that we do not accept transfer here,\n  kindly make your payment to the account number that follows\n  4204816016 (Zenith bank) and input your address: ')
#             print (' Wait for your order(s) to be delivered...') 
#     else: 
#             print(user_choice2,' is not available in our store at the moment.Check again in few days!')
#             print('Thanks for your patronage.The total amount is #', _status1)
#             user = input('  Due to the fact that we do not accept transfer here,\n  kindly make your payment to the account number that follows\n  4204816016 (Zenith bank) and input your address: ')
#             print ('  Wait for your order(s) to be delivered...')
            

             
# else:
#     print('Thanks for your patronage.The total amount is #', _status1)
#     user = input('  Due to the fact that we do not accept transfer here,\n  kindly make your payment to the account number that follows\n  4204816016 (Zenith bank) and input your address: ')
#     print ('  Wait for your order(s) to be delivered...')
#     exit()
       
            #  USING FUNCTION

# Phones = [
#     ('SAMSUNG',1200000),
#     ('IPHONE',300000),
#     ('INFINIX',150000),
#     ('REDMI',79000),
#     ('TECNO',120000),
#     ('GIONEE',90000),
#     ('VIVO',70000),
#     ('OPPO',60000),
#     ('ITEL',30000),
#     ('HUAWEI',80000)
# # ]
# order = []
# products = []
# prices = []
# for product,price in Phones:
#          products.append(product)
#          prices.append(price)
#          print(product)

# def menu():
#     global user_choice1
#     user_choice1 = input('''
#                                         LUXURY PHONE DEPOT
# Welcome to the home of different product of phones,what product would you like to purchase?''').strip().upper()
       
        
    # if user_choice1  in products:
    #         #  print(user_choice, 'is available at our store.' )
    #          _index = products.index(user_choice1)
    #          global _status1
    #          _status1 = prices[_index]
    #          order.append(_status1)
    #          print('It costs #',_status1)
    # else:
    #         print(user_choice1,' is not available in our store at the moment.Check again in few days!')

    # user = input('Would you like to purchase something else?\n A.)Yes\n B.)No\n Option:')
    # if user == 'Yes' or user == 'a' or user == 'A'.strip().capitalize():
    #     user_choice2=(input('Which other product would you like to purchase?')).strip().upper()
    #     for product,price in Phones:
    #        products.append(product)
    #        prices.append(price)
    #     if user_choice2 in products:
    #         # print(user_choice, 'is available at our store.' )
    #         _index = products.index(user_choice2)
    #         _status2 = prices[_index]
    #         print('It costs #',_status2)
    #         order.append(_status2)
#             print('Thanks for your patronage sir\ma.Your order are as follows:\n',
#                   '1.', user_choice1 ,'>>>>> #', _status1,'.\n',
#                   '2.', user_choice2 , '>>>>> #', _status2,'.\n',
#                    'The total amount is # ',  sum(order))
#             conclusion()
#         else: 
#             print(user_choice2,' is not available in our store at the moment.Check again in few days!')
#             print('Thanks for your patronage.The total amount is #', _status1)
#             conclusion()        
#     else:
#         print('Thanks for your patronage.The total amount is #', _status1)
#         conclusion()
#         exit()
# def conclusion():
#     user = input('  Due to the fact that we do not accept cash here,\n  kindly make your payment to the account number that follows\n  4204816016 (Zenith bank) and input your address: ')
#     print ('  Wait for your order(s) to be delivered...')
         
# menu()       

                          # USING CLASS 

class menu:
    def __init__(self) -> None:
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
                    ('HUAWEI',80000)]
        order = []
        products = []
        prices = []
        for product,price in Phones:
            products.append(product)
            prices.append(price)
            print(product)
            global user_choice1
        user_choice1 = input('''
                                        LUXURY PHONE DEPOT
Welcome to the home of different product of phones,what product would you like to purchase?''').strip().upper()
       
        
        if user_choice1  in products:
            #  print(user_choice, 'is available at our store.' )
                 _index = products.index(user_choice1)
                 global _status1
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
                print('Thanks for your patronage sir\ma.Your order(s) are as follows:\n',
                  '1.', user_choice1 ,'>>>>> #', _status1,'.\n',
                  '2.', user_choice2 , '>>>>> #', _status2,'.\n',
                   'The total amount is # ',  sum(order))
                self.conclusion()
            else: 
                print(user_choice2,' is not available in our store at the moment.Check again in few days!')
                print('Thanks for your patronage.The total amount is #', _status1)
                self.conclusion()        
        else:
            print('Thanks for your patronage.The total amount is #', _status1)
            self.conclusion()
            exit()
    def conclusion(self):
            user = input('  Due to the fact that we do not accept cash here,\n  kindly make your payment to the account number that follows\n  4204816016 (Zenith bank) and input your address: ')
            print ('  Wait for your order(s) to be delivered...')
Menu= menu()