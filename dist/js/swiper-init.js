// assets/js/swiper-init.js
document.addEventListener("DOMContentLoaded", function () {
  const swiper = new Swiper(".swiper", {
    slidesPerView: 3,   // Mỗi hàng có 3 slide
    spaceBetween: 16,   // Khoảng cách giữa các slide
    breakpoints: {
      0: { slidesPerView: 1.2 },
      768: { slidesPerView: 2 },
      1024: { slidesPerView: 3 }
    },
    loop: true,
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev"
    },
  });
});
