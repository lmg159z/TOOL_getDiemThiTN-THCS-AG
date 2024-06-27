```
+--------------------------+
| Lê Minh Ghi              |
| github.com/lmg159z       |
+--------------------------+
```

## Project: Lấy điểm thi vào lớp 10 tỉnh An Giang

### Mô tả:

Project này được thiết kế để tự động lấy điểm thi vào lớp 10 của tỉnh An Giang từ website chính thức của tỉnh.

**Mục tiêu:**

* Tự động lấy dữ liệu điểm thi từ website.
* Xuất kết quả ra file CSV.
* Thống kê số lượng thí sinh của từng trường.

### Cấu trúc thư mục:

```
├── GET_MaHoiDongThi
│   └── GET_MHD.py
└── diem_don_vi
    └── 0101_Trường_PTTH_Sư_Phạm_AG.csv
```

### Các file:

#### 1. `index.py`:

* File chính của project.
* Tải dữ liệu từ website theo mã hội đồng thi.
* Xuất kết quả ra file CSV theo từng trường.
* Thống kê số lượng thí sinh của mỗi trường.

**Code:**

* **`index.py`**

#### 2. `Information.py`:

* Chứa thông tin các trường, mã trường, URL của website.
* Chứa danh sách các trường đã lấy điểm thi (thong_ke).

**Code:**

* **`Information.py`**

#### 3. `GET_MaHoiDongThi/GET_MHD.py`:

* Sử dụng để lấy mã hội đồng thi từ website.
* Lưu kết quả vào file CSV.

**Code:**

* **`GET_MaHoiDongThi/GET_MHD.py`**

#### 4. `diem_don_vi/0101_Trường_PTTH_Sư_Phạm_AG.csv`:

* File CSV lưu điểm thi của từng trường.
* Ví dụ: `diem_don_vi/0101_Trường_PTTH_Sư_Phạm_AG.csv`.

### Cách chạy:

1.  **Cài đặt các thư viện:**
    ```bash
    pip install requests beautifulsoup4 tabulate unidecode
    ```

2.  **Chạy file `index.py`:**
    ```bash
    python index.py
    ```

3.  **Chọn option:**

    * **y: Lấy điểm thi theo từng trường**

        ```bash
        Nhập 'y' để lấy từng đơn vị hoặc 'n' để lấy hết: y
        Nhập mã đơn vị: 0101
        Bắt đầu chạy...
        ```

        **Kết quả:**
        * File `diem_don_vi/0101_Trường_PTTH_Sư_Phạm_AG.csv` sẽ được tạo ra, chứa điểm thi của trường PTTH Sư Phạm AG.
        * File `Thong_ke.csv` sẽ được cập nhật, chứa số lượng thí sinh của trường.

    * **n: Lấy điểm thi theo khoảng hoặc toàn bộ**

        ```bash
        Nhập 'y' để lấy từng đơn vị hoặc 'n' để lấy hết: n
        Nhập 'y' để lấy theo khoảng hoặc 'n' để lấy toàn bộ: y
        Nhập mã bắt đầu: 0101
        Nhập mã kết thúc: 0106
        Bắt đầu chạy...
        ```

        **Kết quả:**
        * File `diem_don_vi/` sẽ chứa điểm thi của các trường từ 0101 đến 0106.
        * File `Thong_ke.csv` sẽ được cập nhật, chứa số lượng thí sinh của mỗi trường.

        **Hoặc:**

        ```bash
        Nhập 'y' để lấy từng đơn vị hoặc 'n' để lấy hết: n
        Nhập 'y' để lấy theo khoảng hoặc 'n' để lấy toàn bộ: n
        Bắt đầu chạy...
        ```

        **Kết quả:**
        * File `diem_don_vi/` sẽ chứa điểm thi của tất cả các trường.
        * File `Thong_ke.csv` sẽ được cập nhật, chứa số lượng thí sinh của mỗi trường.

### Lưu ý:

* Website có thể thay đổi cấu trúc, dẫn đến việc code cần được cập nhật.
* Tốc độ lấy dữ liệu phụ thuộc vào tốc độ kết nối mạng và cấu trúc website.
* Có thể thay đổi code để thêm chức năng khác như:
    *  Lấy điểm thi theo số báo danh.
    *  Tìm kiếm thí sinh theo tên.
    *  Xuất kết quả ra file Excel.

### Cải tiến:

*  Sử dụng multiprocessing để tăng tốc độ lấy dữ liệu.
*  Thêm chức năng xử lý lỗi và cảnh báo.
*  Tạo giao diện người dùng thân thiện hơn.


