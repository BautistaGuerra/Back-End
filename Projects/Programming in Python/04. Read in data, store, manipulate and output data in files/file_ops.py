def read_file(file_name):
    """ Reads in a file."""
    """
    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """

    file = open(file_name)
    file_content = file.read()
    print(file_content)

    return file_content

    raise NotImplementedError()

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list"""
    """
    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """

    file = open(file_name)
    file_list = file.readlines()

    return file_list

    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file."""
    """
    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    first_line = []
    for char in file_contents:
        if char == '\n':
            break
        first_line.append(char)
        
    new_file = open(output_filename, 'w')
    separador = ""
    line = separador.join(first_line)
    new_file.write(line)

    # raise NotImplementedError()


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file"""
    """
    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    file = open(file_name)
    even_lines = []
    for index, line in enumerate(file.readlines()):
        if (index + 1) % 2 == 0:
            even_lines.append(line)
    
    return even_lines

    raise NotImplementedError()

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order"""
    """
    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    file = open(file_name)
    file_list = file.readlines()
    file_reverse = []
    for line in file_list[::-1]:
        file_reverse.append(line)

    return file_reverse

    raise NotImplementedError()


def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()