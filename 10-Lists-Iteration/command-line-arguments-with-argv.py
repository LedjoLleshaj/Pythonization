import sys

print(sys.argv) # prints the list of command line arguments including the name of the script
 
word_lengths = 0

for arg in sys.argv[1:]:
    word_lengths += len(arg)

print(word_lengths)

