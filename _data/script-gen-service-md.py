import csv
import os
import re
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

csv_file = "visa_service_list.csv"
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

    🎯 YÊU CẦU NỘI DUNG:
    Viết thành 3 mục rõ ràng:

    1️⃣ **Giới thiệu dịch vụ**
    - 1 đoạn văn 3–4 câu, truyền cảm hứng và cảm xúc.
    - Có emoji phù hợp (2–3 emoji là đủ).
    - Giới thiệu giá trị cốt lõi và lý do khách nên quan tâm.
    - Có call-to-action nhẹ.

    2️⃣ **Lợi ích khi chọn dịch vụ**
    - Liệt kê 3–5 lợi ích chính, dạng bullet (-).
    - Mỗi lợi ích ngắn gọn, dễ đọc, có yếu tố thuyết phục.
    - Có thể gắn với {categories} hoặc {tags} nếu phù hợp.

    3️⃣ **Từ khóa SEO**
    - Viết đúng 5 từ khóa liên quan nhất đến dịch vụ.
    - Ngăn cách bằng dấu phẩy, viết liền trên 1 dòng.
    - Ưu tiên chèn {categories} và {tags} vào từ khóa nếu hợp lý.

    📝 Định dạng output:
    - Xuất ra đúng 3 mục theo thứ tự 1️⃣, 2️⃣, 3️⃣.
    - Không lặp lại yêu cầu, không thêm phần thừa.
    """
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "Bạn là chuyên gia marketing du lịch cao cấp, viết nội dung hấp dẫn, chuẩn SEO và tối ưu chuyển đổi."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content.strip()



# Xóa các file md cũ bắt đầu bằng SVxx
print("🧹 Đang kiểm tra và xóa các file .md cũ (SVxx-*.md) trong thư mục _posts...")
for fname in os.listdir(output_dir):
    if fname.endswith(".md") and fname.startswith("SV"):
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
service_code: {ma_service}
meta-title: {meta_title}
bigimg:
  - "{bigimg}"
image: "{image}"
tags: {tags}
categories: {categories}
location: {location}
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