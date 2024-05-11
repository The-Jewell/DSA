# Write a function called unique_english_letters that takes the string word as a parameter. The function should return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as different letters.
# We’ve given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include that list in your function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  count = []
  for letter in word:
    if letter in letters and letter not in count:
      count.append(letter)
  return len(count)

#tests
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

#Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.
# Write your count_char_x function here:
def count_char_x(word, x):
  count = 0
  for letter in word: 
    if letter == x:
      count +=1
  return count
  
# tests
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1


# Write a function named count_multi_char_x that takes a string named word and a string named x. This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. However, this time, make sure your function works when x is multiple characters long.
# For example, count_multi_char_x("Mississippi", "iss") should return 2

# Write your count_multi_char_x function here:4
def count_multi_char_x(word, x):
  split_word = word.split(x)
  return (len(split_word) -1)

# tests
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.
# For example, substring_between_letters("apple", "p", "e") should return "pl".

# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  start_index= word.find(start)
  end_index = word.find(end)
  if start_index == -1 or end_index == -1:
    return word
  else:
    return word[start_index+1: end_index]


# tests
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

#Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. This function should return True if every word in sentence has a length greater than or equal to x.
# Write your x_length_words function here:
def x_length_words(sentence, x):
  split_sentence = sentence.split()
  for word in split_sentence:
    if len(word) < x:
      return False
    else:
      print(split_sentence)
      return True
# tests
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


# Write a function called check_for_name that takes two strings as parameters named sentence and name. The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. The function should return False otherwise.
# For example, the following three calls should all return True:
# check_for_name("My name is Jamie", "Jamie")
# check_for_name("My name is jamie", "Jamie")
# check_for_name("My name is JAMIE", "Jamie")
# Write your check_for_name function here:

def check_for_name(sentence, name):
  words = sentence.split()
  for word in words:
    if word.lower() == name.lower():
      return True
  return False
  
# tests
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# Create a function named every_other_letter that takes a string named word as a parameter. 
# The function should return a string containing every other letter in word.

# Write your every_other_letter function here:
def every_other_letter(word):
  eol = ""
  for i in range(0,len(word),2):
    eol = eol + (word[i])
  return(eol)   

# tests
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

# Write a function named reverse_string that has a string named word as a parameter. 
# The function should return word in reverse.

# Write your reverse_string function here:
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse = reverse + word[i]
  return reverse 
  
# test
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. 
# Return the two new words as a single string separated by a space.
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  new_word1 = word2[0] + word1[1:]
  new_word2 = word1[0] + word2[1:]
  return new_word1 + " " + new_word2

# tests
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# Create a function named add_exclamation that has one parameter named word. This function should add exclamation points to the end of word until word is 20 characters long. 
# If word is already at least 20 characters long, just return word.

# Write your add_exclamation function here:
def add_exclamation(word):
  while len(word) < 20:
    word += "!"
  return word  
# tests:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn