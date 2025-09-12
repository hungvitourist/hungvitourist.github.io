---
layout: page
title: "Dịch Vụ Vé Máy Bay - Hùng Vĩ Tourist"
meta-title: "Đặt Vé Máy Bay Dễ Dàng & Nhanh Chóng"
bigimg:
- "/img/Picture-HSL/HSL-index.png"
permalink: /flights
---

<!-- Layer 1 -->

<div class="gradient-bg">
  <div class="gradient-text">
    <p>Tỏa sáng theo cách của riêng bạn</p>
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
    ✨Vé Máy Bay Nội Địa✨
  </div>
  <div class="description-content-index-sp">
  🛫 Đặt vé máy bay nhanh chóng, thủ tục đơn giản.<br>
  🏝️ Kết nối các điểm đến nổi tiếng trong Việt Nam.<br>
  💳 Giá cả hợp lý, nhiều chương trình khuyến mãi hấp dẫn.
  </div>
  {% assign hascategoryPosts = false %}
  <div class="details">
    {% for post in site.flights limit:8 %}
	{% if post.category == 'flights#domestic' %}
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

<!-- Layer 1 -->

<div class="gradient-bg">
  <div class="gradient-text">
    <p>Tỏa sáng theo cách của riêng bạn</p>
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
	✨Vé Máy Bay Quốc Tế✨
	</div>
	<div class="description-content-index-sp">
  🌏 Bay đến các thành phố lớn trên thế giới.<br>
  ✈️ Hỗ trợ nhiều hãng hàng không quốc tế uy tín.<br>
  🕒 Linh hoạt giờ bay, giá vé cạnh tranh.
	</div>
	{% assign hascategoryPosts = false %}
	<div class="details">
    {% for post in site.flights limit:8 %}
	{% if post.category == 'flights#international' %}
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

<!-- Layer 1 -->

<div class="gradient-bg">
  <div class="gradient-text">
    <p>Tỏa sáng theo cách của riêng bạn</p>
  </div>
</div>

<div id="booking" class="content-index" style="
      background: 
        linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.5) 100%), 
        url('/img/Picture-HSL/HSL-index.png');
      background-size: cover; /* Ảnh nền bao phủ toàn bộ vùng */
      background-position: center; /* Căn giữa ảnh nền */
      background-repeat: no-repeat; /* Không lặp lại ảnh nền */
        ">
	<div class="summary">
	✨Đặt Chỗ & Hành Lý✨
	</div>
	<div class="description-content-index-sp">
  💺 Hỗ trợ chọn chỗ ngồi theo yêu cầu.<br>
  🛄 Dịch vụ ký gửi và hành lý xách tay thuận tiện.<br>
  📞 Hỗ trợ 24/7, đảm bảo chuyến đi suôn sẻ.
	</div>
  	{% assign hascategoryPosts = false %}
	<div class="details">
    {% for post in site.flights limit:8 %}
	{% if post.category == 'flights#booking' %}
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
