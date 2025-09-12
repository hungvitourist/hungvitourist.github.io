---
layout: page
title: "Gậy LED Magic -  Magic LED HSL"
meta-title: "Light Up Your Style"
bigimg:
- "/img/Picture-HSL/HSL-index.png"
permalink: /visa
---

<!-- Layer 1 VISUAL POI PIXEL -->

<div class="gradient-bg">
  <div class="gradient-text">
    <p>Tỏa sáng theo cách của riêng bạn</p>
  </div>
</div>

<div id="travel" class="content-index" style="
      background: 
        linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.5) 100%), 
        url('/img/Picture-HSL/HSL-index.png');
      background-size: cover; /* Ảnh nền bao phủ toàn bộ vùng */
      background-position: center; /* Căn giữa ảnh nền */
      background-repeat: no-repeat; /* Không lặp lại ảnh nền */
        ">
  <div class="summary">
    ✨Visa Du Lịch✨
  </div>
  <div class="description-content-index-sp">
    🌍 Hỗ trợ xin visa du lịch đi nhiều quốc gia.<br>
    📑 Thủ tục đơn giản, hướng dẫn chi tiết từng bước.<br>
    ⏱️ Thời gian xử lý nhanh chóng, tỷ lệ đậu cao.
  </div>
  {% assign hascategoryPosts = false %}
  <div class="details">
    {% for post in site.visa limit:8 %}
	{% if post.category == 'visa#travel' %}
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

<!-- Layer 1 VISUAL HOOP PIXEL -->

<div class="gradient-bg">
  <div class="gradient-text">
    <p>Tỏa sáng theo cách của riêng bạn</p>
  </div>
</div>

<div id="business" class="content-index" style="
      background: 
        linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.5) 100%), 
        url('/img/Picture-HSL/HSL-index.png');
      background-size: cover; /* Ảnh nền bao phủ toàn bộ vùng */
      background-position: center; /* Căn giữa ảnh nền */
      background-repeat: no-repeat; /* Không lặp lại ảnh nền */
        ">
	<div class="summary">
	✨Visa Công Tác✨
	</div>
	<div class="description-content-index-sp">
    💼 Hỗ trợ làm visa công tác đi nhiều quốc gia.<br>
    📑 Hồ sơ chuẩn bị rõ ràng, quy trình nhanh chóng.<br>
    🤝 Dịch vụ uy tín, đồng hành cùng doanh nghiệp trên mọi hành trình.
	</div>
	{% assign hascategoryPosts = false %}
	<div class="details">
    {% for post in site.visa limit:8 %}
	{% if post.category == 'visa#business' %}
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

<div id="study" class="content-index" style="
      background: 
        linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.5) 100%), 
        url('/img/Picture-HSL/HSL-index.png');
      background-size: cover; /* Ảnh nền bao phủ toàn bộ vùng */
      background-position: center; /* Căn giữa ảnh nền */
      background-repeat: no-repeat; /* Không lặp lại ảnh nền */
        ">
	<div class="summary">
	✨Visa Du Học✨
	</div>
	<div class="description-content-index-sp">
    🎓 Hỗ trợ xin visa du học tại nhiều quốc gia.<br>
    📑 Tư vấn hồ sơ, giấy tờ cần thiết đầy đủ và chi tiết.<br>
    🕒 Thời gian xử lý nhanh chóng, tăng tỷ lệ đậu visa.
	</div>
  	{% assign hascategoryPosts = false %}
	<div class="details">
  {% for post in site.visa limit:8 %}
	{% if post.category == 'visa#study' %}
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


<!-- Layer 1 OTHER -->

<div class="gradient-bg">
  <div class="gradient-text">
    <p>Tỏa sáng theo cách của riêng bạn</p>
  </div>
</div>

<div id="other" class="content-index" style="
      background: 
        linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.5) 100%), 
        url('/img/Picture-HSL/HSL-index.png');
      background-size: cover; /* Ảnh nền bao phủ toàn bộ vùng */
      background-position: center; /* Căn giữa ảnh nền */
      background-repeat: no-repeat; /* Không lặp lại ảnh nền */
        ">
	<div class="summary">
	✨Dịch Vụ Khác✨
	</div>
	<div class="description-content-index-sp">
    🛂 Hỗ trợ làm hộ chiếu, gia hạn hộ chiếu.<br>
    📄 Dịch thuật công chứng hồ sơ du lịch và công tác.<br>
    🌍 Các dịch vụ giấy tờ xuất nhập cảnh khác theo yêu cầu.
	</div>
  	{% assign hascategoryPosts = false %}
	<div class="details">
    {% for post in site.visa limit:8 %}
	{% if post.category == 'visa#other' %}
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
