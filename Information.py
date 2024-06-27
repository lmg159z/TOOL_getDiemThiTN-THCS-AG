



url = "https://baoangiang.com.vn/tra-cuu-diem-thi-vao-lop-10.html?tensbd="

thong_ke = []
nameSchools = {
    "0101": "Trường PTTH Sư Phạm AG",
    "0102": "Trường THPT Long Xuyên",
    "0103": "Trường THPT Nguyễn Hiền",
    "0104": "Trường THPT Nguyễn Công Trứ",
    "0106": "Trường THPT Chuyên Thoại Ngọc Hầu",
    "0201": "Trường THPT Vọng Thê",
    "0202": "Trường THPT Nguyễn Văn Thoại",
    "0204": "Trường THPT Nguyễn Khuyến",
    "0301": "Trường THPT Nguyễn Bỉnh Khiêm",
    "0302": "Trường THPT Cần Đăng",
    "0303": "Trường THPT Vĩnh Bình",
    "0401": "Trường THPT Trần Văn Thành",
    "0402": "Trường THPT Thạnh Mỹ Tây",
    "0403": "Trường THPT Châu Phú",
    "0404": "Trường THCS và THPT Bình Long",
    "0405": "Trường THPT Bình Mỹ",
    "0502": "Trường THPT Võ Thị Sáu",
    "0503": "Trường THPT Chuyên Thủ Khoa Nghĩa",
    "0504": "Trường PT DTNT THPT An Giang",
    "0602": "Trường THPT Chi Lăng",
    "0702": "Trường THPT Nguyễn Trung Trực",
    "0704": "Trường THCS và THPT Cô Tô",
    "0801": "Trường THPT An Phú",
    "0803": "Trường THPT Quốc Thái",
    "0901": "Trường THPT Tân Châu",
    "0902": "Trường THPT Nguyễn Sinh Sắc",
    "0903": "Trường THPT Nguyễn Quang Diêu",
    "0904": "Trường THPT Châu Phong",
    "0905": "Trường THPT Vĩnh Xương",
    "1002": "Trường THPT Chu Văn An",
    "1004": "Trường THPT Nguyễn Chí Thanh",
    "1005": "Trường THCS và THPT Phú Tân",
    "1101": "Trường THPT Châu Văn Liêm",
    "1102": "Trường THPT Ung Văn Khiêm",
    "1105": "Trường THPT Nguyễn Hữu Cảnh",
    "1106": "Trường THPT Võ Thành Trinh",
    "1107": "Trường THPT Huỳnh Thị Hưởng"
}

def dict_to_list():
    # Chuyển đổi dictionary thành danh sách các cặp [key, value]
    result = [[key, value] for key, value in nameSchools.items()]
    return result