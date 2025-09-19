max_score, std_score = [], []
# weight=[]
# nums = input("Enter weights: ")
nums = input("Enter weight: ")
weight=list(map(int, nums.split()))

max_nums = input("Enter max scores: ")
max_score=list(map(int, max_nums.split()))

std_nums = input("Enter student scores: ")
std_score=list(map(int, std_nums.split()))

def calc_weighted_score():
    if(weight==0):
        weight = (max_score/3)*len(max_score)
    weighted_score = sum((std_score[i] / max_score[i]) * weight[i] for i in range(len(weight)))
    return weighted_score
# final_score= calc_weighted_score
print("Final weighted score is:", calc_weighted_score())

