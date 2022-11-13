from modul_1 import sum_of_two

def double_sum(func):
    '''Take result of sum_of_two (function from modul_1) and double it'''
    total_sum = func*2
    return total_sum

if __name__ == '__main__':
    print('This is main modul.')

print(double_sum(sum_of_two(1,2)))