import os
import sys



def create_python_file(directory_path, file_name, description):
    """
    Creates a file with the given name and description inside the specified directory.

    Args:
        directory_path (str): The path to the directory where the file will be created.
        file_name (str): The name of the file to create.
        description (str): The description to write into the file.

    Raises:
        ValueError: If the directory does not exist.
        OSError: If there is an issue creating the file.
    """
    if not os.path.exists(directory_path):
        raise ValueError(f"The directory {directory_path} does not exist.")

    file_path = os.path.join(directory_path, 'Python', file_name+".py")

    print(f"creating a file at this path {file_path}")
    try:
        with open(file_path, 'w') as file:
            file.write("# "+description+"\n")
    except OSError as e:
        print(f"Error creating file '{file_name}': {e}")
        raise


def create_go_file(directory_path, file_name, description):
    """
    Creates a file with the given name and description inside the specified directory.

    Args:
        directory_path (str): The path to the directory where the file will be created.
        file_name (str): The name of the file to create.
        description (str): The description to write into the file.

    Raises:
        ValueError: If the directory does not exist.
        OSError: If there is an issue creating the file.
    """
    if not os.path.exists(directory_path):
        raise ValueError(f"The directory {directory_path} does not exist.")

    file_path = os.path.join(directory_path, 'Go', file_name+".go")

    try:
        with open(file_path, 'w') as file:
            file.write("// "+description+"\n")
    except OSError as e:
        print(f"Error creating file '{file_name}': {e}")
        raise


def main():
    """
    Main function to accept command-line arguments for directory path, file name, and description.
    """

    if len(sys.argv) != 4:
        print("Usage: python script.py <directory_path> <file_name> <description>")
        sys.exit(1)

    directory_path, file_name, description = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        create_python_file(directory_path, file_name, description)
        create_go_file(directory_path, file_name, description)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
