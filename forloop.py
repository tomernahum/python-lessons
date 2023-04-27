

# this is python

# i = 0
# while (i < 5):
#     print("Hello for the " + str(i) + "th time")
    
#     i += 1


print("---")


"""

Take user input

print to the console every letter of that user input line by line

"""

len("Hello")  #5

name = "Tomer"

for i in range(5):
    print(i)
    print(name[i]) 
    print()


print( "Tomer"[1:4] ) #     prints  "ome"
print( "abcdefg"[0:6:2] ) # prints  "ace"

print( "Tomer"[2:] ) # prints  "mer"    (leaving out the end index makes it go to the end of the string)


#print("Hello"[3:0:-1])

print("--------------")

for i in "Tomer":
    print(i)



for i in [0,1,2,3,4]:
    print(i)


myVar = 5
print( f"Tomer {myVar}")