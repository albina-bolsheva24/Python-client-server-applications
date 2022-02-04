'''
    3. Определить, какие из слов, поданных на вход программы, невозможно записать в байтовом типе.
    Для проверки правильности работы кода используйте значения: «attribute», «класс», «функция», «type»
'''

VAR_1 = 'attribute'
VAR_2 = 'класс'
VAR_3 = 'функция'
VAR_4 = 'type'

WORDS = [VAR_1, VAR_2, VAR_3, VAR_4]

for word in WORDS:
    try:
        expr_obj = f"b'{word}'"
        eval(expr_obj)
    except SyntaxError:
        print(f'Слово "{word}" невозможно записать в виде байтовой строки')
