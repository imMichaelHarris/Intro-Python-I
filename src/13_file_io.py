"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
file = open("foo.txt")
for line in file:
    print(line, end="")
file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
newFile = open("bar.tct", "w")

newFile.write("\nTest \n")
newFile.write("Another \n")
newFile.write("Last one")
newFile.close()

newFile = open("bar.tct", "r")

for line in newFile:
    print(line, end="")
