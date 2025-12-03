import os
import modulestring
while True:
    os.system("cls")
    print("*****CHƯƠNG TRÌNH XỬ LÝ STRING*****")
    print("1. Tính độ dài chuỗi")
    print("2. Xâu đối xứng")
    print("3...")
    print("26. Bài toán thứ 1: ...")
    print("27. Bài toán thứ 2: ...")
    print("28. Bài toán thứ 3: ...")
    print("39. Bài toán thứ 4: ...")
    print("30. Kết thúc chương trình")
    luachon=int(input("nhập để lựa chọn chức năng(1-30): "))
    os.system("cls")
    match luachon:
        case 1:         
            print("1. Tính độ dài chuỗi")
            s = input("Nhập chuỗi: ")
            print("Độ dài chuỗi là:", len(s))
            input("\nNhấn Enter để tiếp tục...")
        case 2:
            print("2. Xâu đối xứng")
            s = input("Nhập chuỗi: ")
            if(s==s[::-1]):
                print(f"chuỗi {s} đối xứng")
            else:
                print(f"chuỗi {s} không đối xứng")          
            input("\nNhấn Enter để tiếp tục...")
        case 3:
            print("3. Thống kê nguyên âm")
            s=input("Nhập chuỗi: ")
            print("Chuỗi có số lượng nguyên âm: ",modulestring.demnguyenam(s))
            input("\nNhấn Enter để tiếp tục...")
        case 4:
            print("4. Chuỗi in hoa")
            s = input("Nhập chuỗi: ")
            print("Chuỗi sau khi chuyển sang in hoa:", s.upper())
            input("\nNhấn Enter để tiếp tục...")
        case 5:
            print("5. Chuỗi in thường")
            s = input("Nhập chuỗi: ")
            print("Chuỗi sau khi chuyển sang in hoa:", s.lower())
            input("\nNhấn Enter để tiếp tục...")
        case 6:
            print("6. In hoa ký tự đầu của từ")
            s = input("Nhập chuỗi: ")
            print("Chuỗi sau khi chuẩn hóa :", s.title())
            input("\nNhấn Enter để tiếp tục...")
        case 7:
            print("7. Chuẩn hóa space")
            s = input("Nhập chuỗi: ")
            print(f"Chuỗi đã được chuẩn hóa:  '{modulestring.chuanhoaspace(s)}' ")
            input("\nNhấn Enter để tiếp tục...")
        case 8:
            print("8. Đếm số lần xuất hiện của 1 ký tự")
            s = input("Nhập chuỗi: ")
            a = input("Nhập vào 1 ký tự: ")
            print(f"số lượng ký tự  '{a}'  trong  '{s}'  là: ", s.count(a))

            input("\nNhấn Enter để tiếp tục...")
        case 9:
            print("9. Thay thế ký tự")
            s = input("Nhập chuỗi: ")
            a = input("Nhập vào 1 chuỗi cần thay: ")
            b = input("Nhập vào 1 chuỗi thay thế: ")
            st=s.replace(a, b)
            print("Chuỗi sau khi thay thế: ",st)
            input("\nNhấn Enter để tiếp tục...")
        case 30:
            print("Thoát chương trình...")
            break
        case _:
            print("Lựa chọn không hợp lệ!")
            input("\nNhấn Enter để tiếp tục...")


