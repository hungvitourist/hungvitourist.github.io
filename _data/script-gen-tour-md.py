import csv
import os
import re
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

csv_files = ["tour_international.csv", "tour_domestic.csv"]
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

def generate_ai_content(ten_tour, dia_diem, gia_tour, duration):
    prompt = f"""
    Hãy viết nội dung cho một bài post du lịch với thông tin sau:
    - Tên tour: {ten_tour}
    - Địa điểm: {dia_diem}
    - Giá: {gia_tour} VND
    - Thời lượng: {duration}

    Yêu cầu:
    1. Viết một đoạn meta description ngắn (150-160 ký tự, ngắn gọn, hấp dẫn, chuẩn SEO).
    2. Liệt kê 5 từ khóa SEO liên quan (cách nhau bởi dấu phẩy).
    3. Viết một đoạn nội dung giới thiệu tour thật cuốn hút, truyền cảm hứng, có emoji, dài khoảng 200-250 từ.
    4. Mô tả hành trình tour từng ngày (ví dụ: Ngày 1, Ngày 2, ...), mỗi ngày 2-3 câu, có emoji minh họa.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()

# Xóa các file md cũ bắt đầu bằng ITxx hoặc DTxx
print("🧹 Đang kiểm tra và xóa các file .md cũ (DTxx-*.md, ITxx-*.md) trong thư mục _posts...")
for fname in os.listdir(output_dir):
    if fname.endswith(".md") and (fname.startswith("IT") or fname.startswith("DT")):
        os.remove(os.path.join(output_dir, fname))
        print(f"🗑️  Đã xóa: {fname}")

# Tiếp tục sinh file như cũ
for csv_file in csv_files:
    print(f"\n📖 Đang đọc file: {csv_file}")
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
        total = len(reader)
        for idx, row in enumerate(reader, 1):
            ma_tour = row.get("ma_tour", "")
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
            ai_output = generate_ai_content(title, location, price, duration)
            parts = ai_output.split("\n")
            meta_desc = next((p for p in parts if p.strip()), "")
            keywords = next((p for p in parts if "," in p), "")
            content = "\n".join(parts[2:]).strip()

            filename = f"{ma_tour}-{slug}.md"
            filepath = os.path.join(output_dir, filename)

            percent = int(idx * 100 / total)
            print(f"📝 Đang gen file: {filename} ({idx}/{total}) - {percent}%")

            md_content = f"""---
title: '{title}'
layout: {layout}
meta-title: {meta_title}
bigimg:
  - "{bigimg}"
image: "{image}"
tags: {tags}
categories: {categories}
transport: "{transport}"
location: {location}
duration: {duration}
discount: {discount}
price: {price}
description: "{meta_desc}"
keywords: "{keywords}"
---

## ✈️ {title}

- 🆔 Mã tour: **{ma_tour}**
- 📍 Địa điểm: **{location}**
- 🚗 Phương tiện: **{transport}**
- 💰 Giá tour: **{price} VND**
- ⏳ Thời lượng: **{duration}**

---

{content}

---

👉 Liên hệ ngay để đặt tour hấp dẫn này!

**Từ khóa SEO:**  
{keywords}

"""

            with open(filepath, "w", encoding="utf-8") as post_file:
                post_file.write(md_content)

    print(f"✅ Đã xử lý xong file: {csv_file}")
