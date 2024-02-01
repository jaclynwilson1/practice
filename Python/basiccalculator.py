def basicCalculator(s):
    result = 0
    functions = ['-', '+']
    fun = ''
    for i in s:
        if i in [' ', ')', '(']:
            continue
        else:
            if i in functions:
                fun = i
            else:
                if fun == '-':
                    result = result - int(i)
                else:
                    result = result + int(i)
    return result

s = "(1+(4+5+2)-3)+(6+8)"
sum = basicCalculator(s)
total = 23
print(sum)

w = "2(3+4)"#will update to advanced calaculator