
def calc(weight,muscle,fat,goal_fat_rate):
    fat_rate=fat/weight
    print("현재 fat rate는 {0}".format(fat_rate))
    x=(fat-goal_fat_rate*weight)/(1-goal_fat_rate)
    print("빼야하는 몸무게는 {0}".format(x))
    print("그 때의 몸무게 {0}".format(weight-x))
    return x

hw_amount=str(calc(96.2,41.2,24.6,0.1))+'kg'
print(hw_amount) 