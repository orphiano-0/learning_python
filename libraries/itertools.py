# product
from itertools import product
seta = [1, 2]
setb = [3, 4]
product = product(seta,setb, repeat = 2)
print(list(product))

# permutations
from itertools import permutations
seta = [1, 2, 3, 4]
permutations = permutations(seta)
print(list(permutations))

# combinations
from itertools import combinations
seta = [1, 2, 3, 4]
combinations = combinations(seta, 2)
print(list(combinations))