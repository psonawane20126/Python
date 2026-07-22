import os

# Specify the directory path
path = "/"

# Get and print directory contents
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)