'''
While-Else

    while condition:
        execute_condition_is_true()
    else:
        execute_condition_is_false()

For a simple case, it's the same as putting the false block after the while block
because eventually the condition will be 'falsy'.

    while condition:
        execute_condition_is_true()
    execute_condition_is_false()

For a more complex case, we can exit the while loop without the condition being 'falsy'
and the code would execute when we didn't want it.
We could add an if statement to check if the false block should execute but then the 
condition would be duplicated.

    while condition:                            # 1st use
        flag = execute_condition_is_true()
        if flag:
            break
    if condition:                               # 2nd use: Repetition
        execute_condition_is_false()

Correct use. The false block only executes if the condition is falsy and is not executed 
if we get to the break to jump out of the while block.

    while condition:
        flag = execute_condition_is_true()
        if flag:
            break
    else:                                       # nobreak
        execute_condition_is_false()
'''

'''
Program to stack operators and parameters.
'''

def is_comment(item):
    return isinstance(item, str) and item.startswith('#')

def execute(program):
    '''Execute a stack program.

    Args:
        program: Any stack-like containing where each item in the stack
            is a callable operator or a non-callable operand. The top-most
            items on the stack may be strings beginning with '#' for
            the purposes of documentation. Stack-like means support for:

                item = stack.pop()  # Remove and return the top item
                stack.append(item)  # Push an item to the top
                if stack:           # False in a boolean context when empty
    '''
    # Find the start of the 'program' by skipping
    # any item which is a comment
    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else:   # nobreak
        print("Empty program")
        return

    # Now we have eliminated every comment and all items comprise the actual program
    # Evaluate the program.
    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e:
                print("Error: ", e)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else:   # nobreak
        print("Program successful.")
        print("Result: ", pending)
    print("Finished.")



if __name__ == "__main__":
    import operator

    program = list(reversed((
        "# A short stack program to add",
        "# and multiply some constants",
        5,
        2,
        operator.add,
        3,
        operator.mul)))
    # Result should be: (5 + 2) * 3 = 21
    execute(program)
    # Program successful.
    # Result:  [21]
    # Finished.