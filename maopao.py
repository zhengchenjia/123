value = [100,190,165,170,155,108,139,175,160,180]

def bubble(value):
    
    # 外部循环：对应走访次数
    # 内部循环：    
    
    for i in range(len(value)-1):
        #flag = False
        for ii in range(len(value)-i-1):
            if value[ii] >value[ii+1]:
                value[ii],value[ii+1] = value[ii+1],value[ii]
                flag = True

        #if flag == False:
        #    break
        print(i)

print(value)
bubble(value)
print(value)




# 对数据本身是否有序非常敏感