
from num2words import num2words
num_list = [5]
print(num2words(403871925486174, lang = 'de'))
print(num2words(405023, lang = 'sl'))

num_list.append(num2words(40, lang = 'pt'))
num_list.append(num2words(41, lang = 'pt'))
num_list.append(num2words(42, lang = 'pt'))
print(num_list)