"""
Практическая работа №1
Вариант 2: Показания счетчиков
"""

def schetchik(input_string):
    # Разбиваем строку по пробелам
    parts = input_string.strip().split()
    
    if len(parts) < 3:
        return "Ошибка: нужно ввести три части: тип_ресурса дата значение"
    
    resource = parts[0]
    date = parts[1]
    
    try:
        value = float(parts[2])
    except ValueError:
        return "Ошибка: значение должно быть числом"
    
    return f"Тип ресурса: {resource} | Дата: {date} | Значение: {value}"


print("ПРОГРАММА ДЛЯ ПОКАЗАНИЙ СЧЕТЧИКОВ")
print("Вводите строки в формате: тип_ресурса дата значение")
print()
print("Примеры ввода:")
print("  вода 2026.03.13 123.45")
print("  горячая_вода 2026.03.18 75.3")
print()
print("Для выхода введите: выход")
print()

while True:
    user_input = input("> ")
    
    if user_input.lower() in ["выход", "exit", "q"]:
        print("Пока!")
        break
    
    if user_input.strip():
        print(schetchik(user_input))
        print()