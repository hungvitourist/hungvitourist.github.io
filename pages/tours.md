---
layout: page
title: "Dịch Vụ Tour Du Lịch - Hùng Vĩ Tourist"
meta-title: "TOUR TRONG NƯỚC & QUỐC TẾ"
bigimg:
- "/img/Picture-HSL/HSL-index.png"
permalink: /tours
---

<!-- Layer 1 LED PIXEL -->

<div class="gradient-bg">
  <div class="gradient-text">
    <p>🤝 “Hùng Vĩ Tourist – Nối nhịp hành trình, gắn kết niềm vui.”</p>
  </div>
</div>

<div id="domestic" class="content-index" style="
      background: 
        linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.5) 100%), 
        url('/img/Picture-HSL/HSL-index.png');
      background-size: cover; /* Ảnh nền bao phủ toàn bộ vùng */
      background-position: center; /* Căn giữa ảnh nền */
      background-repeat: no-repeat; /* Không lặp lại ảnh nền */
        ">
  <div class="summary">
    ✨Tour Trong Nước✨
  </div>
  <div class="description-content-index-sp">
  🏞️ Khám phá cảnh đẹp Việt Nam từ Bắc vào Nam.<br>
  🚌 Hành trình trọn gói, tiện lợi và tiết kiệm.<br>
  🏖️ Nhiều lựa chọn tour phù hợp nhu cầu: nghỉ dưỡng, khám phá, văn hoá.
  </div>
  {% assign hascategoryPosts = false %}
  <div class="details">
    {% for post in site.tours limit:8 %}
	  {% if post.category == 'tours#domestic' %}
    <div class="component">
      {% if post.image %}
      <!-- Ảnh đại diện bài đăng -->
      <a href="{{ post.url | prepend: site.baseurl }}">
        <img src="{{ post.image }}" alt="{{ post.title }}" class="avatar" loading="lazy">
      </a>
      {% endif %}
      <!-- Tiêu đề bài đăng -->
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
	<!-- Report hascategoryPosts -->
	{% unless hascategoryPosts %}
	<div class="text-center">
		<p>Hiện danh sách dịch vụ tư vấn đang được cập nhật. Quý khách vui lòng liên hệ Hung Vi Tourist để được hỗ trợ chi tiết.</p>
    {% include qr-zalo.html %}
	</div>
	{% endunless %}
  </div>
</div>

<!-- Layer 1 MATRIX -->

<div class="gradient-bg">
  <div class="gradient-text">
    <p>🏝️ “Khám phá thế giới, bắt đầu từ Hùng Vĩ Tourist.”</p>
  </div>
</div>

<div id="international" class="content-index" style="
      background: 
        linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.5) 100%), 
        url('/img/Picture-HSL/HSL-index.png');
      background-size: cover; /* Ảnh nền bao phủ toàn bộ vùng */
      background-position: center; /* Căn giữa ảnh nền */
      background-repeat: no-repeat; /* Không lặp lại ảnh nền */
        ">
	<div class="summary">
	✨Tour Quốc Tế✨
	</div>
	<div class="description-content-index-sp">
  🌍 Trải nghiệm hành trình khám phá năm châu bốn bể.<br>
  ✈️ Tour trọn gói từ vé máy bay, khách sạn đến tham quan.<br>
  🗺️ Nhiều điểm đến hấp dẫn: Châu Á, Châu Âu, Mỹ, Úc…
	</div>
	{% assign hascategoryPosts = false %}
	<div class="details">
    {% for post in site.tours limit:8 %}
	  {% if post.category == 'tours#international' %}
    <div class="component">
      {% if post.image %}
      <!-- Ảnh đại diện bài đăng -->
      <a href="{{ post.url | prepend: site.baseurl }}">
        <img src="{{ post.image }}" alt="{{ post.title }}" class="avatar" loading="lazy">
      </a>
      {% endif %}
      <!-- Tiêu đề bài đăng -->
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
	<!-- Report hascategoryPosts -->
	{% unless hascategoryPosts %}
	<div class="text-center">
