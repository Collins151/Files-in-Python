def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1.\n")
            file.write("12345\n")
            file.write("Another line with some numbers: 98765\n")
        print("File created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except Exception as e:
        print(f"Error reading file: {e}")

# File Appending
def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Additional line 1.\n")
            file.write("67890\n")
            file.write("One more line for appending.\n")
        print("File appended successfully.")
    except Exception as e:
        print(f"Error appending file: {e}")

# Error Handling
def main():
    create_file()
    read_file()
    append_file()

if __name__ == "__main__":
    main()