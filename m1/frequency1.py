input_dictionary = {}
length = int(input('enter the length of the dictionary: '))
for i in range(length):
    key = input('enter a key: ')
    value = int(input('enter a value: '))
    input_dictionary[key] = value
# printing original dictionary
print("The original dictionary : " +  str(input_dictionary))
  
# Initialize value 
K = int(input('enter the search key: '))
  
# Using loop
# Selective key values in dictionary
res = 0
for key in input_dictionary:
    if input_dictionary[key] == K:
        res = res + 1
      
# printing result 
print("Frequency of K is : " + str(res))
