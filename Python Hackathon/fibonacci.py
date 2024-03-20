# Functions & Fibonacci Sequence
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.



# Your program should:

# Ask the user to input the value of n.
# Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# Print the generated Fibonacci sequence.

def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n using iteration.

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
  if n <= 1:
    return n
  else:
    a, b = 0, 1   #initializes two variables, a and b, with the first two Fibonacci numbers (0 and 1)
    for _ in range(2, n + 1): # Loop to generate the sequence
      c = a + b
      a, b = b, c
    return b # Generates the Fibonacci sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = []
for i in range(num_terms): #
  fibonacci_sequence.append(fibonacci(i))

# Print the Fibonacci sequence
print(fibonacci_sequence)