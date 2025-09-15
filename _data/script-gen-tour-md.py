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

def generate_ai_content(ma_tour, title, location, transport, price, duration, discount=None):
    # Xử lý giá gốc
    try:
        gia_raw = int(str(price).replace(".", "").replace(",", ""))
    except:
        gia_raw = 0

    # Nếu có discount thì tính giá sau giảm
    discount_note = ""
    if discount and str(discount).isdigit() and int(discount) > 0:
        discount = int(discount)
        final_price = int(gia_raw * (100 - discount) / 100)
        # Format giá đẹp
        gia_fmt = f"{gia_raw:,.0f} VND".replace(",", ".")
        final_fmt = f"{final_price:,.0f} VND".replace(",", ".")
        discount_note = f"- 💰 Giá tour gốc: **{gia_fmt}**\n- 🔥 Giảm giá: **{discount}%**\n- 💵 Giá khuyến mãi: **{final_fmt}**\n"
    else:
        gia_fmt = f"{gia_raw:,.0f} VND".replace(",", ".")
        discount_note = f"- 💰 Giá tour: **{gia_fmt}**\n"

    # Header thông tin tour
    header = f"""

- 🆔 Mã tour: **{ma_tour}**
- 📍 Địa điểm: **{location}**
- 🚗 Phương tiện: **{transport}**
{discount_note}- ⏳ Thời gian du lịch: **{duration}**
"""

    # Prompt cho AI
    prompt = f"""
    Bạn là chuyên gia viết content du lịch chuẩn SEO.
    Hãy viết nội dung cho một bài post Markdown với thông tin sau:

    Yêu cầu:
    1. Trả về theo cấu trúc sau:

        {header}

       ## Meta Description
       (1 đoạn, 150-160 ký tự, hấp dẫn, chuẩn SEO)

       ## Giới thiệu
       (3–4 đoạn, tổng khoảng 200-250 từ, văn phong truyền cảm hứng, có emoji, cuối đoạn có call-to-action nhẹ)

       ## Hành trình
       - Ngày 1
         🌅 Sáng: ...
         🌞 Trưa: ...
         🌙 Tối: ...
       - Ngày 2
         (Tiếp tục mô tả chi tiết)
       (tiếp tục cho các ngày)

       ## Ưu đãi
       (Nếu có giảm giá, hãy nhấn mạnh mức % giảm và giá khuyến mãi đã tính toán ở trên để khách hàng thấy lợi ích)

       ## SEO Keywords
       (5 từ khóa, ngăn cách bằng dấu phẩy)

    2. Viết nội dung dễ đọc, ngắn gọn, phù hợp khách du lịch Việt Nam.
    """

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "Bạn là chuyên gia content du lịch, viết chuẩn SEO và thu hút khách hàng."},
            {"role": "user", "content": prompt},
        ],
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
            ai_output = generate_ai_content(ma_tour, title, location, transport, price, duration, discount)
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
tour_code: {ma_tour}
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



{content}

---

👉 Liên hệ ngay để đặt tour hấp dẫn này!

☎️ Hotline: (+84) {{{{ site.phone_number }}}}
🌐 Website: [hungvitourist.com](https://hungvitourist.com)

"""

            with open(filepath, "w", encoding="utf-8") as post_file:
                post_file.write(md_content)

    print(f"✅ Đã xử lý xong file: {csv_file}")
