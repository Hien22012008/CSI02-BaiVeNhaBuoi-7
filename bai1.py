def sort_bubbles(arr):
    n = len(arr)
    #Duyệt qua các phần tử của danh sách
    for i in range(n):
        #So sánh các phần tử kề nhau và hoán đổi vị trí nếu cần
        for j in range(0, n - i - 1):
            #Kiểm tra xem đánh giá của các cửa hàng hiện tại có nhỏ hơn các đánh giá của các cửa hàng tiếp theo ko
            if arr[j][1] < arr[j + 1][1]:
                #Hoán đổi vị trí 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


tea_shops = [
    ("Phuc Long", 4.0),
    ("Tocotoco", 4.0),
    ("Share Tea", 3.5),
    ("Gongcha", 4.5),
    ("Soya", 3.5),
    ("Koi Thé", 4.5),
    ("The Alley", 5.0),
]

sort_bubbles(tea_shops)

for i, (name, rating) in enumerate(tea_shops):
    print(f"{i+1}. {name}: {rating}")
