#Exercise 2
#Modify the postfix evaluation algorithm so that it can handle errors.

from pythonds.basic import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    try:
        for token in tokenList:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = doMath(token,operand1,operand2)
                operandStack.push(result)
        return operandStack.pop()
    except IndexError:
        print("Error in formatting of input")

    
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        try:
            return op1 / op2
        except ZeroDivisionError:
            print("Cannot divide by zero")
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3.34 2 + /'))


#The error with adding decimals to the function 
#is that we check if the input resides in 0123456789.
