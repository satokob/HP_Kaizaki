// Sticky Header
$(window).scroll(function() {
  if ($(window).scrollTop() > 1) {
      $('.main_h').addClass('sticky');
  } else {
      $('.main_h').removeClass('sticky');
  }
});

// Mobile Navigation
$('.mobile-toggle').click(function() {
  if ($('.main_h').hasClass('open-nav')) {
      $('.main_h').removeClass('open-nav');
  } else {
      $('.main_h').addClass('open-nav');
  }
});

$('.main_h li a').click(function() {
  if ($('.main_h').hasClass('open-nav')) {
      $('.navigation').removeClass('open-nav');
      $('.main_h').removeClass('open-nav');
  }
});

// Navigation scroll
$('nav a').click(function(event) {
  var id = $(this).attr("href");
  var offset = 70;
  var target = $(id).offset().top - offset;
  $('html, body').animate({
      scrollTop: target
  }, 500);
  event.preventDefault();
});

$(document).ready(function() {
  // スクロールができるかどうかを判定
  function checkScroll() {
      if ($(document).height() <= $(window).height()) {
          // スクロールできない場合、ヘッダーを表示
          $('.main_h').addClass('sticky');
      } else {
        $('.main_h').removeClass('sticky');
      }
  }

  // 初期ロード時にチェック
  checkScroll();

  // ウィンドウサイズ変更時にもチェック
  $(window).resize(function() {
      checkScroll();
  });
});