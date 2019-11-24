#This is the stuff from list_setup.py

# import the randint function from the random module
from random import randint

# create a function to generate a list of "size" random integers
# up to a maximum of "largest"

def random_list(largest,size):
  # create an empty list
  l = []
  # add a random number to the list the appropriate number of times
  for i in range(size):
    n = randint(0,largest-1)
    l.append(n)
  #print the list to check
  return(l)
#call the function
l = random_list(9,10)

#MY  STUFF!
print(l)


#Defining the function!
def find_minimum(length):
    #Note posi is position, loca is location
    posi = 1
    loca = 0
    while posi <= lenght:
       if l[loca] > l[posi]:
            loca = posi
       posi = posi+1
    Min = l[loca]
    return(loca)

#Making a new list to order
lFinal = []
lenght = 9
for f in range(10):
    Minimum = find_minimum(lenght)
    Value = l.pop(Minimum)
    lFinal.append(Value)
    lenght = lenght-1

#Printing final list:
print(lFinal)
