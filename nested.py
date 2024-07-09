#1 wap to check whether the given number is even and grater than 5 num = 2

# num = 2
# if num % 2 == 0:
#     print("even")
#     if num > 5:
#         print("correct nummber")
#     else:
#         print("wrong number")
# else:
#     print("wrong number")

#2 wap to check number is odd and check if num is div by 5

# num = 35
# num = 33
# if num % 2 != 0:
#     print("odd")
#     if num % 7:
#         print("divisible by 7")
#     else:
#         print("not divisible number")
# else:
#     print("wrong number")

#4

# username = "python"
# password = "python masters"
#
# inusernm = str(input("enter username"))
# inusrpas = str(input("enter password"))
#
# if inusernm == username:
#     print("correct username")
#     print("enter password")
#     if(inusrpas == password):
#         print("correct password")
#     else:
#         print("wrong password")
# else:
#     print("worng username")





#5 Movie

# theaters = {
#     "Theater A": {
#         "Movie 1": 150,
#         "Movie 2": 200
#     },
#     "Theater B": {
#         "Movie 3": 180,
#         "Movie 4": 220
#     }
# }
#
# print("Welcome to Book My Show!")
# print("Available theaters:")
# for theater in theaters:
#     print(theater)
#
# chosen_theater = input("Enter theater name: ")
#
# if chosen_theater in theaters:
#     print(f"Available movies in {chosen_theater}:")
#     for movie in theaters[chosen_theater]:
#         print(movie)
#
#     chosen_movie = input("Enter movie name: ")
#
#     if chosen_movie in theaters[chosen_theater]:
#         ticket_price = theaters[chosen_theater][chosen_movie]
#         print(f"Ticket price: {ticket_price}")
#
#
#         confirm = input("Do you want to book the ticket? (yes/no): ").lower()
#         if confirm == "yes":
#             print("Ticket booked successfully!")
#             print(
#                 f"You have booked the movie '{chosen_movie}' at '{chosen_theater}' for {ticket_price}")
#         else:
#             print("Booking canceled.")
#     else:
#         print("Invalid movie selection. Please try again.")
# else:
#     print("Invalid theater name. Please try again.")



#6 wap to find middle element is even or odd

# s = [3,4,6,6,9,1,5]
# if len(s)%2==1:
#     print("its odd")
#     res=s[len(s)//2]             #7/2--->3.5    #7//2---->3
#     if res%2==0:
#         print("even")
#
#     else:
#         print("odd")
# else:
#     print("its even")



#7 Define the available shopping apps and categories
# apps = ["flipkart", "amazon"]
# categories = ["electronics", "mobile", "fashion", "furniture"]
#
# select_app = input("Enter app name (flipkart/amazon): ").lower()
# select_category = input("Enter category (electronics/mobile/fashion/furniture): ").lower()
#
# if select_app in apps:
#     print("Selected app:", select_app)
#
#     if select_category in categories:
#         print(f"You are purchasing a phone from the '{select_category}' category.")
#         print("product purchased succesfully")
#     else:
#         print("Invalid category selected.")
# else:
#     print("Invalid app selected.")







#8 Input details for each product
# print("Enter details for Product 1:")
# product1_price = float(input("Enter price for Product 1: "))
# print("Enter details for Product 2:")
# product2_price = float(input("Enter price for Product 2: "))
# print("Enter details for Product 3:")
# product3_price = float(input("Enter price for Product 3: "))
#
# total_amount = product1_price + product2_price + product3_price
# num_products = 3
# payment_mode = input("Enter payment mode (credit card or other): ")
#
# if num_products >= 3 and total_amount >= 1500 and payment_mode.lower() == 'credit card':
#     discount = 0.1 * total_amount
#     discounted_amount = total_amount - discount
#     print(f"Total amount after 10% discount: {discounted_amount:.2f}")
# else:
#     print("Sorry, you are not eligible for the discount.")



#9

# Initialize an empty list
# my_list = [1,2,3,4]
#
# while True:
#     print("\nCurrent list:", my_list)
#     print("Menu:")
#     print("1. pop()")
#     print("2. sort()")
#     print("3. clear()")
#     print("4. Exit")
#
#     choice = input("Enter your choice (1/2/3/4): ")
#
#     if choice == '1':
#         if isinstance(my_list, list):
#             if len(my_list) > 0:
#                 popped_element = my_list.pop()
#                 print(f"Popped element: {popped_element}")
#             else:
#                 print("List is empty. Cannot pop.")
#         else:
#             print("Invalid data type. Please enter list data type.")
#     elif choice == '2':
#         if isinstance(my_list, list):
#             my_list.sort()
#             print("List sorted.")
#         else:
#             print("Invalid data type. Please enter list data type.")
#     elif choice == '3':
#         if isinstance(my_list, list):
#             my_list.clear()
#             print("List cleared.")
#         else:
#             print("Invalid data type. Please enter list data type.")
#     elif choice == '4':
#         print("Exiting program.")
#         break
#     else:
#         print("Invalid option. Please choose from 1, 2, 3, or 4.")
