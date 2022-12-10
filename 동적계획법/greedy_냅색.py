def inmybag(n):
    for i in range(weight):
        if i == 0:
            continue
        else:
            if i<product[n][0]


weight = int(input("가방의 무게 : "))
product = {}
bag = [[(),0,0] for i in range(weight+1)]
print("물건이름/kg/가격")
for i in range(weight):
    tmp = input().split(" ")
    product.update({tmp[0]: (int(tmp[1]), int(tmp[2]))})

for i in product:
    inmybag(i)

print("최대무게 : {}".format(bag[weight-1][1]))
print("최대 가격 : {}".format(bag[weight-1][2]))
print("가방에 담긴 물건들 : {}".format(bag[weight-1][0]))
