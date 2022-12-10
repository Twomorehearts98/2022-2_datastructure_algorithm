def quick_sort(arr, s, e):
    if s > e: return
    pivot = s
    l, r = s + 1, e
    while l <= r:
        while l <= e and arr[l][1] <= arr[pivot][1]:
            l += 1
        while r > s and arr[r][1] >= arr[pivot][1]:
            r -= 1
        if l > r:
            arr[r], arr[pivot] = arr[pivot], arr[r]
        else:
            arr[r], arr[l] = arr[l], arr[r]
    quick_sort(arr, s, r - 1)
    quick_sort(arr, r + 1, e)


if __name__ == "__main__":
    customer = int(input("고객의 수 : "))

    s = list(map(int, input("서비스를 받는 시간 : ").split()))
    service = [[i] for i in range(customer)]
    for i in range(customer):
        service[i].append(s[i])

    quick_sort(service, 0, customer-1)
    total = []
    for i in range(len(service)):
        if i == 0:
            total.append(service[0][1])
        else:
            total.append(service[i - 1][1] + total[i - 1])
    print("손님들이 기다리는 최소 시간 : {}".format(total[customer-1]))
    for i in range(customer):
        print(service[i][0]+1, end=" ")
