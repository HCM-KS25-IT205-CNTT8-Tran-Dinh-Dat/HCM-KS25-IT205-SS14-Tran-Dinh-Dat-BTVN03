students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

# ================= HELPER FUNCTIONS =================

def validate_score(score_input):
    try:
        score = float(score_input)
        return 0 <= score <= 10
    except:
        return False


def find_student_by_id(student_list, student_id):
    student_id = student_id.strip().upper()

    for i in range(len(student_list)):
        if student_list[i]["student_id"] == student_id:
            return i
    return -1


def get_rank(avg):
    if avg >= 8:
        return "Giỏi"
    elif avg >= 6.5:
        return "Khá"
    elif avg >= 5:
        return "Trung bình"
    else:
        return "Yếu"

# ================= FUNCTIONS =================

def display_students(student_list):
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    for i, s in enumerate(student_list, 1):
        print(f"{i}. Mã: {s['student_id']} | Tên: {s['name']} | Toán: {s['math_score']} | Anh: {s['english_score']}")


def add_student(student_list):
    student_id = input("Nhập mã học viên: ").strip().upper()

    # CHECK TRÙNG MÃ
    for s in student_list:
        if s["student_id"] == student_id:
            print("Mã học viên đã tồn tại!")
            return

    name = input("Nhập tên học viên: ").title()

    math = input("Nhập điểm Toán: ")
    if not validate_score(math):
        print("Điểm không hợp lệ!")
        return

    english = input("Nhập điểm Anh: ")
    if not validate_score(english):
        print("Điểm không hợp lệ!")
        return

    student = {
        "student_id": student_id,
        "name": name,
        "math_score": float(math),
        "english_score": float(english)
    }

    student_list.append(student)
    print("Thêm học viên thành công!")


def update_score(student_list):
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    index = find_student_by_id(student_list, student_id)

    if index == -1:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return

    math = input("Nhập điểm Toán mới: ")
    if not validate_score(math):
        print("Điểm không hợp lệ!")
        return

    english = input("Nhập điểm Anh mới: ")
    if not validate_score(english):
        print("Điểm không hợp lệ!")
        return

    student_list[index]["math_score"] = float(math)
    student_list[index]["english_score"] = float(english)

    print("Cập nhật điểm thành công!")


def evaluate_students(student_list):
    for s in student_list:
        avg = (s["math_score"] + s["english_score"]) / 2
        rank = get_rank(avg)

        print(f"Mã: {s['student_id']} | Tên: {s['name']} | ĐTB: {avg:.2f} | Xếp loại: {rank}")


# ================= MENU =================

menu = """
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====
1. Hiển thị danh sách học viên
2. Thêm học viên mới
3. Cập nhật điểm thi
4. Đánh giá học lực
5. Thoát
"""

while True:
    print(menu)
    choice = input("Chọn chức năng: ")

    if choice == "1":
        display_students(students)

    elif choice == "2":
        add_student(students)

    elif choice == "3":
        update_score(students)

    elif choice == "4":
        evaluate_students(students)

    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ!")