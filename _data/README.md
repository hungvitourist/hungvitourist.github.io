
# Hướng dẫn sử dụng dữ liệu & script tự động sinh bài viết cho Hùng Vĩ Tourist

Website Hùng Vĩ Tourist sử dụng các file CSV để quản lý danh sách tour du lịch và dịch vụ, đồng thời cung cấp script Python để tự động sinh các bài viết markdown cho website.

---

## 1. Các file dữ liệu CSV

### a. Tour du lịch

- **tour_international.csv**: Danh sách tour du lịch quốc tế (mã tour bắt đầu ITxx hoặc QTxx).
- **tour_domestic.csv**: Danh sách tour du lịch nội địa (mã tour bắt đầu DTxx hoặc NDxx).

#### Định nghĩa các cột


| Tên cột      | Ý nghĩa                                                                 |
|--------------|------------------------------------------------------------------------|
| ma_tour      | Mã tour (ITxx: quốc tế, DTxx: nội địa, ví dụ: IT01, DT01)              |
| title        | Tên tour                                                               |
| layout       | Loại layout (thường là `post`)                                         |
| meta_title   | Tiêu đề SEO cho tour                                                   |
| bigimg       | Đường dẫn ảnh lớn đại diện tour (ưu tiên ảnh đẹp, rõ nét)              |
| image        | Đường dẫn ảnh nhỏ đại diện tour (có thể trùng với bigimg)              |
| tags         | Các từ khóa liên quan, cách nhau bởi dấu phẩy                          |
| categories   | Danh mục tour, ví dụ: `[tours#international]` hoặc `[tours#domestic]`  |
| transport    | Phương tiện di chuyển (ví dụ: ✈️, 🚌, 🚆)                               |
| location     | Địa điểm chính của tour                                                |
| duration     | Thời lượng tour (ví dụ: 5N4Đ, 3N2Đ)                                    |
| discount     | Phần trăm giảm giá (nếu có, số nguyên, ví dụ: 10, 15)                  |
| price        | Giá tour, định dạng có dấu chấm ngăn cách hàng nghìn (vd: 25.900.000)  |

Có thể thêm:<br>
- `special-offer`: Tour có giá ưu đãi đặc biệt<br>
- `hot`: Tour đang thịnh hành, nhiều khách quan tâm |


#### Ví dụ một dòng dữ liệu

```
IT01,"Tour Nhật Bản Mùa Hoa Anh Đào",post,"Nhật Bản Mùa Hoa Anh Đào","/img/tours/international/22072.jpg","/img/tours/international/22072.jpg","tour nhật bản, hoa anh đào, du lịch nhật bản, tour quốc tế, tour tokyo, tour kyoto, tour osaka","[tours#international]","✈️","Tokyo - Kyoto - Osaka","5N4Đ",8,"32.900.000"
```

---

### b. Dịch vụ (service)

- **service_list.csv**: Danh sách các dịch vụ của Hùng Vĩ Tourist.

#### Định nghĩa các cột

| Tên cột      | Ý nghĩa                                                                 |
|--------------|------------------------------------------------------------------------|
| ma_service   | Mã dịch vụ (ví dụ: SV_CONS01, SV_HOTEL01, SV_CAR01, ...)               |
| title        | Tên dịch vụ                                                            |
| layout       | Loại layout (thường là `post`)                                         |
| meta_title   | Tiêu đề SEO cho dịch vụ                                                |
| bigimg       | Đường dẫn ảnh lớn đại diện dịch vụ                                     |
| image        | Đường dẫn ảnh nhỏ đại diện dịch vụ                                     |
| tags         | Các từ khóa liên quan, cách nhau bởi dấu phẩy                          |
| categories   | Danh mục dịch vụ, ví dụ: `[service#consult]`, `[service#hotel]`, ...   |
| transport    | (Để trống)                                                             |
| location     | Phạm vi dịch vụ (thường là "Toàn thế giới")                            |
| duration     | (Để trống)                                                             |
| discount     | (Để trống)                                                             |
| price        | (Để trống)                                                             |

#### Quy ước mã dịch vụ

- **SV_CONSxx**: Tư vấn du lịch (`service#consult`)
- **SV_HOTELxx**: Đặt khách sạn (`service#hotel`)
- **SV_CARxx**: Thuê xe du lịch (`service#carRental`)
- **SV_PKGxx**: Tour trọn gói (`service#packageTour`)
- **SV_EVENTxx**: Tổ chức sự kiện (`service#event`)
- **SV_PARTNERxx**: Hợp tác & đối tác (`service#partner`)
- **SV_OTHERxx**: Dịch vụ khác (`service#other`)

---

## 2. Hướng dẫn sử dụng script sinh file Markdown từ CSV

### a. Sinh bài viết tour

1. Đảm bảo đã cài đặt Python và thư viện `openai`.
2. Đặt file `tour_international.csv` và `tour_domestic.csv` vào thư mục `_data`.
3. Đặt script `script-gen-tour-md.py` vào cùng thư mục.
4. Xuất token API OpenAI của bạn (lấy tại https://platform.openai.com/api-keys) và export vào biến môi trường:

**Trên Windows (cmd):**
```
set OPENAI_API_KEY=sk-xxxxxx
```
**Trên PowerShell:**
```
$env:OPENAI_API_KEY="sk-xxxxxx"
```
**Trên Linux/macOS:**
```
export OPENAI_API_KEY=sk-xxxxxx
```

5. Chạy script:
```
python script-gen-tour-md.py
```

Script sẽ tự động đọc cả hai file CSV, log tiến trình ra terminal và sinh các file markdown vào thư mục `_posts`.

---

### b. Sinh bài viết dịch vụ

1. Đảm bảo đã cài đặt Python và thư viện `openai`.
2. Đặt file `service_list.csv` vào thư mục _data.
3. Đặt script `script-gen-service-md.py` vào cùng thư mục.
4. Đảm bảo đã export biến môi trường `OPENAI_API_KEY` như hướng dẫn trên.
5. Chạy script:
```
python script-gen-service-md.py
```

Script sẽ tự động đọc file CSV dịch vụ, log tiến trình ra terminal và sinh các file markdown vào thư mục `_posts`.

---

## 3. Lưu ý

- Đường dẫn ảnh là đường dẫn nội bộ trên website, cần đảm bảo file ảnh tồn tại đúng vị trí.
- Nếu muốn dùng ảnh online, thay thế bằng link ảnh công khai (https://...).
- Giá tour nên đặt trong dấu ngoặc kép `"..."` để tránh lỗi khi đọc CSV.
- Không để trống các trường quan trọng như `ma_tour`, `title`, `price` (đối với tour) hoặc `ma_service`, `title` (đối với dịch vụ).
- Khi cập nhật tour hoặc dịch vụ mới, chỉ cần thêm vào file CSV và chạy lại script.

---

**Mọi thắc mắc vui lòng liên hệ quản trị viên website (bangnguyendev@outlook.com) để được hỗ trợ.**
