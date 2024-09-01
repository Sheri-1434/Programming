# __name__ and __main__ (special variables)



print("This is a testing module")

# print(__name__)

def test1():
    print('This is a {} variable'.format(__name__))


if __name__ == "__main__":
    test1()