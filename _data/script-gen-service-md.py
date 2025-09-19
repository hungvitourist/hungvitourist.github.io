import csv
import os
import re
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

csv_file = "post_news_list.csv"
output_dir = "_posts"

os.makedirs(output_dir, exist_ok=True)

def slugify(text):
    text = text.lower()
    text = re.sub(r"[àáạảãâầấậẩẫăằắặẳẵ]", "a", text)
    text = re.sub(r"[èéẹẻẽêềếệểễ]", "e", text)
    text = re.sub(r"[ìíịỉĩ]", "i", text)
    text = re.sub(r"[òóọỏõôồốộổỗơờớợởỡ]", "o", text)
    text = re.sub(r"[ùúụủũưừứựửữ]", "u", text)
    text = re.sub(r"[ỳýỵỷỹ]", "y", text)
    text = re.sub(r"[đ]", "d", text)
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")

def generate_ai_content(ma_service, title, categories, tags):
    prompt = f"""
    Bạn là chuyên gia marketing du lịch cao cấp, am hiểu SEO và content chuẩn chuyển đổi.
    Hãy viết nội dung quảng bá cho dịch vụ "{title}" của Hùng Vĩ Tourist.

    🎯 YÊU CẦU VIẾT BÀI:

    Bạn là một copywriter chuyên viết blog/news cho công ty du lịch Hung Vi Tourist. 
    Nhiệm vụ: dựa vào metadata sau đây để viết một bài post-news chi tiết, truyền cảm hứng, tối ưu SEO.

    📌 Metadata:
    - Mã dịch vụ: {ma_service}
    - Tiêu đề: {title}
    - Layout: {layout}
    - Meta Title: {meta_title}
    - Ảnh chính: {bigimg}
    - Ảnh preview: {image}
    - Tags: {tags}
    - Categories: {categories}
    - Địa điểm: {location}
    - Phương tiện: {transport}
    - Thời lượng tour: {duration}
    - Giá/khuyến mãi: {price} / {discount}

    📌 Cấu trúc nội dung cần có (yêu cầu bài viết dài, ít nhất 1000 từ):

    1️⃣ **Mở đầu**
    - 1–2 đoạn văn 4–5 câu.
    - Giới thiệu chủ đề theo metadata `{title}`.
    - Gợi cảm xúc, có 2–3 emoji phù hợp.
    - Nhấn mạnh lý do khách nên quan tâm.
    - Call-to-action nhẹ.

    2️⃣ **Nội dung chính**
    - Chia thành 4–6 mục lớn tùy theo loại bài:
    - Nếu {categories} là `tips` → liệt kê mẹo, kinh nghiệm, lưu ý thực tế.
    - Nếu {categories} là `destination` → mô tả địa điểm, khí hậu, văn hóa, trải nghiệm, gợi ý lịch trình.
    - Nếu {categories} là `guide` → viết hướng dẫn từng bước, checklist, quy trình chi tiết.
    - Nếu {categories} là `event` → phân tích xu hướng, lợi ích, bí quyết tổ chức sự kiện du lịch/doanh nghiệp.
    - Nếu {categories} là `policy` → cập nhật quy định, thủ tục, chính sách mới, đưa ví dụ minh họa.
    - Nếu {categories} là `health` → tư vấn sức khỏe, vaccine, bảo hiểm, phòng bệnh khi đi du lịch.
    - Mỗi mục có heading (## hoặc ###), có giải thích dài (3–4 đoạn), xen kẽ bullet list để dễ đọc.

    3️⃣ **Thông tin bổ sung (nếu có)**
    - Chèn {location}, {transport}, {duration}, {price}, {discount} vào nội dung nếu phù hợp.
    - Có thể thêm ví dụ thực tế (tour, chuyến đi, tình huống minh họa).

    4️⃣ **Kinh nghiệm & mẹo hữu ích**
    - Đưa ra 3–5 kinh nghiệm ngắn gọn, dễ áp dụng, liên quan đến {tags}.

    5️⃣ **Kết luận & Call-to-action**
    - Viết 1 đoạn truyền cảm hứng.
    - Nhắc lại Hung Vi Tourist.
    - CTA mạnh mẽ: “Đặt tour ngay hôm nay”, “Liên hệ để được tư vấn”…  

    6️⃣ **Từ khóa SEO**
    - Viết đúng 5 từ khóa liên quan nhất.
    - Ngăn cách bằng dấu phẩy, viết trên 1 dòng.
    - Ưu tiên dùng {tags} và {categories}.

    ⚡ Yêu cầu văn phong:
    - Truyền cảm hứng, giàu cảm xúc, nhưng vẫn chuyên nghiệp.
    - Tối ưu SEO: có tiêu đề phụ, đoạn ngắn, bullet list.
    - Độ dài: ít nhất 1000 từ, có thể 1200–1500 từ cho bài chuyên sâu.
    - Dùng emoji phù hợp, không lạm dụng.
    - Viết đúng ngữ pháp, chính tả tiếng Việt.
    """
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "Bạn là chuyên gia marketing du lịch cao cấp, viết nội dung hấp dẫn, chuẩn SEO và tối ưu chuyển đổi."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content.strip()



