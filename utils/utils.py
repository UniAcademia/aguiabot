def somente_numeros(string):
    import re
    return re.sub("[^0-9]", "", string)
