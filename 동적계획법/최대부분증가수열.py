
def checkandchange():
    for i in range(n):
        for k in range(i+1):
            if data[i] > data[k]:
                if(count[i]<=count[k]):
                    count[i] = count[k]+1
                    via[i] = k

def checklongest(i):
    if via[i] == -1:
        print(data[i], end=" ")
        return
    checklongest(via[i])
    print(data[i], end = " ")


if __name__ == "__main__":
    n = int(input("입력되는 데이터수 : "))
    data = list(map(int, input().split(" ")))
    count = [1 for i in range(n)]
    via = [-1 for i in range(n)]



    checkandchange()
    print(data)
    print(count)
    print(via)
    biggest = 0
    for i in range(n-1, -1, -1):
        if count[biggest]<count[i]:
            biggest = i

    #print(biggest)
    checklongest(biggest)
    #print(data[biggest], end=" ")