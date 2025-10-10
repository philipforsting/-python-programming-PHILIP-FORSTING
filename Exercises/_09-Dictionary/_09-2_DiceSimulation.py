import random as rnd

def GenerateRolls(number_scores):
    scores = [rnd.randint(1,6) for _ in range(number_scores)]
    return scores

rolls_grade = {grade: i+1 for i, grade in enumerate("123456")}
print(f"rolls_grade: {rolls_grade}")
print(f"rolls_grade.items(): {rolls_grade.items()}")

dice_rolls = GenerateRolls(1000000)
rolls_count = {key: 0 for key in rolls_grade}
print(f"rolls_count first: {rolls_count}")

for dice_roll in dice_rolls:
    for grade, limit in rolls_grade.items():
        if limit == dice_roll :
            rolls_count[grade] += 1

print(f"Grade count {rolls_count}")