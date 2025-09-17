# Swapping without creating third varaible:

def swapping(num1, num2): # return num1 with value of num2 and vice versa
    # say num1 = a, num2 = b
    num1 = num1 ^ num2
    num2 = num1 ^ num2 # equiv. to (a ^ b) ^ num2 = a, hence num2 = num1's value
    num1 = num1 ^ num2 # equiv. to (a ^ b) ^ num2 = (a ^ b) ^ a = b, hence num1 = num2's value
    return "num1:"+str(num1) + "; num2:"+str(num2)
    
print(swapping(11,22))