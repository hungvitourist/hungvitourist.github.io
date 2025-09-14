# Hướng dẫn sử dụng file tour_international.csv và tour_domestic.csv

Hai file `tour_international.csv` và `tour_domestic.csv` lưu trữ danh sách các tour du lịch quốc tế và nội địa, phục vụ cho website Hùng Vĩ Tourist.

## Định nghĩa các cột

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

## Quy ước mã tour

- **ITxx**: Tour quốc tế (International Tour)
- **DTxx**: Tour nội địa (Domestic Tour)

## Ví dụ một dòng dữ liệu

```
IT01,"Tour Nhật Bản Mùa Hoa Anh Đào",post,"Nhật Bản Mùa Hoa Anh Đào","/img/tours/international/22072.jpg","/img/tours/international/22072.jpg","tour nhật bản, hoa anh đào, du lịch nhật bản, tour quốc tế, tour tokyo, tour kyoto, tour osaka","[tours#international]","✈️","Tokyo - Kyoto - Osaka","5N4Đ",8,"32.900.000"
```

## Lưu ý

- Đường dẫn ảnh là đường dẫn nội bộ trên website, cần đảm bảo file ảnh tồn tại đúng vị trí.
- Nếu muốn dùng ảnh online, thay thế bằng link ảnh công khai (https://...).
- Giá tour nên đặt trong dấu ngoặc kép `"..."` để tránh lỗi khi đọc CSV.
- Không để trống các trường quan trọng như `ma_tour`, `title`, `price`.

---

## Hướng dẫn sử dụng script sinh file Markdown từ CSV

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

**Mọi thắc mắc vui lòng liên hệ quản trị viên website để được hỗ trợ.**