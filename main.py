students = []

count = int(input("何人分の成績を入力しますか？: "))

for _ in range(count):
    name = input("名前を入力してください: ")
    score = int(input("点数を入力してください: "))
    students.append((name, score))

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
print(f"平均点: {average:.2f}")

print("------------------")
print("合格者一覧")

for name, score in students:
    if score >= 80:
        print(f"{name}: {score}点")