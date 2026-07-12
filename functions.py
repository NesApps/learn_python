# joe_exp_list = [2100, 2500, 3400]
# tom_exp_list = [200, 300, 500]

# total=0
# for item in joe_exp_list:
#     total = total + item
# print("joe expenses is: ", total)
#
# total=0
# for item in tom_exp_list:
#     total = total + item
# print("tom expenses is: ", total)


def calculate_total(exp):
    total=0
    for item in exp:
        total = total + item
    return total
joe_exp_list = [2100, 2500, 3400]
tom_exp_list = [200, 300, 500]

joe_total= calculate_total(joe_exp_list)
tom_total = calculate_total(tom_exp_list)

print("Joe's total expense is: ", joe_total)
print("Tom's total expense is: ", tom_total)
