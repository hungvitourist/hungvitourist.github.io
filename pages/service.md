---
layout: page
title: "Dịch vụ Hung Vi Tourist"
meta-title: "Khám phá các dịch vụ du lịch chuyên nghiệp của Hung Vi Tourist"
bigimg:
- "/img/Picture-HSL/japan-background.jpg"
permalink: /service
---

<div class="gradient-bg">
  <div class="gradient-text">
    <p>Dịch vụ Du lịch – Hung Vi Tourist</p>
  </div>
</div>

<!-- 🎓 Tư vấn du lịch -->
<div id="consult" class="content-index" style="
      background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 100%),
      url('/img/Picture-HSL/HSL-index.png');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;">
  <div class="summary">
    🎓 Tư Vấn Du Lịch
  </div>
  <div class="description-content-index-sp">
    💡 Tư vấn lộ trình du lịch phù hợp với nhu cầu và ngân sách.<br>
    💡 Đề xuất tour hot theo mùa, điểm đến nổi bật.<br>
    💡 Hỗ trợ thông tin visa, giấy tờ cần thiết.<br>
    💡 Đảm bảo chuyến đi an toàn – trọn vẹn.<br>
  </div>
  {% assign hascategoryPosts = false %}
  <div class="details">
    {% for post in site.service limit:8 %}
      {% if post.category == 'service#consult' %}
        <div class="component">
          {% if post.image %}
          <a href="{{ post.url | prepend: site.baseurl }}">
            <img src="{{ post.image }}" alt="{{ post.title }}" class="avatar" loading="lazy">
          </a>
          {% endif %}
          <a href="{{ post.url | prepend: site.baseurl }}">
            {% if post.meta-title %}
            <div class="component-name">{{ post["meta-title"] }}</div>
            {% else %}
            <div class="component-name">{{ post.title }}</div>
            {% endif %}
          </a>
        </div>
        {% assign hascategoryPosts = true %}
      {% endif %}
    {% endfor %}
    {% unless hascategoryPosts %}
    <div class="text-center">
      <p>Hiện danh sách dịch vụ tư vấn đang được cập nhật. Quý khách vui lòng liên hệ Hung Vi Tourist để được hỗ trợ chi tiết.</p>
      {% include qr-zalo.html %}
    </div>
    {% endunless %}
  </div>
</div>

<!-- 🏨 Đặt khách sạn -->
<div id="hotel" class="content-index" style="
      background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 100%),
      url('/img/Picture-HSL/HSL-index.png');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;">
  <div class="summary">
    🏨 Đặt Khách Sạn
  </div>
  <div class="description-content-index-sp">
    💡 Đặt phòng khách sạn từ bình dân đến cao cấp.<br>
    💡 Ưu đãi giá tốt – thanh toán linh hoạt.<br>
    💡 Hợp tác với hệ thống resort, villa nổi tiếng.<br>
    💡 Hỗ trợ khách đoàn, công ty, nhóm sự kiện.<br>
  </div>
  {% assign hascategoryPosts = false %}
  <div class="details">
    {% for post in site.service limit:8 %}
      {% if post.category == 'service#hotel' %}
      <div class="component">
        {% if post.image %}
        <a href="{{ post.url | prepend: site.baseurl }}">
          <img src="{{ post.image }}" alt="{{ post.title }}" class="avatar" loading="lazy">
        </a>
        {% endif %}
        <a href="{{ post.url | prepend: site.baseurl }}">
          {% if post.meta-title %}
          <div class="component-name">{{ post["meta-title"] }}</div>
          {% else %}
          <div class="component-name">{{ post.title }}</div>
          {% endif %}
        </a>
      </div>
      {% assign hascategoryPosts = true %}
      {% endif %}
    {% endfor %}
    {% unless hascategoryPosts %}
    <div class="text-center">
      <p>Hiện danh sách khách sạn đang được cập nhật. Quý khách vui lòng liên hệ Hung Vi Tourist để nhận ưu đãi tốt nhất.</p>
      {% include qr-zalo.html %}
    </div>
    {% endunless %}
  </div>
</div>

