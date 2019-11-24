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
#Setting the number to use to partion!
partitionNumber = 4

#The Function!
def partition(number):
    lFinal = []
    
    #Adding Smaller Numbers:
    location = 0
    for i in range(10):
        if l[location] < number:
            lFinal.append(l[location])
        location += 1
        
    #Adding Equal Numbers:
    location = 0
    for i in range(10):
        if l[location] == number:
            lFinal.append(l[location])
        location += 1
        
    #Adding Bigger Numbers:
    location = 0
    for i in range(10):
        if l[location] > number:
            lFinal.append(l[location])
        location += 1

    return(lFinal)


#Performing the function!
output = partition(partitionNumber)
print(output)