# Xóa các file md cũ bắt đầu bằng SV, ND, QT, NEWS, IT, DT
prefixes = ("SV", "ND", "QT", "NEWS", "IT", "DT")
print(f"🧹 Đang kiểm tra và xóa các file .md cũ ({', '.join(prefixes)}-*.md) trong thư mục _posts...")
for fname in os.listdir(output_dir):
    if fname.endswith(".md") and fname[:3].upper().startswith(prefixes):
        os.remove(os.path.join(output_dir, fname))
        print(f"🗑️  Đã xóa: {fname}")

print(f"\n📖 Đang đọc file: {csv_file}")
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = list(csv.DictReader(f))
    total = len(reader)
    for idx, row in enumerate(reader, 1):
        ma_service = row.get("ma_service", "")
        title = row.get("title", "")
        layout = row.get("layout", "post")
        meta_title = row.get("meta_title", title)
        bigimg = row.get("bigimg", "")
        image = row.get("image", "")
        tags = row.get("tags", "")
        categories = row.get("categories", "")
        transport = row.get("transport", "")
        location = row.get("location", "")
        duration = row.get("duration", "")
        discount = row.get("discount", "")
        price = row.get("price", "")

        slug = slugify(title)
        ai_output = generate_ai_content(ma_service, title, categories, tags)
        # Tách phần giới thiệu và keywords
        parts = ai_output.split("\n")

        meta_desc = next((p for p in parts if p.strip()), "")

        # Tìm dòng có từ khóa (có dấu phẩy)
        keywords = next((p for p in parts if "," in p), "")
        # Làm sạch: bỏ ngoặc kép thừa và strip khoảng trắng
        keywords = keywords.replace('"', "'").strip()

        # Ghép lại content
        content = "\n".join(parts[2:]).strip()

        filename = f"{ma_service}-{slug}.md"
        filepath = os.path.join(output_dir, filename)

        percent = int(idx * 100 / total)
        print(f"📝 Đang gen file: {filename} ({idx}/{total}) - {percent}%")

        md_content = f"""---
title: '{title}'
layout: {layout}
service_code: "{ma_service}"
meta-title: "{meta_title}"
bigimg:
  - "{bigimg}"
image: "{image}"
tags: {tags}
categories: {categories}
location: "{location}"
---

## {title}

- 🆔 Mã dịch vụ: **{ma_service}**
- 📍 Phạm vi: **{location}**
- 🏷️ Danh mục: **{categories}**

---

### Giới thiệu dịch vụ

{content}

---

👉 Liên hệ ngay để được tư vấn và sử dụng dịch vụ!

- ☎️ Hotline: (+84) {{{{ site.author.telephone }}}}
- 📧 Email: {{{{ site.author.email }}}}
- 🌐 Website: [hungvitourist.com](https://hungvitourist.com)

"""

        with open(filepath, "w", encoding="utf-8") as post_file:
            post_file.write(md_content)

print(f"✅ Đã xử lý xong file: {csv_file}")