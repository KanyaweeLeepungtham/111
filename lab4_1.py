def calc_weighted_score(weight, max_score, std_score):
    # ถ้าไม่มีการใส่ weight → ให้ถัวเฉลี่ยเท่า ๆ กัน
    if not weight:
        weight = [1] * len(max_score)

    weighted_score = sum((std_score[i] / max_score[i]) * weight[i] for i in range(len(weight)))
    return weighted_score


# รับค่า input
nums = input("Enter weights (กด Enter ถ้าไม่ใส่): ").strip()
weight = list(map(int, nums.split())) if nums else []

max_nums = input("Enter max scores: ")
max_score = list(map(int, max_nums.split()))

std_nums = input("Enter student scores: ")
std_score = list(map(int, std_nums.split()))

# เรียกใช้ฟังก์ชัน
final_score = calc_weighted_score(weight, max_score, std_score)
print("Final weighted score is:", final_score)
