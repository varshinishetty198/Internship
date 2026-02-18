import random


p_heads = 1/2
p_six = 1/6
theoretical_independent = p_heads * p_six

print("---- Independent Events ----")
print("Theoretical Probability (Heads AND 6):", theoretical_independent)


trials = 100000
count_success = 0

for _ in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)
    
    if coin == "H" and die == 6:
        count_success += 1

experimental_independent = count_success / trials

print("Experimental Probability:", experimental_independent)
print()



print("---- Dependent Events (Without Replacement) ----")

# Theoretical Probability
p_first_red = 5/10
p_second_red_given_first = 4/9
theoretical_dependent = p_first_red * p_second_red_given_first

print("Theoretical Probability (Both Red):", theoretical_dependent)


trials = 100000
count_both_red = 0

for _ in range(trials):
    bag = ["R"]*5 + ["B"]*5
    first = random.choice(bag)
    bag.remove(first)
    second = random.choice(bag)
    
    if first == "R" and second == "R":
        count_both_red += 1

experimental_dependent = count_both_red / trials

print("Experimental Probability:", experimental_dependent)


