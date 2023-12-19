from math_operations import basic_operations,power_operations,apply_operations

#test basic operations
result_basic = basic_operations(10,50)
print("basic operations result: ",result_basic)

#test power operations
result_power = power_operations(2,3)
print("power operations result: ",result_power)

#test power operations with modulo
result_power_modulo = power_operations(2,3, modulo = 5)
print("power operations with modulo result: ",result_power_modulo)

# Test apply_operations
operations = [
    (lambda x, y: x + y, (3, 4)),
    (lambda x, y: x * y, (2, 5)),
]

result_apply = apply_operations(operations)
print("Apply Operations Result:", result_apply)
