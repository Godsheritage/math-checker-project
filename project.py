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
#  Not quite. You guessed 2.0 but the actual answer was 1
operation = input("Enter operation:").lower()
nums1 = (input("Enter first number:"))
nums2 = (input("Enter second number:"))
expected_answer = float(input("Enter expected answer:"))

# ADDITION OPERATION
if operation == 'add':
    if nums1.isnumeric() and nums2.isnumeric():
        correct_answer = int(nums1) + int(nums2)
        if correct_answer == (expected_answer):
            print(f"You were correct! The answer is {expected_answer}")
        else:
            print(
                f"not quite. You guessed {expected_answer}  but the actual answer was {correct_answer}"
            )
    else:
        print("Invalid input. Please try again.")

# MULTIPLICATION OPERATION
elif operation == 'multiply':
    if nums1.isnumeric() and nums2.isnumeric():
        correct_answer = int(nums1) * int(nums2)
        if correct_answer == expected_answer:
            print(f"You were correct! The answer is {expected_answer}")
        else:
            print(
                f"not quiet. you guessed {expected_answer}  but the actual answer was {correct_answer}")
    else:
        print("Invalid input. Please try again.")

# DIVISION OPERATION
elif operation == 'divide':
    if int(nums2) == 0 or not nums2.isnumeric() or not nums1.isnumeric():
        print("Invalid input. Please try again.")
    else:
        correct_answer = int(nums1) / int(nums2)
        if correct_answer == expected_answer:
            print(f"You were correct! The answer is {expected_answer}")
        else:
            print(
                f"not quite. You guessed {expected_answer}  but the actual answer was {correct_answer}"
            )

# SUBTRACTION OPERATION
elif operation == 'subtract':
    if nums1.isnumeric() and nums2.isnumeric():
        correct_answer = int(nums1) - int(nums2)
        if correct_answer == expected_answer:
            print(f"You were correct! The answer is {expected_answer}")
        else:
            print(
                f"not quite. You guessed {expected_answer}  but the actual answer was {correct_answer}"
            )
    else:
        print("Invalid input. Please try again.")


# REMAINDER OPERATION
elif operation == 'remainder':
    if int(nums2) == 0 or not nums2.isnumeric() or not nums1.isnumeric():
        print("Invalid input. Please try again.")
    else:
        correct_answer = int(nums1) % int(nums2)
        if correct_answer == expected_answer:
            print(f"You were correct! The answer is {expected_answer}")
        else:
            print(
                f"not quite. You guessed {expected_answer}  but the actual answer was {correct_answer}"
            )

# EXPONENT OPERATION
elif operation == 'exponent':
    if nums1.isnumeric() and nums2.isnumeric():
        correct_answer = int(nums1) ** int(nums2)
        if correct_answer == expected_answer:
            print(f"You were correct! The answer is {expected_answer}")
        else:
            print(
                f"not quite. You guessed {expected_answer}  but the actual answer was {correct_answer}"
            )
    else:
        print("Invalid input. Please try again.")

# IF OPERATION IS NOT DEFINED
else:
    print("Invalid Operation, please check your input and try again")


# SHOULD I MAKE A TYPE CHECK FOR THE EXPECTED ANSWER TO MAKE SURE IT IS ALSO A FLOAT?
