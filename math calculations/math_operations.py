

def basic_operations(x,y):
    if (type(x) == int or type (x) == float) and (type(y) == int or type(y) == float):
        summer = x + y
        difference = x - y
        product = x * y

        quofficient = (x / y) if y!=0 else 'undefined'
        

        return {'add':summer, 'subtract':difference, 'multiply':product, 'divide':quofficient}

    else:
        return "Can't do calculations on inputs with datatypes other than int or float(double)"

def power_operations(base,exponent,**kwargs):
    if (type(base) == int or type (base) == float) and (type(exponent) == int or type(exponent) == float):
        power = base ** exponent

        if 'modulo' in kwargs and (type(kwargs['modulo']) == int or type(kwargs['modulo']) == float):
            power = power % kwargs['modulo']

        return power
    else:
        return "Can't do calculations on inputs with datatypes other than int or float(double)"


def apply_operations(operation_list):
    
    answers = list(map(lambda x:x[0](*x[1]),operation_list))

    return answers
