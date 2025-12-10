import os
def chuanhoaspace(st):
    return (" ".join(st.strip().split()))
def demnguyenam(st):
    dem=0
    a="ueoai"
    for i in st:
        if i in a:
            dem+=1
    return dem
hoa_don_list=[]
while True:
    os.system("cls")
    print("*****CHƯƠNG TRÌNH XỬ LÝ STRING*****")
    print("1. Tính độ dài chuỗi")
    print("2. Xâu đối xứng")
    print("3...")
    print("26. Quản Lý Hóa Đơn: ...")
    print("27. Bài toán thứ 2: ...")
    print("28. Bài toán thứ 3: ...")
    print("39. Bài toán thứ 4: ...")
    print("30. Kết thúc chương trình")
    luachon=(input("nhập để lựa chọn chức năng(1-30): "))
    if not luachon.isdigit():
        print("Lỗi: vui lòng nhập số!")
        input("\nNhấn Enter để tiếp tục...")
        continue
    else:
        luachon=int(luachon)
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
            print("Chuỗi có số lượng nguyên âm: ",demnguyenam(s))
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
            print(f"Chuỗi đã được chuẩn hóa:  '{chuanhoaspace(s)}' ")
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


        case 26:      
            def xet_ma_hd(mahd):
                for hd in hoa_don_list:
                    if mahd == hd["ma"]:
                        return False
                return True
            

            def them_hoa_don():
                print("\n***** Thêm hóa đơn *****")

                while True:
                    print("[nhập 0 để dừng thêm hóa đơn]")
                    ma = input("Nhập mã hóa đơn: ")
                    ma=ma.upper()
                    if ma == "0":
                        print("Kết thúc nhập hóa đơn")
                        input("\nNhấn Enter để tiếp tục...")
                        return
                    if not xet_ma_hd(ma):
                        print("Mã hóa đơn đã tồn tại!\n")
                        continue
                    hd = {"ma": ma, "chi_tiet": []}
                    print("=== Nhập chi tiết hóa đơn ===")

                    while True:
                        ten = input("Nhập tên sản phẩm (0 để dừng): ")
                        if ten == "0":
                            print("dừng!")
                            break

                        ten = (chuanhoaspace(ten).lower()).title()
                        so_luong = int(input("Nhập số lượng: "))
                        don_gia = float(input("Nhập đơn giá: "))

                        ct = {
                            "ten": ten,
                            "so_luong": so_luong,
                            "don_gia": don_gia
                        }

                        hd["chi_tiet"].append(ct)
                        print("Thêm sản phẩm thành công!\n")

                    hoa_don_list.append(hd)
                    print("Thêm hóa đơn thành công!\n")  

            def xem_ds_hoa_don():
                print("---xem danh sách hóa đơn---")
                if not hoa_don_list:
                    print ("chưa có hóa đơn nào cả!")
                    input("\nNhấn Enter để tiếp tục...")
                    return
                # for hd in hoa_don_list:
                #     print(f"Mã: {hd['ma']} | Tên SP: {hd['ten']} | SL: {hd['so_luong']} | Đơn giá: {hd['don_gia']}")   
                # input("\nNhấn Enter để tiếp tục...")

                for hd in hoa_don_list:
                    print(f"\nMã hóa đơn: {hd['ma']}")
                    for ct in hd["chi_tiet"]: 
                        print(f"  {ct['ten']} | SL: {ct['so_luong']} | Giá: {ct['don_gia']}")
                input("\nNhấn Enter để tiếp tục...")
                            
                        
            def tim_hoa_don():
                print("\n***** Tìm hóa đơn theo mã *****")
                ma=input("Nhập mã hóa đơn cần tìm: ")
                ma=ma.upper();
                for hd in hoa_don_list:
                    if hd["ma"] == ma:
                        for ct in hd["chi_tiet"]:
                            print(f" {ct['ten']} | SL: {ct['so_luong']} | Giá {ct['don_gia']}")
                        
                        input("\nNhấn Enter để tiếp tục...")
                        return
                print("không tìm thấy hóa đơn này")

                input("\nNhấn Enter để tiếp tục...")

            def tinh_tien():
                print("\n***** Tính tổng tiền 1 hóa đơn ***** ")
                ma=input("nhập mã hóa đơn cần tính: ")
                ma=ma.upper()
                tong=0;
                for hd in hoa_don_list:
                    if hd["ma"]==ma:
                        for ct in hd["chi_tiet"]:
                            tong+=ct["so_luong"]*ct["don_gia"]
                        print(f"tổng tiền hóa đơn {ma} = {tong}\n")
                        input("\nNhấn Enter để tiếp tục...")
                        return 
                print("không tìm thấy hóa đơn này!")
                input("\nNhấn Enter để tiếp tục...")
            def tinh_doanh_thu():
                tong=0
                for hd in hoa_don_list:
                    for ct in hd["chi_tiet"]:
                        tong+=ct["so_luong"]*ct["don_gia"]
                print(f"doanh thu của ngày hôm nay: {tong} \n")
                input("\nNhấn Enter để tiếp tục...")

            def xoa_hoa_don():
                ma=input("nhập mã hóa đơn cần xóa: ")
                ma=ma.upper()
                for i,hd in enumerate(hoa_don_list):
                    if hd["ma"]==ma:
                        del hoa_don_list[i]
                        print("xóa đơn hàng thành công!")
                    else:
                        print("không tìm thấy hóa đơn!")
                input("\nNhấn Enter để tiếp tục...")
            def them_hang_hd():
                ma=input("Nhập mã hóa đơn cần thêm hàng hóa: ")
                ma=ma.upper()              
                if xet_ma_hd(ma):
                    print ("Hóa đơn không tồn tại! ")
                    input("\nNhấn Enter để tiếp tục...")
                for hd in hoa_don_list: 
                    if hd["ma"]==ma:
                        while True:
                            ten = input("Nhập tên sản phẩm (0 để dừng): ")
                            if ten == "0":
                                print("dừng!")
                                break

                            ten = (chuanhoaspace(ten).lower()).title()
                            so_luong = int(input("Nhập số lượng: "))
                            don_gia = float(input("Nhập đơn giá: "))

                            ct = {
                                "ten": ten,
                                "so_luong": so_luong,
                                "don_gia": don_gia
                            }
                            hd["chi_tiet"].append(ct)
            def menu():
                while True:
                    os.system("cls")
                    print("26. Quản Lý Hóa Đơn Cào Cào")
                    print("===== MENU =====")
                    print("1. Thêm hóa đơn")
                    print("2. Xem danh sách hóa đơn")
                    print("3. Tìm hóa đơn theo mã")
                    print("4. Tính tổng tiền 1 hóa đơn")
                    print("5. Tính doanh thu")
                    print("6. Xóa hóa đơn")
                    print("7. Thêm sản phẩm vào hóa đơn")
                    print("8. EXIT")
                    yeucau=(input("xin nhập lựa chọn của bạn(1-8): "))
                    if not yeucau.isdigit():
                        print("Lỗi: vui lòng nhập số!")
                        input("\nNhấn Enter để tiếp tục...")
                        continue
                    else:
                        yeucau = int(yeucau)
                    os.system("cls")
                    inip=str(yeucau)
                    
                    match yeucau:
                        case 1:
                            them_hoa_don()
                        case 2:
                            xem_ds_hoa_don()
                        case 3:
                            tim_hoa_don()
                        case 4:
                            tinh_tien()
                        case 5:
                            tinh_doanh_thu()
                        case 6:
                            xoa_hoa_don()
                        case 7:
                            them_hang_hd()
                        case 8:
                            print("thoát chương trình...")
                            return 
                        case _:
                            print("Lựa chọn không hợp lệ!")

            menu()
            input("\nNhấn Enter để tiếp tục...")

        case 30:
            print("Thoát chương trình...")
            break
        case _:
            print("Lựa chọn không hợp lệ!")
            input("\nNhấn Enter để tiếp tục...")


