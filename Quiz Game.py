score =0

question =[
    ("Capital of Bangladesh ?","dhaka"),
    ("3 + 5 = ?","8"),
    ("python is a programing language (yes/no) ?","yes")
]

for q , ans in question:
    user = input(q + " ")
    if user.lower() == ans:
        score += 1
    print("Score:", score, "/", len(question))