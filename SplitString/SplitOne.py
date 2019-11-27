# Split means Udhar se spilit kro

name = "Ganesh Mahadev Salunkhe"
print(name.split())

word = 'geeks,for,geeks'
# Splits at ','
print(word.split(','))

wording = 'geeks:for:geeks'
# Splitting at ':'
print(wording.split(':'))

words = 'geeksfor geeks'
# Splitting at ' '
print(words.split())

# instead of space (' ') we will replace it with ('r') and it will split the string wherever 'r' is mentioned in the string
fname = "GanreshSarlunkhe"
# Splitting at 'r'
print(fname.split('r'))
