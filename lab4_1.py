weight, max_score, std_score = [], [], []

nums = input("Enter weights: ")
weight.extend(map(int, nums.split()))

max_nums = input("Enter max scores: ")
max_score.extend(map(int, max_nums.split()))

std_nums = input("Enter student scores: ")
std_score.extend(map(int, std_nums.split()))

weighted_score = sum((std_score[i] / max_score[i]) * weight[i] for i in range(len(weight)))

print("Final weighted score is:", weighted_score)
