# For this project, you will be implementing a program that will check your math for you! Your program will take as input:

# The operation. Your program should support the following operations:

# add

# multiply

# divide

# subtract

# remainder (hint: the % operator will be useful)

# exponent

# 2 numbers to perform the operation on

# The expected answer

# Your program will perform the requested operation on the provided numbers, and compare the computed answer with the expected answer provided by the user. If they match, print a success message which includes the answer. If they don't match, print a message with both the expected answer and the actual answer.

#Your program should never fail. If the user provides invalid input - either an unsupported operation or an impossible task (such as dividing by zero) - your program should output "Invalid input. Please try again". ###

# Enter operation:add
# Enter first number:4
# Enter second number:16
# Enter expected answer:20
# You were correct! The answer is 20.0

# add input validation to the input numbers
# input ints output floats

operation = input("Enter operation?").lower()
nums1 = int(input("Enter first number?"))
nums2 = int(input("Enter second number?"))
given_answer = int(input("Enter expected answer?"))

# ADDITION OPERATION
if operation == 'add':
    expected_answer = nums1 + nums2
    if expected_answer == given_answer:
        print(f"You were correct! The answer is {given_answer}")
    else:
        print(
            f"your answer is wrong it should be {expected_answer} instead of {given_answer}"
        )

# MULTIPLICATION OPERATION
elif operation == 'multiply':
    expected_answer = nums1 * nums2
    if expected_answer == given_answer:
        print(f"You were correct! The answer is {given_answer}")
    else:
        print(
            f"your answer is wrong it should {expected_answer} instead of {given_answer}")

# DIVISION OPERATION
elif operation == 'divide':
    if nums2 == 0:
        print("Invalid input. Please try again.")
    else:
        expected_answer = nums1 / nums2
        if expected_answer == given_answer:
            print(f"You were correct! The answer is {given_answer}")
        else:
            print(
                f"your answer is wrong it should be {expected_answer} instead of {given_answer}"
            )

# SUBTRACTION OPERATION
elif operation == 'subtract':
    expected_answer = nums1 - nums2
    if expected_answer == given_answer:
        print(f"You were correct! The answer is {given_answer}")
    else:
        print(
            f"your answer is wrong it should be {expected_answer} instead of {given_answer}"
        )

# REMAINDER OPERATION
elif operation == 'remainder':
    if nums2 == 0:
        print("Invalid input. Please try again.")
    else:
        expected_answer = nums1 % nums2
        if expected_answer == given_answer:
            print(f"You were correct! The answer is {given_answer}")
        else:
            print(
                f"your answer is wrong it should be {expected_answer} instead of {given_answer}"
            )

# Exponent Operation
elif operation == 'exponent':
    expected_answer = nums1 ** nums2
    if expected_answer == given_answer:
        print(f"You were correct! The answer is {given_answer}")
    else:
        print(
            f"your answer is wrong it should be {expected_answer} instead of {given_answer}"
        )
else:
    print("Invalid Operation, please check your input and try again")
