(function ($)
  { "use strict"
  

/* 1. Proloder */
    $(window).on('load', function () {
      $('#preloader-active').delay(450).fadeOut('slow');
      $('body').delay(450).css({
        'overflow': 'visible'
      });
    });

/* 2. sticky And Scroll UP */
    $(window).on('scroll', function () {
      var scroll = $(window).scrollTop();
      if (scroll < 400) {
        $(".header-sticky").removeClass("sticky-bar");
        $('#back-top').fadeOut(500);
      } else {
        $(".header-sticky").addClass("sticky-bar");
        $('#back-top').fadeIn(500);
      }
    });

  // Scroll Up
    $('#back-top a').on("click", function () {
      $('body,html').animate({
        scrollTop: 0
      }, 800);
      return false;
    });
  

/* 3. slick Nav */
// mobile_menu
    var menu = $('ul#navigation');
    if(menu.length){
      menu.slicknav({
        prependTo: ".mobile_menu",
        closedSymbol: '+',
        openedSymbol:'-'
      });
    };

/* 4. MainSlider-1 */
    // h1-hero-active
    function mainSlider() {
      var BasicSlider = $('.slider-active');
      BasicSlider.on('init', function (e, slick) {
        var $firstAnimatingElements = $('.single-slider:first-child').find('[data-animation]');
        doAnimations($firstAnimatingElements);
      });
      BasicSlider.on('beforeChange', function (e, slick, currentSlide, nextSlide) {
        var $animatingElements = $('.single-slider[data-slick-index="' + nextSlide + '"]').find('[data-animation]');
        doAnimations($animatingElements);
      });
      BasicSlider.slick({
        autoplay: true,
        autoplaySpeed: 8000,
        dots: false,
        fade: true,
        arrows: false, 
        prevArrow: '<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',
        nextArrow: '<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',
        responsive: [{
            breakpoint: 1024,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 991,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              arrows: false
            }
          },
          {
            breakpoint: 767,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              arrows: false,
              dots:false
            }
          }
        ]
      });

      function doAnimations(elements) {
        var animationEndEvents = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
        elements.each(function () {
          var $this = $(this);
          var $animationDelay = $this.data('delay');
          var $animationType = 'animated ' + $this.data('animation');
          $this.css({
            'animation-delay': $animationDelay,
            '-webkit-animation-delay': $animationDelay
          });
          $this.addClass($animationType).one(animationEndEvents, function () {
            $this.removeClass($animationType);
          });
        });
      }
    }
    mainSlider();

    $('.owl-carousel').owlCarousel({
      autoplay: true,
      center: true,
      loop: true,
      nav: true,
      items:1
    });

    
/* 4. Testimonial Active*/
var testimonial = $('.h1-testimonial-active');
if(testimonial.length){
testimonial.slick({
    dots: true,
    infinite: true,
    speed: 1000,
    autoplay:true,
    loop:true,
    arrows: true,
    prevArrow: '<button type="button" class="slick-prev"><i class="ti-arrow-top-left"></i></button>',
    nextArrow: '<button type="button" class="slick-next"><i class="ti-arrow-top-right"></i></button>',
    slidesToShow: 1,
    slidesToScroll: 1,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
          dots: true,
          arrows:true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows:true
        }
      },
      {
        breakpoint: 500,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
          dots:false
        }
      }
    ]
  });
}



// Single Img slder
$('.services-active').slick({
  dots: false,
  infinite: true,
  autoplay: true,
  speed: 500,
  arrows: true,
  prevArrow: '<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',
  nextArrow: '<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',
  slidesToShow: 3,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
      }
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
      }
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        arrows: true
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false
      }
    },
  ]
});

function centerSliderArrows() {
    $('.services-active').each(function () {

        var slider = $(this);
        var catIcon = slider.find('.slick-current .cat-icon');

        if (!catIcon.length) {
            catIcon = slider.find('.cat-icon').first();
        }

        if (!catIcon.length) {
            return;
        }

        var iconTop = catIcon.position().top;
        var iconHeight = catIcon.outerHeight();

        slider.find('.slick-prev, .slick-next').css(
            'top',
            (iconTop + iconHeight / 2) + 'px'
        );
    });
}

$(window).on('load resize', function () {
    centerSliderArrows();
});

$('.services-active').on('afterChange setPosition', function () {
    centerSliderArrows();
});

/* 6. Nice Selectorp  */
  var nice_Select = $('select');
    if(nice_Select.length){
      nice_Select.niceSelect();
    }

/* 7. data-background */
    $("[data-background]").each(function () {
      $(this).css("background-image", "url(" + $(this).attr("data-background") + ")")
      });


/* 10. WOW active */
    new WOW().init();

// 11. ---- Mailchimp js --------//  
    function mailChimp() {
      $('#mc_embed_signup').find('form').ajaxChimp();
    }
    mailChimp();


// 12 Pop Up Img
    var popUp = $('.single_gallery_part, .img-pop-up');
      if(popUp.length){
        popUp.magnificPopup({
          type: 'image',
          gallery:{
            enabled:true
          }
        });
      }
// 12 Pop Up Video
    var popUp = $('.popup-video');
    if(popUp.length){
      popUp.magnificPopup({
        type: 'iframe'
      });
    }

/* 13. counterUp*/
    $('.counter').counterUp({
      delay: 10,
      time: 3000
    });

/* 14. Datepicker */
  $('#datepicker1').datepicker();

// 15. Time Picker
  $('#timepicker').timepicker();

//16. Overlay
  $(".snake").snakeify({
    speed: 200
  });


//17.  Progress barfiller

  $('#bar1').barfiller();
  $('#bar2').barfiller();
  $('#bar3').barfiller();
  $('#bar4').barfiller();
  $('#bar5').barfiller();
  $('#bar6').barfiller();

})(jQuery);

$(document).ready(function () {

    $('.anatomy-heading').css({
        opacity: 0,
        transform: 'translateY(40px)'
    });

    $('.anatomy-visual').css({
        opacity: 0,
        transform: 'translateX(50px)'
    });

    $('.anatomy-part').css({
        opacity: 0,
        transform: 'translateY(25px)'
    });


    function anatomyAnimation() {

        $('.f1-anatomy').each(function () {

            var section = $(this);
            var windowBottom = $(window).scrollTop() + $(window).height();
            var sectionTop = section.offset().top;

            if (windowBottom > sectionTop + 100) {

                section.find('.anatomy-heading').animate({
                    opacity: 1
                }, 700);

                section.find('.anatomy-heading').css(
                    'transform',
                    'translateY(0)'
                );

                section.find('.anatomy-visual').animate({
                    opacity: 1
                }, 900);

                section.find('.anatomy-visual').css(
                    'transform',
                    'translateX(0)'
                );

                section.find('.anatomy-part').each(function (index) {

                    var item = $(this);

                    setTimeout(function () {

                        item.animate({
                            opacity: 1
                        }, 500);

                        item.css(
                            'transform',
                            'translateY(0)'
                        );

                    }, index * 100);

                });

            }

        });

    }


    $(window).on('scroll load', anatomyAnimation);

});