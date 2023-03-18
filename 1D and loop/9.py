array = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'even', 'odd']
x, y = map(int, input().split())
even_or_odd = ['even' if i%2==0 else 'odd' for i in (x, y)]
print(array[x-1], array[y-1], *even_or_odd)