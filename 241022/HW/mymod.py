def count_lines(file_name):
    '''Count lines in module'''
    my_file = open(file_name, 'r')
    line_quantity = my_file.readlines()
    my_file.close()
    print(f'Your module contain:', len(line_quantity), 'line(s).')

def count_chars(file_name):
    '''Count chars in module'''
    my_file = open(file_name, 'r')   
    my_file_chars = my_file.read()
    my_file.close()
    print(f'Your module contain:', len(my_file_chars), 'char(s).')

def test():
    '''Take name of file and run other two function from this module.'''
    file_name = input('Please input file name with path:')
    count_lines(file_name)
    count_chars(file_name)

if __name__ == '__main__':
    test()