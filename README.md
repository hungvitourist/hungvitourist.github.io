## CI/CD Status

| Workflow               | Status |
|-------------------------|--------|
| Deploy Jekyll site      | [![Deploy Jekyll site to Pages](https://github.com/happysmartlight/happysmartlight.github.io/actions/workflows/jekyll.yml/badge.svg)](https://github.com/happysmartlight/happysmartlight.github.io/actions/workflows/jekyll.yml) |
| Jekyll site CI          | [![Jekyll site CI](https://github.com/happysmartlight/happysmartlight.github.io/actions/workflows/Jekyll_CI.yml/badge.svg?branch=master)](https://github.com/happysmartlight/happysmartlight.github.io/actions/workflows/Jekyll_CI.yml) |
| Lighthouse CI           | [![Lighthouse CI](https://github.com/happysmartlight/happysmartlight.github.io/actions/workflows/Lighthouse_CI.yml/badge.svg?branch=master)](https://github.com/happysmartlight/happysmartlight.github.io/actions/workflows/Lighthouse_CI.yml) |
| Pages build deployment  | [![pages-build-deployment](https://github.com/happysmartlight/happysmartlight.github.io/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/happysmartlight/happysmartlight.github.io/actions/workflows/pages/pages-build-deployment) |

<!-- 
Ghi Chú:
bundle exec jekyll build
bundle exec jekyll serve 
-->
# Hùng Vĩ Tourist - Quản lý & Tự động sinh bài viết tour du lịch

## Giới thiệu

Dự án này giúp quản lý và tự động sinh các bài viết tour du lịch cho website Hùng Vĩ Tourist.  
Các tour được lưu trữ dưới dạng file CSV trong thư mục `_data/` và được sinh thành các file Markdown bài viết nhờ script Python sử dụng AI.

---

## Cấu trúc dữ liệu tour

### 1. Các file CSV

- **_data/tour_international.csv**  
  Chứa danh sách tour du lịch quốc tế (mã tour bắt đầu ITxx).

- **_data/tour_domestic.csv**  
  Chứa danh sách tour du lịch nội địa (mã tour bắt đầu DTxx).

#### Các cột trong file CSV

| Tên cột      | Ý nghĩa                                                                 |
|--------------|------------------------------------------------------------------------|
| ma_tour      | Mã tour (ITxx: quốc tế, DTxx: nội địa, ví dụ: IT01, DT01)              |
| title        | Tên tour                                                               |
| layout       | Loại layout (thường là `post`)                                         |
| meta_title   | Tiêu đề SEO cho tour                                                   |
| bigimg       | Đường dẫn ảnh lớn đại diện tour (ưu tiên ảnh đẹp, rõ nét)              |
| image        | Đường dẫn ảnh nhỏ đại diện tour (có thể trùng với bigimg)              |
| tags         | Các từ khóa liên quan, cách nhau bởi dấu phẩy                          |
| categories   | Danh mục tour, ví dụ: `[tours#international]` hoặc `[tours#domestic]`. Có thể thêm:<br>  - `special-offer`: Tour có giá ưu đãi đặc biệt (giảm giá, khuyến mãi, deal tốt)<br>  - `hot`: Tour đang thịnh hành, nhiều khách quan tâm, đặt nhiều |
| transport    | Phương tiện di chuyển (ví dụ: ✈️, 🚌, 🚆)                               |
| location     | Địa điểm chính của tour                                                |
| duration     | Thời lượng tour (ví dụ: 5N4Đ, 3N2Đ)                                    |
| discount     | Phần trăm giảm giá (nếu có, số nguyên, ví dụ: 10, 15)                  |
| price        | Giá tour, định dạng có dấu chấm ngăn cách hàng nghìn (vd: 25.900.000)  |

---

## 2. Script sinh bài viết tự động

**Script:**  
`_data/script-gen-tour-md.py`

### Chức năng:
- Đọc dữ liệu từ hai file CSV trên.
- Xóa các file markdown cũ (bắt đầu bằng ITxx hoặc DTxx) trong thư mục `_posts`.
- Sinh nội dung bài viết tour tự động bằng AI (OpenAI GPT).
- Log tiến trình ra terminal (đang đọc file nào, gen file nào, % hoàn thành).
- Tạo file Markdown cho từng tour trong thư mục `_posts`.

### Hướng dẫn sử dụng

1. **Cài đặt Python và thư viện openai:**
   ```
   pip install openai
   ```

2. **Lấy API Key OpenAI:**  
   Đăng nhập https://platform.openai.com/api-keys và copy token.

3. **Export API Key vào biến môi trường:**

   - **Windows (cmd):**
     ```
     set OPENAI_API_KEY=sk-xxxxxx
     ```
   - **PowerShell:**
     ```
     $env:OPENAI_API_KEY="sk-xxxxxx"
     ```
   - **Linux/macOS:**
     ```
     export OPENAI_API_KEY=sk-xxxxxx
     ```

4. **Chạy script:**
   ```
   python _data/script-gen-tour-md.py
   ```

5. **Kết quả:**  
   Các file Markdown bài viết tour sẽ được tạo trong thư mục `_posts/`.

---

## Lưu ý

- Đường dẫn ảnh trong CSV là đường dẫn nội bộ, cần đảm bảo file ảnh tồn tại đúng vị trí.
- Nếu muốn dùng ảnh online, thay thế bằng link ảnh công khai (https://...).
- Không để trống các trường quan trọng như `ma_tour`, `title`, `price`.
- Khi cập nhật tour mới, chỉ cần thêm vào file CSV và chạy lại script.

---

## Hướng dẫn sử dụng Docker để chạy Jekyll local

### 1. Build image Jekyll

Bạn cần có file `Dockerfile` phù hợp (cài Ruby, Bundler, Jekyll...).  
Sau đó build image với tên `jekyll-hungvitourist`:

```sh
docker build -t jekyll-hungvitourist .
docker compose up
docker exec -it hungvitourist-web bash
docker compose down
```

**Mọi thắc mắc vui lòng liên hệ quản trị viên website (bangnguyendev@outlook.com hoặc 0784.140494) để được hỗ trợ.**