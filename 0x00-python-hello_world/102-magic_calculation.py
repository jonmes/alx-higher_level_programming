from dis import dis
def magic_calculation(a, b):
    return 98 + (a**b)
print(dis(magic_calculation))
