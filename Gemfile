# Gemfile - cấu hình môi trường Jekyll

# Nguồn lấy gem (RubyGems chính thức)
source "https://rubygems.org"

# Jekyll core
gem "jekyll"

# Theme mặc định (có thể thay bằng theme khác nếu muốn)
gem "minima"

# Các plugin Jekyll phổ biến
group :jekyll_plugins do
  gem "jekyll-feed"              # Tạo RSS feed (hữu ích cho SEO + Google Search Console)
  gem "jekyll-seo-tag"           # Thêm thẻ meta SEO tự động
  gem "jekyll-paginate"          # Hỗ trợ phân trang blog
  gem "jekyll-sitemap"           # Tạo sitemap.xml (SEO + Google index)
  gem "jekyll-toc"               # Tự động tạo mục lục (table of contents)
  gem "jekyll-datapage-generator" # Sinh trang động từ file dữ liệu YAML/JSON/CSV
end

# Quản lý admin site (chạy tại http://localhost:4000/admin)
gem "jekyll-admin"

# Windows và JRuby cần bổ sung tzinfo
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo"
  gem "tzinfo-data"
end

# Tăng tốc watch trên Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Các gem hỗ trợ server
gem "webrick"   # Bắt buộc cho Jekyll 4 trên Ruby 3+
gem "rack"      # Cần cho jekyll-admin
gem "listen", "~> 3.0"  # Giúp Jekyll tự động rebuild khi file thay đổi
gem "puma"      # Web server đa luồng, thay thế WEBrick khi chạy
gem "ffi"       # Cần cho listen trên Windows