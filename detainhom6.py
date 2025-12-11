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
        case 10:
            print("10. nén chuỗi")
            s = input("Nhập: ")
            kq = ""
            dem = 1
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    dem += 1
                else:
                    kq += s[i-1] + str(dem)
                    dem = 1
            kq += s[-1] + str(dem)
            print(kq)
            input("\nNhấn Enter để tiếp tục...")
        
        case 11:
            print("11. nén chuỗi(vd: a5)")
            s = input("Nhập: ")
            kq = ""
            i = 0
            while i < len(s):
                ch = s[i]
                i += 1
                so = ""
                while i < len(s) and '0' <= s[i] <= '9':
                    so += s[i]
                    i += 1
                so = int(so)
                for _ in range(so):
                    kq += ch
            print(kq)
            input("\nNhấn Enter để tiếp tục...")
        case 12:
            print("12. tách họ tên")
            s = input("Nhập họ tên: ")
            # bỏ trắng dư
            tmp = ""
            truoc = ' '
            for ch in s:
                if ch != ' ':
                    tmp += ch
                else:
                    if truoc != ' ':
                        tmp += ' '
                truoc = ch
            if tmp[0] == ' ':
                tmp = tmp[1:]
            if tmp[-1] == ' ':
                tmp = tmp[:-1]
            # tách
            ds = []
            t = ""
            for ch in tmp:
                if ch != ' ':
                    t += ch
                else:
                    ds.append(t)
                    t = ""
            ds.append(t)
            if len(ds) == 1:
                ho = ""
                tendem = ""
                ten = ds[0]
            elif len(ds) == 2:
                ho = ds[0]
                tendem = "" 
                ten = ds[1]
            else:
                ho = ds[0]
                ten = ds[-1]
                tendem = " ".join(ds[1:-1])

            print("Họ:", ho)
            print("Tên đệm:", tendem)
            print("Tên:", ten)
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
                    print("(Thắng)")
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
        case 27:
            
            ds_sinhvien = []
            def chuan_hoa_ten(ten):
                ten = ten.strip()
                phan = ten.split()
                ten = " ".join(phan)
                ten = ten.title()
                return ten

            def kiem_tra_ma_sv(ma):
                if len(ma) < 3:
                    return False
                if ma[0:2].upper() != "SV":
                    return False
                for ch in ma[2:]:
                    if ch < '0' or ch > '9':
                        return False
                return True

            def them_sinh_vien():
                print("\n=== THÊM SINH VIÊN ===")
                ma = input("Nhập mã sinh viên (SV + số): ")

                if not kiem_tra_ma_sv(ma):
                    print("Mã sinh viên không hợp lệ!")
                    return

                ten = input("Nhập họ tên sinh viên: ")
                ten = chuan_hoa_ten(ten)

                ds_sinhvien.append({
                    "ma": ma.upper(),
                    "ten": ten
                })

                print("Thêm sinh viên thành công!")
                input("\nenter để tiếp tục...")

            def xem_danh_sach():
                print("\n=== DANH SÁCH SINH VIÊN ===")

                if len(ds_sinhvien) == 0:
                    print("Không có sinh viên!")
                    input("\nenter để tiếp tục...")
                    return

                print("{:<10} | {:<30}".format("Mã SV", "Họ và tên"))
                print("-" * 45)

                for sv in ds_sinhvien:
                    print("{:<10} | {:<30}".format(sv["ma"], sv["ten"]))
                input("\nenter để tiếp tục...")

            def tim_theo_ten():
                print("\n=== TÌM SINH VIÊN THEO TÊN ===")

                if len(ds_sinhvien) == 0:
                    print("Không có sinh viên!")
                    return

                ten_can_tim = input("Nhập tên cần tìm: ").strip().lower()
                tim_thay = False

                for sv in ds_sinhvien:
                    if ten_can_tim in sv["ten"].lower():
                        print(f"- {sv['ma']}: {sv['ten']}")
                        tim_thay = True

                if not tim_thay:
                    print("Không tìm thấy sinh viên!")
                input("\nenter để tiếp tục...")

            def tach_ho_ten_theo_ma():
                print("\n=== TÁCH HỌ TÊN THEO MÃ SINH VIÊN ===")

                if len(ds_sinhvien) == 0:
                    print("Không có sinh viên!")
                    input("\nenter để tiếp tục...")
                    return

                ma = input("Nhập mã sinh viên cần tách tên: ").upper()

                sv_tim = None
                for sv in ds_sinhvien:
                    if sv["ma"] == ma:
                        sv_tim = sv
                        break

                if sv_tim is None:
                    print("Không tìm thấy sinh viên có mã:", ma)
                    return

                ten = sv_tim["ten"]
                phan = ten.split()

                if len(phan) == 1:
                    ho = ""
                    tendem = ""
                    ten_chinh = phan[0]
                elif len(phan) == 2:
                    ho = phan[0]
                    tendem = ""
                    ten_chinh = phan[1]
                else:
                    ho = phan[0]
                    ten_chinh = phan[-1]
                    tendem = " ".join(phan[1:-1])

                print("\n== Kết quả tách tên ==")
                print("Họ      :", ho)
                print("Tên đệm :", tendem)
                print("Tên     :", ten_chinh)
                input("\nenter để tiếp tục...")

            def sinh_vien_ten_dai_nhat():
                print("\n=== SINH VIÊN CÓ TÊN DÀI NHẤT ===")

                if len(ds_sinhvien) == 0:
                    print("Không có sinh viên!")
                    return

                max_sv = ds_sinhvien[0]

                for sv in ds_sinhvien:
                    if len(sv["ten"]) > len(max_sv["ten"]):
                        max_sv = sv

                print(f"→ {max_sv['ma']} | {max_sv['ten']} (độ dài: {len(max_sv['ten'])})")
                input("\nenter để tiếp tục...")

            def menu():
                while True:
                    os.system("cls")
                    print("(Quốc, Quân)")
                    print("\n==============================")
                    print(" CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
                    print("==============================")
                    print("1. Thêm sinh viên")
                    print("2. Xem danh sách sinh viên")
                    print("3. Tìm sinh viên theo tên")
                    print("4. Tách họ - đệm - tên theo mã SV")
                    print("5. Tìm sinh viên có tên dài nhất")
                    print("6. Thoát")
                    print("==============================")

                    chon = input("Chọn chức năng (1-6): ")

                    if chon == "1":
                        them_sinh_vien()
                    elif chon == "2":
                        xem_danh_sach()
                    elif chon == "3":
                        tim_theo_ten()
                    elif chon == "4":
                        tach_ho_ten_theo_ma()
                    elif chon == "5":
                        sinh_vien_ten_dai_nhat()
                    elif chon == "6":
                        print("Thoát chương trình...")
                        break
                    else:
                        print("Lựa chọn không hợp lệ! Vui lòng chọn 1–6.")

            menu()

        case 30:
            print("Thoát chương trình...")
            break
        case _:
            print("Lựa chọn không hợp lệ!")
            input("\nNhấn Enter để tiếp tục...")


