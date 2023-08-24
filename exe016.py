
from num2words import num2words
num_list = [0]
for num in range (40, 51):
    num_in_words = num2words(num)
    num_list.append(num_in_words)
print(num_list)