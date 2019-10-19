"""
author = Petr Filip
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

passwords = {'bob': '123',
             'ann': 'pass123',
             'mike': 'password123',
             'liz': 'pass123'}

# Welcome the user and ask for username and password
print(40 * '-')
print('Welcome to the app. Please log in:')
username = input('Username: ')
password = input('Password: ')
print(40 * '-')

# Check password
if username not in passwords.keys() or password not in passwords.values():
    print('Wrong password or username.')
    exit()
elif passwords.get(username) != password:
    print('Wrong password or username.')
    exit()

# Choose text
print('We have three texts to be analyzed.')
select = input('Enter a number between 1 and 3 to select: ')
while select not in ['1', '2', '3']:
    select = input('Enter a number between 1 and 3 to select: ')
select = int(select)
print(40 * '-')
words = TEXTS[select-1].split()

# Words counting
words_total = len(words)
words_capital = 0
words_uppercase = 0
words_lowercase = 0
words_num_only = 0
num_sum = 0
frequency = {}
i = 0
while i < len(words):
    if words[i].istitle():
        words_capital += 1
    elif words[i].isupper():
        words_uppercase += 1
    elif words[i].islower():
        words_lowercase += 1
    elif words[i].isdigit():
        words_num_only += 1
        num_sum += float(words[i])
    length = len(words[i])
    if words[i].endswith(',') or words[i].endswith('.'):
        length -= 1
    freq = frequency.get(length, 0)
    frequency.update({length: freq + 1})
    i += 1
print('There are', words_total, 'words in the selected text.')
print('There are', words_capital, 'titlecase words')
print('There are', words_uppercase, 'uppercase words')
print('There are', words_lowercase, 'lowercase words')
print('There are', words_num_only, 'numeric strings')
print(40 * '-')

# Frequencies of word lengths in the text
while frequency:
    min_key = min(frequency.keys())
    min_value = frequency.pop(min_key)
    print(min_key, min_value * '*', min_value)

# Sum of numbers in the text
print(40 * '-')
print('If we summed all the numbers in this text we would get:', num_sum)
