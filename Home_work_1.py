# Необходимо написать функцию калькулятор, которая принимает строку состоящую из числа, оператора и второго числа разделенных пробелом. Например ('1 + 1'); Необходимо разделить строку используя str.split(), и проверить является результирующий список валидным.
# a) Если ввод не состоит из 3 элементов, необходимо возбудить исключение FormulaError, которое является пользовательским исключением.
# b) Попытайтесь сконвертировать первое и третье значение ввода к типу float.
# Перехватите любые исключения типа ValueError, которые возникают, и выбросите FormulaError
# c) Если второе значение ввода не является '+', '-', '*', '/' также выбросите FormulaError.
# Если инпут валидный - ф-я должна вернуть результат операции

class FormulaError(Exception):
    pass

def calc(string):
    par = string.split(' ')
    if len(par) != 3:
        raise FormulaError("Formula Error")
    try:
        par[0], par[2] = float(par[0]), float(par[2])
    except Exception as error:
        raise FormulaError("Formula Error")
    if par[1] in ("+", '-', '*', "/"):
        string = " ".join(['par[0]', par[1], 'par[2]'])
        return eval(string)
    else:
        raise FormulaError("Formula Error")


if __name__ == "__main__":
    print(calc(input()))