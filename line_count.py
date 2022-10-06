fhand = open('input.py')
read = fhand.read()
char_count = (len(read))
line_count = 0
for cheese in fhand:
    line_count += 1
print(f'input.py has {line_count} lines of code,')
print(f'and has {char_count} characters.')