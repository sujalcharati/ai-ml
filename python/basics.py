# This will be the basics for python let gets started ...

#  numbers

# a = 4
# b=5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)
# print(a/b) #always give in point value  ie float value
# print(a**b) # power func



# text 

# a = "my name is sujal\n i am an engineer"
# print(a) #\n is used for new line

# print(a[4]) # indexing for individual
# print([a[1:4]]) # slicing for substring
# print(a[-1]) # last index
# print(a[:12])
# print(a[:2]+a[22:]) # slice concatenation

# print('J' + a[1:])
# print(a[:2] + 'py')
# print(len(a)) # length func



# lists

# myarea = ["cse","cyrpto","web3","devops"]
# print(myarea)
# print(myarea[0])
# print(myarea[-2])
# print(myarea[2:])
# print(myarea[:1]+ myarea[2:]) # remove crypto
# print(myarea + ["iot","vlsi"])
# myarea[2] = "blockchain"  #mutable lists
# print(myarea)
# myarea.append("cloud") # append
# print(myarea)

# myfeild = myarea  # passing reference
# print(myfeild)
# print(id(myfeild) == id(myarea)) # bool val
# myfeild.append("webdev")
# print(myfeild)
# print(myfeild[4:])
# print(len(myfeild))

# my2d = [[1,0,2],[2,5,6]] # 2d list
# print(my2d[0][2])


# simple fibonacci

# a=1
# b=2
# while a < 10:
#     print(a)
#     a,b =b,a+b


# conditional statement

# if and if-else elif
# x = int(input(" enter a nummber\n ")) # user defined input
# if  x< 0:
#     print(" its negative number")
# elif x==0:
#     print(" its zero")
# else:
#     print(" its positive")

# for loop

# Measure some strings:
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

# # Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#         print(active_users)

# range func

# for i in range(8):
#     print(i)

# print(list(range(2,6)))

# words = ['cat', 'window', 'defenestrate']

# for i in range(len(words)):
#     print(i,words[i])

# print(sum(range(10))) # does 0+1+2+3+4+...+9



# break and continue 

# break for exit of loop and  continue for the skip current iteration and move to next iteration
# a = 1
# while a <10:
#     a+=1
#     print(" condition is true")
#     if a == 5:
#         print("this is done")
#         break
    

# for num in range(1,10):
#   if num % 2 == 0:
#      print(f"got even number {num}")
#      continue
#   print(f"got 0dd number {num}")



# switch/match - case statement




# Define a point as an (x, y) tuple
# point = (0, 0)  # You can change these values to test different cases

# # point is an (x, y) tuple
# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"Y={y}")
#     case (x, 0):
#         print(f"X={x}")
#     case (x, y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a point")




# functions




# def writesomething():
#     print(" writing something")
# writesomething()





    

