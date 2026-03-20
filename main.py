students = [("佐藤", 90), ("田中", 72), ("鈴木", 85), ("高橋", 60)]

total = 0

print("成績判定ツール")
print("------------------")

for name, score in students:
    total += score

    if score >= 90:
        grade = "A"
        result = "合格"
    elif score >= 80:
        grade = "B"
        result = "合格"
    else:
        grade = "C"
        result = "不合格"

    print(f"{name}: {score}点 - {result} / 評価: {grade}")

average = total / len(students)

print("------------------")
print(f"平均点: {average}")