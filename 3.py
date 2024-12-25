# Частотні таблиці з даними
frequency_table = {
    'Outlook': {
        'Yes': {'Sunny': 3, 'Overcast': 4, 'Rain': 2},
        'No': {'Sunny': 2, 'Overcast': 0, 'Rain': 3}
    },
    'Humidity': {
        'Yes': {'High': 3, 'Normal': 6},
        'No': {'High': 4, 'Normal': 1}
    },
    'Wind': {
        'Yes': {'Weak': 6, 'Strong': 3},
        'No': {'Weak': 2, 'Strong': 3}
    }
}

# Ймовірності для цільової змінної
P_Yes = 9 / 14
P_No = 5 / 14

def calculate_probability(attribute, value, target):
    """
    Розрахунок умовної ймовірності P(Attribute=value|Target)
    """
    return frequency_table[attribute][target][value] / sum(frequency_table[attribute][target].values())

# Задані умови
conditions = {
    'Outlook': 'Overcast',
    'Humidity': 'High',
    'Wind': 'Strong'
}

# Обчислення ймовірностей для Yes і No
P_Yes_given_conditions = (
    calculate_probability('Outlook', conditions['Outlook'], 'Yes') *
    calculate_probability('Humidity', conditions['Humidity'], 'Yes') *
    calculate_probability('Wind', conditions['Wind'], 'Yes') *
    P_Yes
)

P_No_given_conditions = (
    calculate_probability('Outlook', conditions['Outlook'], 'No') *
    calculate_probability('Humidity', conditions['Humidity'], 'No') *
    calculate_probability('Wind', conditions['Wind'], 'No') *
    P_No
)

# Нормалізація
P_Total = P_Yes_given_conditions + P_No_given_conditions
P_Yes_final = P_Yes_given_conditions / P_Total
P_No_final = P_No_given_conditions / P_Total

print("Ймовірність гри (Yes):", round(P_Yes_final, 4))
print("Ймовірність гри (No):", round(P_No_final, 4))

# Висновок
if P_Yes_final > P_No_final:
    print("Матч відбудеться.")
else:
    print("Матч не відбудеться.")
