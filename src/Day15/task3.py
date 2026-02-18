import random

P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05

print("Given:")
print("P(Spam) =", P_spam)
print("P(Ham) =", P_ham)
print("P(Free | Spam) =", P_free_given_spam)
print("P(Free | Ham) =", P_free_given_ham)
print()



P_free = (P_free_given_spam * P_spam) + \
         (P_free_given_ham * P_ham)

print("Step 1: Total Probability of 'Free'")
print("P(Free) =", P_free)
print()


P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("Step 2: Apply Bayes Theorem")
print("P(Spam | Free) =", P_spam_given_free)
print()
print("So if an email contains 'Free',")
print("Probability it is Spam =", round(P_spam_given_free * 100, 2), "%")
print()

trials = 100000
spam_and_free = 0
total_free = 0

for _ in range(trials):

   
    if random.random() < P_spam:
        email_type = "Spam"
    else:
        email_type = "Ham"

   
    if email_type == "Spam":
        contains_free = random.random() < P_free_given_spam
    else:
        contains_free = random.random() < P_free_given_ham

    
    if contains_free:
        total_free += 1
        if email_type == "Spam":
            spam_and_free += 1


experimental_probability = spam_and_free / total_free

print("Experimental P(Spam | Free) =", experimental_probability)
print("Theoretical P(Spam | Free) =", P_spam_given_free)
