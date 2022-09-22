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

operation = input("Enter operation?")
nums1 = int(input("Enter first number?"))
nums2 = int(input("Enter second number?"))
given_answer = int(input("Enter expected answer?"))


if operation == '+':
    expected_answer = nums1 + nums2
    if expected_answer == given_answer:
        print(f"You were correct! The answer is {given_answer}")
    else:
        print(
            f"your answer is wrong it should be {expected_answer} instead of {given_answer}"
        )
elif operation == '*':
    expected_answer = nums1 * nums2
    if expected_answer == given_answer:
        print(f"You were correct! The answer is {given_answer}")
    else:
        print(
            f"your answer is wrong it should {expected_answer} instead of {given_answer}")
elif operation == '/':
    if nums2 == 0:
        print("Invalid input. Please try again.")
    expected_answer = nums1 / nums2
    if expected_answer == given_answer:
        print(f"You were correct! The answer is {given_answer}")
    else:
        print(
            f"your answer is wrong it should be {expected_answer} instead of {given_answer}"
        )
elif operation == '-':
    expected_answer = nums1 - nums2
    if expected_answer == given_answer:
        print(f"You were correct! The answer is {given_answer}")
    else:
        print(
            f"your answer is wrong it should be {expected_answer} instead of {given_answer}"
        )
elif operation == '%':
    if nums2 == 0:
        print("Invalid input. Please try again.")
    expected_answer = nums1 % nums2
    if expected_answer == given_answer:
        print(f"You were correct! The answer is {given_answer}")
    else:
        print(
            f"your answer is wrong it should be {expected_answer} instead of {given_answer}"
        )
elif operation == '**':
    expected_answer = nums1 ** nums2
    if expected_answer == given_answer:
        print(f"You were correct! The answer is {given_answer}")
    else:
        print(
            f"your answer is wrong it should be {expected_answer} instead of {given_answer}"
        )
else:
    print("Invalid Operation, please check your input and try again")