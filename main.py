def read_entire_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print("Reading entire file:")
        print(content)

def read_file_by_lines(file_path):
    with open(file_path, 'r') as file:
        print("Reading file line by line:")
        for line in file:
            print(line, end='')

def read_file_into_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print("Reading file into list:")
        for line in lines:
            print(line, end='')

def read_line_chunk(file_path, chunk_size):
    with open(file_path, 'r') as file:
        print(f"Reading file in chunks of {chunk_size} bytes:")
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
             print(chunk, end='')

# Codingal Usage
file_path = 'Codingal.txt'

# Create the codingal file
with open(file_path, 'w') as file:
    file.write("Hello World!\nThis is a test file.\n")

# Read the entire file
read_entire_file(file_path)

# Read file line by line
read_file_by_lines(file_path)

# Read file into a list
read_file_into_list(file_path)

# Read file in chunks
read_line_chunk(file_path, 10)