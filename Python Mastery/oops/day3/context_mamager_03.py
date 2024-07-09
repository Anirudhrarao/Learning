# You can create your own context managers using a class with __enter__ and __exit__ methods.
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Using the custom context manager
with FileManager('example.txt', 'r') as f:
    content = f.read()
    print(content)
# The file is automatically closed here
