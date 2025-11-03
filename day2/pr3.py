def read_file_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line


def filter_lines(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line


def strip_lines(lines):
    for line in lines:
        yield line.strip()


def number_lines(lines):
    for i, line in enumerate(lines):
        yield f"{i}: {line}"


def chunk_lines(lines, chunk_size):
    chunk = []
    for line in lines:
        chunk.append(line)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk: 
        yield chunk



# Create a sample file for testing
sample_content = """
Hello World
Python Programming
This is a test
Python is awesome
Final line
"""


# Write sample file
with open('sample.txt', 'w') as f:
    f.write(sample_content)


# Read file using generator
print("All lines:")
for line in read_file_lines('sample.txt'):
    print(repr(line))


# Chain generators - filter and strip
print("\nFiltered lines (containing 'Python'):")
lines = read_file_lines('sample.txt')
filtered = filter_lines(lines, 'Python')
stripped = strip_lines(filtered)
for line in stripped:
    print(line)


# Number lines
print("\nNumbered lines:")
lines = read_file_lines('sample.txt')
stripped = strip_lines(lines)
numbered = number_lines(stripped)
for line in numbered:
    print(line)


# Chunk lines
print("\nChunked lines (size 2):")
lines = read_file_lines('sample.txt')
stripped = strip_lines(lines)
chunked = chunk_lines(stripped, 2)
for chunk in chunked:
    print(chunk)