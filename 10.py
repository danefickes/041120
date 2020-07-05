alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_list = []
for letter in alpha:
    alpha_list.append(letter)

count = 0
alpha_dict = {}
for letter in alpha_list:
    alpha_dict[count] = letter
    count += 1

reverse_alpha_dict = {}
for entry in alpha_dict:
    reverse_alpha_dict[alpha_dict[entry]] = entry

tuples = ()
tuple_list = []
for entry in reverse_alpha_dict:
    tuples = (entry, reverse_alpha_dict[entry])
    tuple_list.append(tuples)

print(tuple_list)


#for number in range(5,10):
#    print(alpha_dict[number])

