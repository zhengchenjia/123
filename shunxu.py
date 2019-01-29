# 顺序查找


#原始数据 value [3,9,8,2,1,5,4,6,10,7,13,12,11]

#待查找数据　key　６

# location = 0
# key = 6
# value = value [3,9,8,2,1,5,4,6,10,7,13,12,11]
# for i in range(len(value)):
#     if value[i] == key:
#         return i 
#         break
    

def linear(value,key):
    for i in range(len(value)):
        if value[i] == key:
            return i 
    else:
        return -1 #查找失败，返回－１




# 注意else的位置，所有的位置都要遍历完 

if __name__ == '__main__':
    value = [3,9,8,2,1,5,4,6,10,7,13,12,11]
    key = 6
    res = linear(value,key)
    if res == -1:
        print('查找失败')
    else:
        print('查找成功，位置是',res)


















