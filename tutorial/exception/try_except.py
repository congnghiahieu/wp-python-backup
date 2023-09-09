# Cách sử dụng
# try:
# except someKindOfSpecificErr:
# except:
# else:
# finally:

# Nếu biết được và muốn bắt được loại lỗi cụ thể thì ta sử dụng except với tên loại lỗi cụ thể. Có thể dùng "as" để đổi tên lỗi
# Nếu không biết được sẽ xảy ra lỗi gì thì chỉ cần except:
# Khi thực hiện thành công khối try thì sẽ đi vào khối else (nếu có định nghĩa khối else)
# Khối finally sẽ được thực hiện bất kể thành công hay không. Ví dụ nếu mở file và đọc file thành công hay có lỗi thì sau cùng vẫn phải đóng file lại

# Chú ý:
# Nếu biến được định nghĩa trong khối try thì kể cả trong khối except hay finally đều có thể đọc được
# Tên các lỗi trong python đều là "Error" không phải "Exception" (vẫn tồn tại Exception)

# 1 khối except có thể bắt được nhiều loại lỗi bằng cách sử dụng (Error1, Error2)
# VD: except (ZeroDivisionError, EOFError, ValueError, NameError) as err:

try:
    result = 2 / 1
except (ZeroDivisionError, ValueError) as err:
    print(err)
    print("Lỗi chia cho 0")
except EOFError as err:
    print(err)
    print("Lỗi đọc hết file")
except:
    print("Lỗi không xác định")
else:
    print(
        "Thực hiện tất cả các đoạn mã ở trong khối try thành công (không exception) thì thực hiện đoạn code trong khối else"
    )
finally:
    print(result)
    print(
        "Kể cả thực hiện thành công hay có exception thì đều thực hiện khối finally này"
    )

print(result)  # 1
