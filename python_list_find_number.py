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

#MY STUFF!

#testing manual variable setting place:
print(l)
imputNumber = 0


def find_number(Number):
  #Set variables to their defaults
  frequency = 0
  locationList = []
  position = 0

  #This thing looks through everything
  while position <= 9:
    if l[position] == Number:
      frequency = frequency + 1
      locationList.append(position)
    position = position + 1
  #This thing compiles the outputs in 1 list and returns that
  outputList = [frequency,LocationList]
  return(outputList)
  #This is an alternate output meathod for the function
  print(frequency)
  print(locationList)
  
#This runs the function
find_number(imputNumber)

result = find_number(imputNumber)
numb = result.pop[0]

print(result)
print(numb)





