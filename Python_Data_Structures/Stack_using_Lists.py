empty_stack = []



def push_func(empty_stack,numbers_to_store_in_stack):
    if len(empty_stack) == numbers_to_store_in_stack:
        print("range exceeded",)
    else:
        number = int(input("Enter the number to store in stack"))
        empty_stack.append(number)
        return number

def pop_func(empty_stack):
    if not empty_stack:
        return "stack is empty"
    else:
        num = empty_stack.pop()
        return num

numbers_to_store_in_stack = int(input("Enter the range to store in stack"))
while True:

    print("select the operation 1.push 2.pop 3.quit")
    select_option = int(input("Select the option"))
    if select_option == 1:
        push_output = push_func(empty_stack,numbers_to_store_in_stack)
        print("added number",push_output, empty_stack)
    elif select_option == 2:
        pop_output = pop_func(empty_stack)
        print("removed num", pop_output, empty_stack)
    elif select_option==3:
        break
    else:
        print("please select the correct option to do operation")


