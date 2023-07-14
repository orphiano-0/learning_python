def dividend(x):
    def divisor(y):
        print(f"{x} divided by {y} = {x / y}")
    return divisor

closure = dividend(20)
closure(5)

def multiplier(n):
    def multiplied_by(m):
        print(f"{n} multiplied by {m} = {n * m}")
    return multiplied_by

times_two = multiplier(2)
times_three = multiplier(3)
times_four = multiplier(4)
# variable multiplied by the parameter
times_three(5)