<!-- 🚐 Thuê xe du lịch -->
<div id="carRental" class="content-index" style="
      background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 100%),
      url('/img/Picture-HSL/HSL-index.png');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;">
  <div class="summary">
    🚐 Thuê Xe Du Lịch
  </div>
  <div class="description-content-index-sp">
    💡 Xe 5-7-9-16-29 chỗ, đời mới, tiện nghi.<br>
    💡 Lái xe kinh nghiệm, an toàn, chu đáo.<br>
    💡 Dịch vụ đưa đón sân bay, tour, hợp đồng dài hạn.<br>
    💡 Giá cả minh bạch – phục vụ tận nơi.<br>
  </div>
  {% assign hascategoryPosts = false %}
  <div class="details">
    {% for post in site.service limit:8 %}
      {% if post.category == 'service#carRental' %}
      <div class="component">
        {% if post.image %}
        <a href="{{ post.url | prepend: site.baseurl }}">
          <img src="{{ post.image }}" alt="{{ post.title }}" class="avatar" loading="lazy">
        </a>
        {% endif %}
        <a href="{{ post.url | prepend: site.baseurl }}">
          {% if post.meta-title %}
          <div class="component-name">{{ post["meta-title"] }}</div>
          {% else %}
          <div class="component-name">{{ post.title }}</div>
          {% endif %}
        </a>
      </div>
      {% assign hascategoryPosts = true %}
      {% endif %}
    {% endfor %}
    {% unless hascategoryPosts %}
    <div class="text-center">
      <p>Dịch vụ thuê xe Happy Car đang được cập nhật. Quý khách vui lòng liên hệ để đặt xe nhanh chóng.</p>
      {% include qr-zalo.html %}
    </div>
    {% endunless %}
  </div>
</div>

<!-- 🛳️ Tour trọn gói -->
<div id="packageTour" class="content-index" style="
      background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 100%),
      url('/img/Picture-HSL/HSL-index.png');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;">
  <div class="summary">
    🛳️ Tour Trọn Gói
  </div>
  <div class="description-content-index-sp">
    💡 Tour trong nước & quốc tế đa dạng.<br>
    💡 Lịch trình khoa học, giá ưu đãi.<br>
    💡 Dịch vụ trọn gói: xe, khách sạn, vé máy bay.<br>
    💡 Hỗ trợ thiết kế tour riêng theo nhu cầu.<br>
  </div>
  {% assign hascategoryPosts = false %}
  <div class="details">
    {% for post in site.service limit:8 %}
      {% if post.category == 'service#packageTour' %}
      <div class="component">
        {% if post.image %}
        <a href="{{ post.url | prepend: site.baseurl }}">
          <img src="{{ post.image }}" alt="{{ post.title }}" class="avatar" loading="lazy">
        </a>
        {% endif %}
        <a href="{{ post.url | prepend: site.baseurl }}">
          {% if post.meta-title %}
          <div class="component-name">{{ post["meta-title"] }}</div>
          {% else %}
          <div class="component-name">{{ post.title }}</div>
          {% endif %}
        </a>
      </div>
      {% assign hascategoryPosts = true %}
      {% endif %}
    {% endfor %}
    {% unless hascategoryPosts %}
    <div class="text-center">
      <p>Danh sách tour đang được cập nhật. Vui lòng liên hệ Hung Vi Tourist để đặt tour nhanh chóng.</p>
      {% include qr-zalo.html %}
    </div>
    {% endunless %}
  </div>
</div>

<!-- 🎉 Tổ chức sự kiện -->
<div id="event" class="content-index" style="
      background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 100%),
      url('/img/Picture-HSL/HSL-index.png');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;">
  <div class="summary">
    🎉 Tổ Chức Sự Kiện
  </div>
  <div class="description-content-index-sp">
    💡 Tổ chức team building, gala dinner, hội nghị.<br>
    💡 Cung cấp MC, âm thanh ánh sáng chuyên nghiệp.<br>
    💡 Dịch vụ trọn gói – ý tưởng sáng tạo.<br>
    💡 Đảm bảo thành công cho mọi sự kiện.<br>
  </div>
  {% assign hascategoryPosts = false %}
  <div class="details">
    {% for post in site.service limit:8 %}
      {% if post.category == 'service#event' %}
      <div class="component">
        {% if post.image %}
        <a href="{{ post.url | prepend: site.baseurl }}">
          <img src="{{ post.image }}" alt="{{ post.title }}" class="avatar" loading="lazy">
        </a>
        {% endif %}
        <a href="{{ post.url | prepend: site.baseurl }}">
          {% if post.meta-title %}
          <div class="component-name">{{ post["meta-title"] }}</div>
          {% else %}
          <div class="component-name">{{ post.title }}</div>
          {% endif %}
        </a>
      </div>
      {% assign hascategoryPosts = true %}
      {% endif %}
    {% endfor %}
    {% unless hascategoryPosts %}
    <div class="text-center">
      <p>Danh sách dịch vụ tổ chức sự kiện đang được cập nhật. Vui lòng liên hệ để được tư vấn chương trình phù hợp.</p>
      {% include qr-zalo.html %}
    </div>
    {% endunless %}
  </div>
