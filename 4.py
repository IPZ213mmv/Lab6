# Завантаження та ознайомлення з даними
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Завантаження даних із локального файлу
file_path = 'renfe_small.csv'  # Змініть на шлях до вашого локального файлу
data = pd.read_csv(file_path)

# Перегляд перших рядків та інформації про дані
print(data.head())
print(data.info())

# Попередня обробка даних
# Видалення рядків з пропущеними значеннями
data = data.dropna()

# Перетворення категоріальних змінних на числові
categorical_columns = ['insert_date', 'origin', 'destination', 'train_type', 'fare', 'ticket_type']
data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

# Розділення даних на навчальну та тестову вибірки
# Припустимо, що цільова змінна - 'fare'
X = data.drop('fare', axis=1)
y = data['fare']

# Розділення на навчальну та тестову вибірки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Навчання наївного байєсівського класифікатора
# Ініціалізація та навчання моделі
model = GaussianNB()
model.fit(X_train, y_train)

# Прогнозування на тестових даних
y_pred = model.predict(X_test)

# Оцінка точності моделі
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Точність моделі: {accuracy}')
print('Звіт про класифікацію:')
print(report)
