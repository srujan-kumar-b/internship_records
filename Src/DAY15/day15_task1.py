import random

trials = 1000

count_sum_7 = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("Total Trials:", trials)
print("Number of times sum = 7:", count_sum_7)
print("Experimental Probability:", experimental_probability)

theoretical_probability = 6 / 36
print("Theoretical Probability:", theoretical_probability)