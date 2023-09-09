# while
# break
# continue
# while else

# while, break, continue trong python hoạt động như bình thường
# while else: Khi kết thúc vòng while (khi điều kiện sai) thì sẽ chạy vào đoạn code ở else statement
# Sẽ nhảy vào khối else khi vòng lặp while kết thúc bình thường, tức là kiểm tra điều kiện không còn thoả mãn nữa và kết thúc vòng lặp while
# Nếu khi chạy vòng lặp mà vòng lặp bị kết thúc bằng break thì sẽ không chạy đoạn code trong else

value = 1
while value <= 10:
    value+=1
    if value == 5:
        continue
    print(value)
else:
    print("Value now is equal to ", str(value))