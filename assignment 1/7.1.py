
with open('sample.txt', 'w') as file:
    file.write('Hello, this is a text file!\n')
    file.write('This file contains some sample text.')
with open('sample.txt', 'r') as file:
    content = file.read()
print(content)
