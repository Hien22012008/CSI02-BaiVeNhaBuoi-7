def count_third_largest(arr):
    #Sắp xếp dãy số giảm dần
    arr.sort(reverse = True)

    #Tìm phând tử lớn thứ ba
    if len(arr) >= 3:
        third_largest = arr[2]
    else:
        return 0
    
    #Đếm số lần xuất hiện của phần tử lớn thứ ba
    count = arr.count(third_largest)
    return count

arr = [3, 2, 1, 5, 4, 7, 6, 6, 5]
res = count_third_largest(arr)

print(f"Số lần xuất hiện của phần tử lớn thứ ba là: {res}")