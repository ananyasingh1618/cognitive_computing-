with open('sample.txt', 'a') as file:
    file.write('\nThis is the appended text.')
with open('sample.txt', 'r') as file:
    content = file.read()
print(content)
