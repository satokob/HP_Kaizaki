window.onload = function() {
  const swiper = new Swiper(".swiper", {
      loop: true,
      slidesPerView: 3, // 画面に表示するスライドの数
      spaceBetween: 5, // 画像間の空白を5pxに設定
      speed: 5000, // 移動スピードをゆっくりに設定
      autoplay: {
          delay: 0, // スライドが止まらないように遅延なし
          disableOnInteraction: false, // ユーザー操作でスライドが止まらないように
      },
      loopAdditionalSlides: 3, // ループを滑らかにするためのスライド追加
      cssMode: false, // CSSモードを無効にして、JavaScriptでの滑らかな動きを優先
      freeMode: true, // スライドの自由な動きを許可してスムーズな動きを実現
      freeModeMomentum: false, // 慣性移動を無効にして滑らかな連続移動を維持
      
  });
}
