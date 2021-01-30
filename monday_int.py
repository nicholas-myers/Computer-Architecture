# Given the following array of values, print out all the elements in reverse order, with each element on a new line.
# For example, given the list
nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# Your output should be
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# 1 function accepts a list of numbers
def print_rev(list):
# reverse the list
    list.reverse()
# iterate through each num
    for num in list:
# print the num
        print(num)
        
# print_rev(nums)

# STRETCH
# Given a hashmap where the keys are integers, print out all of the values of the hashmap in reverse order, ordered by the keys. 
# For example, given the following hashmap:
# ```
info = {
  14: "vs code",
  3: "window",
  9: "alloc",
  26: "views",
  4: "bottle",
  15: "inbox",
  79: "widescreen",
  16: "coffee",
  19: "tissue",
}
# ```
# The expected output is:
# ```
# widescreen
# views
# tissue
# coffee
# inbox
# vs code
# alloc
# bottle
# window
# ```
# since "widescreen" has the largest integer key, "views" has the second largest, etc. 
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# function accepts a dictionary
def print_reverse_dict(dict):
# put the keys in reverse order
    in_order = sorted(dict.keys())
    in_order.reverse()
    # make a new dict that is in the correct order
    reversed_order = {k: dict[k] for k in in_order}
    print(reversed_order)
# print each value
    
    for v in reversed_order.values():
        print(v)

print_reverse_dict(info)