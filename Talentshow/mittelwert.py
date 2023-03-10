numbers = [3, 5, 2, 8, 1, 9, 4, 6]

# Entferne das Maximum und Minimum
numbers.remove(max(numbers))
numbers.remove(min(numbers))

# Berechne den Mittelwert
mean = sum(numbers) / len(numbers)
mean_round = round(mean, 1)
print("Mittelwert:", mean_round)
