# ACTIVITY 2

# Introduction 
# The last model of the “dy” augmented reality glasses includes three sensors
# which tell you the position of the focus point where the user is staring at.
# The position is represented by three values x, y and z. Your goal is to read
# the coordinates of the point from the sensors and print the point coordinates,
# arranging them according to the (x, y, z) format. 

# Input 
# The input consists of integer values that represent the
# coordinates x, y and z of a 3D point, one by line. 

# Output 
# Print out the 3D point coordinates following this output format: (x, y, z) 

# Example 1 
# Input 3 4 5 
# Output (3, 4, 5) 

# Example 2 
# Input 0 -7831 2323 
# Output (0, -7831, 2323)

x = int(input("x value: "))
y = int(input("y value: "))
z = int(input("z value: "))
print(f"{x}, {y}, {z}")