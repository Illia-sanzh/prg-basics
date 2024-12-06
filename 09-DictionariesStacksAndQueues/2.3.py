import queue
close_brackets = [']', '}', ')']
open_brackets = ['[', '{', '(']
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    expressionqueue = queue.LifoQueue()
    for element in expression:
        if element in open_brackets:
            expressionqueue.put(element)
        if element in close_brackets:
            opbracket = expressionqueue.get()
            clbracket = element 
            if open_brackets.index(opbracket) == close_brackets.index(clbracket):
                continue
            else: 
                return False
    if expressionqueue.empty() == False:
        return False

    return True



if brackets_ok(expression3) == True:
   print(True)
else:
   print(False)

# if brackets_ok(expression2):
# ...
# ...