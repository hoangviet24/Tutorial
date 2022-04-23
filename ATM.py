from random import randint

print("CÂY ATM CHẠY BẰNG CƠM")
print("Lưu ý chỉ rút số chẵn như 50, 100, lớn hơn 10 và bé hơn 1000")

#Mật khẩu
def password():
    password = randint(100000,999999)
    print(password)
    while True:
        main_password = int(input("Vui lòng nhập mã pin: "))
        if main_password == password:
            print("Nhập đúng")
            break
        elif main_password != password:
            print("Sai mã pin. Vui lòng nhập lại.")
            continue
 
def name():
    name = input("Tên bạn là gì: ")
    print("Chào mừng",name.upper(),"Đến với cây ATM")

def money():
    while True:
        
        money = int(input("Số tiền bạn muốn rút: "))

        if money %2 != 0:
            print("Số tiền không hợp lệ")
            continue
        else:
            print("Đây là số tiền bạn rút",money)
            break

#Lập lại để xem người dùng có muốn rút tiền nữa không
def again():
    print("Bạn có muốn rút nữa không")
    print("Y hoặc N")
    user = input()
    if user == "Y" or "y":
        
            while True:
                money = int(input("Số tiền bạn muốn rút: "))

                if money %2 != 0:
                    print("Số tiền không hợp lệ")
                    continue
                else:
                    print("Đây là số tiền bạn rút",money)
                    break
    if user == "N" or "n":
        print("Cảm ơn bạn đã ghé qua")    
def main():
    password()
    name()    
    money()
    again()
if __name__ == "__main__":
    main()

