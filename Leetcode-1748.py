nums = list(map(int,input().split()))
son = 0
mantiq = True
for i in range(len(nums)):
    mantiq = True
    for j in range(len(nums)):
        if nums[i] == nums[j] and i!=j:
            mantiq = False
            break
    if mantiq:
        son+= int(nums[i])
print(son)