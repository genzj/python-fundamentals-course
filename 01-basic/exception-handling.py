# -*- encoding: utf-8 -*-

if __name__ == '__main__':
    a = 'abc'
    # Handle exceptions with a try/except block
    try:
        print(a[1])
        pass
    except IndexError as e:
        print('We get an Index Error')
    except (TypeError, NameError):
        pass                 # Multiple exceptions can be handled together, if required.
    else:                    # Optional clause to the try/except block. Must follow all except blocks
        print("All good!")   # Runs only if the code in try raises no exceptions
    finally:                 # Execute under all circumstances
        print("We can clean up resources here")
