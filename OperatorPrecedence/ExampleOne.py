# The operator precedence determines which operators need to be evaluated first.
# To avoid ambiguity in values, precedence operators are necessary. Just like in normal multiplication method,
# multiplication has a higher precedence than addition. For example in 3+ 4*5, the answer is 23, to change the order
# of precedence we use a parentheses (3+4)*5, now the answer is 35. Precedence operator used in
# Python are (unary + - ~, **, * / %, + - , &) etc.

v = 4
w = 5
x = 8
y = 2
z = 0
z = (v + w) * x / y;
# z = (v + w) * x;
# z = v + w * x;
# z = v + w * x / y;
print("Value of (v+w) * x/ y is ", z)