<p>Hiện danh sách dịch vụ tư vấn đang được cập nhật. Quý khách vui lòng liên hệ Hung Vi Tourist để được hỗ trợ chi tiết.</p>
    {% include qr-zalo.html %}
	</div>
	{% endunless %}
  </div>
</div>

<!-- Layer 1 Laser -->

<div class="gradient-bg">
  <div class="gradient-text">
    <p>🚐 “Hùng Vĩ Tourist – Người bạn đồng hành trên mọi nẻo đường.”</p>
  </div>
</div>

<div id="combo" class="content-index" style="
      background: 
        linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.5) 100%), 
        url('/img/Picture-HSL/HSL-index.png');
      background-size: cover; /* Ảnh nền bao phủ toàn bộ vùng */
      background-position: center; /* Căn giữa ảnh nền */
      background-repeat: no-repeat; /* Không lặp lại ảnh nền */
        ">
	<div class="summary">
	✨Combo Du Lịch✨
	</div>
	<div class="description-content-index-sp">
  🎁 Tiết kiệm chi phí với gói combo vé máy bay + khách sạn.<br>
  🛫 Linh hoạt lựa chọn lịch trình phù hợp.<br>
  🏨 Nhiều gói khuyến mãi hấp dẫn theo mùa.
	</div>
  	{% assign hascategoryPosts = false %}
	<div class="details">
    {% for post in site.tours limit:8 %}
	{% if post.category == 'tours#combo' %}
    <div class="component">
      {% if post.image %}
      <!-- Ảnh đại diện bài đăng -->
      <a href="{{ post.url | prepend: site.baseurl }}">
        <img src="{{ post.image }}" alt="{{ post.title }}" class="avatar" loading="lazy">
      </a>
      {% endif %}
      <!-- Tiêu đề bài đăng -->
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
	<!-- Report hascategoryPosts -->
	{% unless hascategoryPosts %}
	<div class="text-center">
<p>Hiện danh sách dịch vụ tư vấn đang được cập nhật. Quý khách vui lòng liên hệ Hung Vi Tourist để được hỗ trợ chi tiết.</p>
    {% include qr-zalo.html %}
	</div>
	{% endunless %}
  </div>
</div>

<!-- Layer 1 POWER -->

<div class="gradient-bg">
  <div class="gradient-text">
    <p>Tỏa sáng theo cách của riêng bạn</p>
  </div>
</div>

<div id="freeTravel" class="content-index" style="
      background: 
        linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.5) 100%), 
        url('/img/Picture-HSL/HSL-index.png');
      background-size: cover; /* Ảnh nền bao phủ toàn bộ vùng */
      background-position: center; /* Căn giữa ảnh nền */
      background-repeat: no-repeat; /* Không lặp lại ảnh nền */
        ">
	<div class="summary">
	✨Du Lịch Tự Túc✨
	</div>
	<div class="description-content-index-sp">
  🗺️ Tự do khám phá với lịch trình riêng của bạn.<br>
  🚆 Hỗ trợ đặt vé máy bay, tàu xe và khách sạn.<br>
  📌 Gợi ý điểm đến, ăn uống, vui chơi chi tiết.
	</div>
  	{% assign hascategoryPosts = false %}
	<div class="details">
    {% for post in site.tours limit:8 %}
	{% if post.category == 'tours#freeTravel' %}
    <div class="component">
      {% if post.image %}
      <!-- Ảnh đại diện bài đăng -->
      <a href="{{ post.url | prepend: site.baseurl }}">
        <img src="{{ post.image }}" alt="{{ post.title }}" class="avatar" loading="lazy">
      </a>
      {% endif %}
      <!-- Tiêu đề bài đăng -->
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
	<!-- Report hascategoryPosts -->
	{% unless hascategoryPosts %}
	<div class="text-center">
<p>Hiện danh sách dịch vụ tư vấn đang được cập nhật. Quý khách vui lòng liên hệ Hung Vi Tourist để được hỗ trợ chi tiết.</p>
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

