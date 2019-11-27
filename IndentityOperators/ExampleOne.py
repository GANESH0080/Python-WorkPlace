# To compare the memory location of two objects, Identity Operators are used.
# The two identify operators used in Python are (is, is not).


x = 20
y = 20
if ( x is y ):
	print("x & y  SAME identity")
y=30
if ( x is not y ):
	print("x & y have DIFFERENT identity")