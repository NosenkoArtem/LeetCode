from typing import List
from bisect import bisect_right

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for ch in letters:
            if ch > target:
                return ch
        return letters[0]
    
# с помощью бинарного поиска
# bisect_right(a, t)
# Эта функция из модуля bisect выполняет бинарный поиск. Она находит индекс позиции, куда можно вставить символ t, сохранив порядок в списке a, при этом вставляя его справа от всех таких же символов.
# Фактически, этот индекс указывает на первый элемент, который строго больше t.
# % len(a)
# Оператор остатка от деления реализует логику «кольцевого» списка.
# Если bisect_right возвращает индекс внутри списка (от 0 до len(a) - 1), остаток ничего не меняет.
# Если t больше или равен самому большому элементу в списке, bisect_right вернет индекс, равный len(a). В этом случае len(a) % len(a) даст 0.
class Solution:
    def nextGreatestLetter(self, a: List[str], t: str) -> str:
        return a[bisect_right(a,t)%len(a)]

# в этом решении не надо делать %len(a) для возврата в нулевой элемент
class Solution:
    def nextGreatestLetter(self, a: List[str], t: str) -> str:
        return (a*2)[bisect_right(a,t)]