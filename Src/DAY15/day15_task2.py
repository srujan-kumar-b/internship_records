import random

trials = 100000
count_success = 0

for _ in range(trials):
    coin = random.choice(["H", "T"])

    die = random.randint(1, 6)
    
    if coin == "H" and die == 6:
        count_success += 1

experimental_probability = count_success / trials

print("Independent Event:")
print("Experimental Probability (Heads AND 6):", experimental_probability)
print("Theoretical Probability:", 1/12)