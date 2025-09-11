module Jekyll
  module FormatPrice
    def format_price(input)
      input.to_s.reverse.gsub(/(\d{3})(?=\d)/, '\\1.').reverse + " VNĐ"
    end
  end
end

Liquid::Template.register_filter(Jekyll::FormatPrice)
