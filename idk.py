import time

my_array = ["Lorem", "Noob", "blah", "elite"]


def On(search):  # just search it linearly
    for thing in my_array:
        if thing == search:
            return True


# Log N would be sorted then binary search

# to make it O(1)
# take 1 more step to just access the element like my_array[3] or something
# by using a function that return index in this case it's Hash function

def len_hash(string):
    return len(string)


# problem is it doesn't work with another word with same length
# what about long word

long_word = "Hippopotomonstrosesquippedaliophobia"
long_word_hash = len_hash(long_word)
long_word_index = long_word_hash % len(my_array)

my_array[long_word_index] = long_word


# try assign a number to all letter
# good thing ASCII already done this


def add_hash(string):
    total = 0
    for letter in string:
        total += ord(letter)
    return total


# this is a bit better, but it doesn't work with anagrams

# encode stuff here
def utf8_hash(string):
    total = 0
    string_bytes = string.encode()
    for b in string_bytes:
        total += b
    return total


my_array = [None] * 8


def put(key, string):
    hashed_string = utf8_hash(key)
    index = hashed_string % len(my_array)
    my_array[index] = string


put("Hello", "Hello World")


def get(string):
    hashed_string = utf8_hash(string)  # turn it into number first
    index = hashed_string % len(my_array)  # turn it into index
    value = my_array[index]
    return value


get("Hello")


def fibonacci_sequence(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci_sequence(num - 1) + fibonacci_sequence(num - 2)


start_time = time.time()
print(fibonacci_sequence(37))
end_time = time.time()
execution_duration = end_time - start_time
print(f"it took {execution_duration:.6f} seconds to execute")

# it takes longer time exponentially compare to how big the number is,
# so basically it's an example of what not to do
