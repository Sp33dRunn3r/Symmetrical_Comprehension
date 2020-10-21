# Dictionary Comprehension
my_dict = {'a': 1, 'b': 2}
my_dict = {k:v**2 for k, v in my_dict.items()}

print(my_dict)
Dictionary Comprehension
my_dict = {'a': 1, 'b': 2}
my_dict = {k:v**2 for k, v in my_dict.items()
if v%2==0}

print(my_dict)

Dictionary Comprehension
my_dict = {k: k*2 for k in [1,2,3]}

print(my_dict)
