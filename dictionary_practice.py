# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary
def sum_values(my_dictionary):
  sum = 0
  for value in my_dictionary.values():
    sum += value
  return sum
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys.
def sum_even_keys(my_dictionary):
  sum = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      sum += my_dictionary[key]
  return sum
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. The function should add 10 to every value in my_dictionary and return my_dictionary
def add_ten(my_dictionary):
  for key in my_dictionary:
    my_dictionary[key] += 10 
  return my_dictionary  
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. This function should return a list of all values in the dictionary that are also keys.
def values_that_are_keys(my_dictionary):
  values_are_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary:
      values_are_keys.append(value)
  return values_are_keys
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]


# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.
def max_key(my_dictionary):
  highest_key = None
  highest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > highest_value:
      highest_value = value
      highest_key = key
  return highest_key  


# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"