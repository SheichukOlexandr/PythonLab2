import math

def sum_with_precision(x, a, epsilon):
  """
  Обчислює значення суми з заданою точністю.

  Args:
    x: Дійсне число.
    a: Дійсне число.
    epsilon: Точність.

  Returns:
    Кортеж (значення суми, кількість врахованих доданків).
  """

  s = 0
  k = 1
  term = math.exp(-k) / (a ** (2 * k) + math.factorial(k))

  while abs(term) > epsilon:
    s += term
    k += 1
    term = math.exp(-k) / (a ** (2 * k) + math.factorial(k))

  return s, k

# Зчитати значення x та a з клавіатури
x = float(input("Введіть значення x: "))
a = float(input("Введіть значення a: "))
epsilon = 1e-6

sum, terms = sum_with_precision(x, a, epsilon)

print(f"Сума: {sum}")
print(f"Кількість врахованих доданків: {terms}")
