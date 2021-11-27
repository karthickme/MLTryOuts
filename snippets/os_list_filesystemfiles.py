import os

# The path for listing items
path = 'data/03Temperature'
# The list of items
files = os.listdir(path)
# Loop to print each filename separately
for filename in files:
    print(filename)
