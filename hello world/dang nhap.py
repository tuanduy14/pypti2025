import getpass
import os

# Đường dẫn đến tệp lưu trữ thông tin người dùng
USER_DATA_FILE = 'users.txt'


def load_users():
    """Tải danh sách người dùng từ tệp."""
    users = {}
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            for line in f:
                username, password = line.strip().split(',')
                users[username] = password
    return users


def save_user(username, password):
    """Lưu thông tin người dùng vào tệp."""
    with open(USER_DATA_FILE, 'a') as f:
        f.write(f'{username},{password}\n')


def register():
    """Chức năng đăng ký người dùng."""
    users = load_users()
    username = input("Nhập tên người dùng: ")

    if username in users:
        print("Tên người dùng đã tồn tại. Vui lòng chọn tên khác.")
        return

    password = getpass.getpass("Nhập mật khẩu: ")
    save_user(username, password)
    print("Đăng ký thành công!")


def login():
    """Chức năng đăng nhập người dùng."""
    users = load_users()
    username = input("Nhập tên người dùng: ")

    if username not in users:
        print("Tên người dùng không tồn tại.")
        return

    password = getpass.getpass("Nhập mật khẩu: ")

    if users[username] == password:
        print("Đăng nhập thành công!")
    else:
        print("Mật khẩu không đúng.")


def main():
    while True:
        print("\nChọn chức năng:")
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("3. Thoát")
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()