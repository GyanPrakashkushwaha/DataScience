# This is a comment. Comments in R start with the '#' symbol.

# Declare and initialize variables
var1 <- 10  # Integer variable
var2 <- "Hello, World!"  # String variable

# Input/Output
print(paste("Value of var1: ", var1))  # Output
print(paste("Value of var2: ", var2))  # Output

# User input
print("Enter a number:")
num <- as.integer(readline())  # Input

# Selection (IF-THEN)
if(num > var1) {
  print("The number you entered is greater than var1.")
} else {
  print("The number you entered is not greater than var1.")
}

# Iteration (looping)
print("Countdown:")
for(i in seq(num, 1, -1)) {
  print(i)
}
