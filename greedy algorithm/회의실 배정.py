def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num[2] < pivot:
            lesser_arr.append(num)
        elif num[2] > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

if __name__ == "__main__":
    n = int(input("강의실 개수 : "))
    lst = []
    print("강의번호 시작시간 종료시간")
    t = 0
    for i in range(n):
        classes = list(map(int, input().split()))
        lst.append(classes)
    lst = quick_sort(lst)
    tmp = []
    etime = 0
    for i in range(n):
        if i == 0:
            etime = lst[0][2]
            tmp.append(lst[0][0])
        else:
            if lst[i][1]>etime:
                etime = lst[i][2]
                tmp.append(lst[i][0])
    print("배정된 최대의 강의실 개수 : {}\n배정된 강의실 번호:{}".format(len(tmp), tmp))