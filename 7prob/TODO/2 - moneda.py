############## MONEDA #############
def lanza():
    return choice(['aguila','sello'])

def resultado(veces):
    values = {}
    for iteration in range(veces):
        moneda = lanza()
        values[moneda] = values.get(moneda, 0) + 1
    return values

print(resultado(5))