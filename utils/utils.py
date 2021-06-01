def somente_numeros(string):
    import re
    return re.findall(r'\d+', string)[0]
