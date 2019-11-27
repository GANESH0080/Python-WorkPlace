# Global Variable
num = 100
print(num)


def globalmethod():
    # Local variable
    num = "I am ganesh Salunkhe"
    print(num)


globalmethod()
# Destroy the local variable because local variable scope is only in function or in method only
print(num)
