import re
from collections import defaultdict

def parse_polynomial(poly):
    # Убираем пробелы и преобразуем знаки минусов, чтобы не терять их при разборе
    poly = poly.replace(' ', '').replace('-', '+-')
    
    # Регулярное выражение для поиска коэффициентов и степеней
    pattern = r'([+-]?\d*)(x\^?\d*)?'
    
    terms = defaultdict(int)
    
    matches = re.findall(pattern, poly)
    
    for coeff, var in matches:
        if var == '':
            power = 0
        elif var == 'x':
            power = 1
        else:
            power = int(var.split('^')[-1])
        
        if coeff in ('+', '-'):
            coeff += '1'
        
        terms[power] += int(coeff or 1)
    
    return terms

def add_polynomials(poly1, poly2):
    # Разбираем многочлены
    terms1 = parse_polynomial(poly1)
    terms2 = parse_polynomial(poly2)
    
    # Объединяем коэффициенты одноименных членов
    result_terms = defaultdict(int)
    
    for power in set(terms1.keys()).union(terms2.keys()):
        result_terms[power] = terms1[power] + terms2[power]
    
    # Формируем итоговый многочлен
    result = []
    for power in sorted(result_terms.keys(), reverse=True):
        coeff = result_terms[power]
        if coeff == 0:
            continue
        if power == 0:
            result.append(f'{coeff:+d}')
        elif power == 1:
            result.append(f'{coeff:+d}x')
        else:
            result.append(f'{coeff:+d}x^{power}')
    
    # Соединяем члены в строку и убираем знак плюс у первого члена
    result_str = ''.join(result)
    if result_str.startswith('+'):
        result_str = result_str[1:]
    
    return result_str + ' = 0'

# Пример использования
poly1 = "2x^2 + 4x + 5 = 0"
poly2 = "5x^3 - 3x^2 - 12 = 0"

result = add_polynomials(poly1, poly2)
print(result)