</div>

<!-- 🤝 Hợp tác & đối tác -->
<div id="partner" class="content-index" style="
      background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 100%),
      url('/img/Picture-HSL/HSL-index.png');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;">
  <div class="summary">
    🤝 Hợp Tác & Đối Tác
  </div>
  <div class="description-content-index-sp">
    💡 Liên kết với hãng hàng không, khách sạn, resort.<br>
    💡 Hợp tác với đối tác quốc tế: Thái Lan, Hàn Quốc, Nhật Bản...<br>
    💡 Chia sẻ lợi ích – phát triển bền vững.<br>
    💡 Luôn tìm kiếm đối tác uy tín, lâu dài.<br>
  </div>
  {% assign hascategoryPosts = false %}
  <div class="details">
    {% for post in site.service limit:8 %}
      {% if post.category == 'service#partner' %}
      <div class="component">
        {% if post.image %}
        <a href="{{ post.url | prepend: site.baseurl }}">
          <img src="{{ post.image }}" alt="{{ post.title }}" class="avatar" loading="lazy">
        </a>
        {% endif %}
        <a href="{{ post.url | prepend: site.baseurl }}">
          {% if post.meta-title %}
          <div class="component-name">{{ post["meta-title"] }}</div>
          {% else %}
          <div class="component-name">{{ post.title }}</div>
          {% endif %}
        </a>
      </div>
      {% assign hascategoryPosts = true %}
      {% endif %}
    {% endfor %}
    {% unless hascategoryPosts %}
    <div class="text-center">
      <p>Danh sách đối tác đang được cập nhật. Vui lòng liên hệ Hung Vi Tourist để hợp tác ngay hôm nay.</p>
      {% include qr-zalo.html %}
    </div>
    {% endunless %}
  </div>
</div>

<!-- 🛒 Dịch vụ khác -->
<div id="other" class="content-index" style="
      background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 100%),
      url('/img/Picture-HSL/HSL-index.png');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;">
  <div class="summary">
    🛒 Dịch Vụ Khác
  </div>
  <div class="description-content-index-sp">
    💡 Vé máy bay – nội địa & quốc tế.<br>
    💡 Bảo hiểm du lịch, visa trọn gói.<br>
    💡 Hỗ trợ khách đoàn, khách lẻ, công ty.<br>
    💡 Luôn đồng hành cùng khách hàng trên mọi hành trình.<br>
  </div>
  {% assign hascategoryPosts = false %}
  <div class="details">
    {% for post in site.service limit:8 %}
      {% if post.category == 'service#other' %}
      <div class="component">
        {% if post.image %}
        <a href="{{ post.url | prepend: site.baseurl }}">
          <img src="{{ post.image }}" alt="{{ post.title }}" class="avatar" loading="lazy">
        </a>
        {% endif %}
        <a href="{{ post.url | prepend: site.baseurl }}">
          {% if post.meta-title %}
          <div class="component-name">{{ post["meta-title"] }}</div>
          {% else %}
          <div class="component-name">{{ post.title }}</div>
          {% endif %}
        </a>
      </div>
      {% assign hascategoryPosts = true %}
      {% endif %}
    {% endfor %}
    {% unless hascategoryPosts %}
    <div class="text-center">
      <p>Các dịch vụ khác của Hung Vi Tourist đang được cập nhật. Quý khách vui lòng liên hệ để được tư vấn chi tiết.</p>
      {% include qr-zalo.html %}
    </div>
    {% endunless %}
  </div>
</div>



<!-- Layer 4 -->

<div class="gradient-bg">
  <div class="gradient-text">
    <P>được cung cấp dịch vụ bởi</P><h2>✨HÙNG VĨ TOURIST✨</h2>
    <br>
    <div class="text-center">
      <a target="_blank" rel="noopener" href="/" class="project-link" title="✨HÙNG VĨ TOURIST✨">
        <img src="{{ site.baseurl }}/img/Picture-HSL/logo-trans.png" class="img-rounded" loading="lazy" alt="✨HÙNG VĨ TOURIST✨" width="30%" />
      </a>
    </div>
  </div>
</div>

