def main():
    my_file = open('numbers.txt', 'r')

    file_contents = my_file.read()

    my_file.close()

    print(file_contents)

main()