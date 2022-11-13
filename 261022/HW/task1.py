def oops():
    '''Generate IndexError'''
    message = 'Hello World'
    print(message[len(message)])

def catch_oops():
    '''Catch IndexError from fuction 'oops' '''
    try:
        oops()
    except IndexError:
        print('Function "catch_oops" catch IndexError')

catch_oops()