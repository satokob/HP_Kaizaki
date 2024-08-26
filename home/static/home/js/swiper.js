window.onload = function() {
  const swiper = new Swiper(".hero__swiper", {
      loop: true,
      autoplay: {
          delay: 3000, // スライドが切り替わるまでの時間を長くする
          pauseOnMouseEnter: true,
          disableOnInteraction: false, 
      }, 
      speed: 1000, // スライドの移動スピードを遅くする
      slidesPerView: 2, // 一度に表示するスライドの数
      spaceBetween: 10, // 画像と画像の間に空白を追加
  });
}
