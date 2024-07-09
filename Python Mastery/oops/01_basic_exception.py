def read_file(file_path: str) -> None:
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"An error occurred while reading the file at {file_path}.")
    except IOError:
        print(f"An error occurred while reading the file at {file_path}.")
    else:
        print('File read successfully.')
        print(content)
    finally:
        print('Execution of programe completed.')

read_file('message.txt')