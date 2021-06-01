# import my_module
# my_module.func_in_module()


from my_module import *
func_in_module()


s = 'GLOBAL VARIABLE!'


def func():
    print(locals())
    print(globals())
    print(globals()['s'])


func()


def hello(name='Jose'):
    def greet():
        return 'THIS STRING IS INSIDE GREET()'

    def welcome():
        return 'THIS STRING IS INSIDE WELCOME()'

    # print(greet())
    # print(welcome())
    # print('End of hello()')

    if name == 'Jose':
        return greet
    else:
        return welcome
    return 'hello '+name


# print(hello())
my_new_greet = hello
print(my_new_greet()())


def new_decorator(func):
    def wrap_func():
        print('CODE HERE BEFORE EXECUTING FUNC')
        func()
        print('FUNC() HAS BEEN CALLED')
    return wrap_func


print('\n')


@new_decorator
def func_needs_decorator():
    print('THIS FUNCTION IS IN NEED OF A DECORATOR!')

# func_needs_decorator = new_decorator(func_needs_decorator)


func_needs_decorator()
