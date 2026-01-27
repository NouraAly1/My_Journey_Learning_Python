# While Loop Example
# This demonstrates a while loop that counts from 1 to 10, but breaks when it reaches 6

# Start counting from 1
i = 1

# Loop while i is less than or equal to 10
while i <= 10:
      i += 1
      # Stop the loop if i equals 6
      if i == 6:
          break
      print(i)

# This message prints after the loop ends
print("the loop has ended")