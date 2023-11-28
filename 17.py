dictionary1 = {"red":"красный", "blue":"синий"}
dictionary2 = {"green":"зеленый", "yellow":"желтый"}

dictionary3 = {**dictionary1, **dictionary2}
print(dictionary3)