
'''
Five-letter word collection (e_dict_filter.py)

Uses file scrabble_dict.txt to create filtered.txt
filtered.txt contains only five-letter words
To be used in wordle.py as collection of valid guesses
'''

# Opens file of all (Scrabble) words
og = open('scrabble_dict.txt', 'r')

# Creates and opens file for storing five-letter (Scrabble) words
filt = open('filtered.txt', 'w')

# Finds all five-letter words and writes them to filtered.txt
while True:
    line = og.readline()
    if line == '':
        break
    if len(line) == 6:
        filt.write(line)

# Closes both files
og.close()
filt.close()
