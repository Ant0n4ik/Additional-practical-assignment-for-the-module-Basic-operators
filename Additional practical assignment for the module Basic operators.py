def generator_passworld(n):
    digits = list(range(1, 10))
    result = ''
    used_pairs = set()
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            a, b = digits[i], digits[j]
            pair_sum = a + b
            if n % pair_sum == 0 and (a, b) not in used_pairs:
                result += f'{a}{b}'
                used_pairs.add((a, b))
    return result
n = int(input('Введите число от 3 до 20: '))
password = generator_passworld(n)
print(f'Пароль для числа {n}: {password}')