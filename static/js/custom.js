(function ($) {
    "use strict";
    $(document).ready(function () {
        /*
       Preeloader
       ============================*/
        $(window).on("load", function () {
            $("#preloader").fadeOut();
            $("#preloader-status").delay(200).fadeOut("slow");
            $("body").delay(200).css({ "overflow-x": "hidden" });
        });

        /*
       Jquery Mobile Menu
       ============================*/
        $("#main-menu").meanmenu({
            meanScreenWidth: "991",
            meanMenuContainer: ".mobile-nav-menu",
        });

        // Mobile toggle button
         $(".mobile-menu-toggle-btn").on("click", function () {
            $(".menu-sidebar-area").addClass("active");
            $(".body-overlay").addClass("active");
            // $(".mean-nav :first-child ul").css("display", "block");

        });
        $(".menu-sidebar-close-btn").on("click", function () {
            $(".menu-sidebar-area").removeClass("active");
            $(".body-overlay").removeClass("active");
        });

         /*
       Jquery Body Overlay
       ============================*/
        $(".body-overlay").on("click", function () {
            $(".menu-sidebar-area").removeClass("active");
            $(".body-overlay").removeClass("active");
        });


        /*
        Stikey Js
        ============================*/
        var nav = $(".header-menu-area.sticky-header");
        var scrolled = false;
        $(window).scroll(function () {
            if (100 < $(window).scrollTop() && !scrolled) {
                nav
                    .addClass("sticky_menu animated fadeIn")
                    .animate({ "margin-top": "0px" });
                scrolled = true;
            }
            if (100 > $(window).scrollTop() && scrolled) {
                nav.removeClass("sticky_menu animated fadeIn").css("margin-top", "0px");
                scrolled = false;
            }
        });


        /*
        Jquery Accordion
        ============================*/

        $('body').on('click','.accordion-wrapper-two .accordion-head', function () {
            $('.accordion-title').trigger('click');
        });

        /*
        Skill Progress Bar Js
        ============================*/
        $('.skill-progressbar').one('inview', function (event, isInView, visiblePartX, visiblePartY) {
            if (isInView) {
                jQuery('.progress-inner').each(function () {
                    jQuery(this).find('.progress-content').animate({
                        width: jQuery(this).attr('data-percentage')
                    }, 2000);

                    jQuery(this).find('.progress-number-count').animate(
                        { left: jQuery(this).attr('data-percentage') },
                        {
                            duration: 2000,
                            step: function (now, fx) {
                                var data = Math.round(now);
                                jQuery(this).find('.progress-percent').html(data + '%');
                            }
                        });
                });

            }
        });
        /*
       Slider
       ============================*/
        $(".slider-wrapper").slick({
            slidesToShow: 1,
            infinite: true,
            autoplay: false,
            draggable: true,
            arrows: true,
            slidesToScroll: 1,
            loop: true,
            dots: true,
            speed: 1500,
            // fade: true,
            prevArrow:
                "<button type='button' class='slider-arrow-btn prev-btn'><i class='icon-arrow-left-2'></i></button>",
            nextArrow:
                "<button type='button' class='slider-arrow-btn next-btn'><i class='icon-arrow-right-2'></i></button>",
            responsive: [
                {
                    breakpoint: 767,
                    settings: {
                        autoplay: true,
                    },
                },
            ],
        });

        /*
       Portfolio Card Slider service page
       ============================*/
        $(".portfolio_card_wrapper").slick({
            slidesToShow: 3,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: true,
            slidesToScroll: 1,
            loop: true,
            dots: false,
            speed: 1500,
            prevArrow:
                "<button type='button' class='portfolio-card-arrow-btn active prev-btn'><i class='icon-arrow-left-2'></i></button>",
            nextArrow:
                "<button type='button' class='portfolio-card-arrow-btn next-btn'><i class='icon-arrow-right-2'></i></button>",
            responsive: [
                {
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
                    },
                },
            ],
        });


        $('.prev_btn_custom').on('click', function (e) {
            e.preventDefault();
            $('.prev-btn').trigger('click');
        });
        $('.next_btn_custom').on('click', function (e) {
            e.preventDefault();
            $('.next-btn').trigger('click');
        });

        /*
       Team Slider
       ============================*/
        $("#team_slider_one").slick({
            slidesToShow: 2,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: true,
            slidesToScroll: 1,
            loop: true,
            dots: true,
            speed: 1500,
            // variableWidth: true,
             prevArrow:
                "<button type='button' class='team-card-arrow-btn prev-btn'><i class='icon-arrow-left-2'></i></button>",
            nextArrow:
                "<button type='button' class='team-card-arrow-btn next-btn'><i class='icon-arrow-right-2'></i></button>",
            responsive: [
                {
                    breakpoint: 1399,
                    settings: {
                        slidesToShow: 3,
                    },
                },
                {
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
                        variableWidth: false,
                    },
                },
            ],
        });
        $('#team-prev').on('click', function (e) {
            e.preventDefault();
            $('.prev-btn').trigger('click');
        });
        $('#team-next').on('click', function (e) {
            e.preventDefault();
            $('.next-btn').trigger('click');
        });

        /*
       Team Slider
       ============================*/
        $("#team_slider_two").slick({
            slidesToShow: 3,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: true,
            slidesToScroll: 1,
            loop: true,
            dots: true,
            speed: 1500,
            // variableWidth: true,
            prevArrow:
                "<button type='button' class='team-card-arrow-btn prev-btn'><i class='icon-arrow-left-2'></i></button>",
            nextArrow:
                "<button type='button' class='team-card-arrow-btn next-btn'><i class='icon-arrow-right-2'></i></button>",
            responsive: [
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
                        variableWidth: false,
                    },
                },
            ],
        });

       /*
       Testimonial Slider
       ============================*/
        $("#testimonial_two").slick({
            slidesToShow: 1,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: true,
            slidesToScroll: 1,
            loop: true,
            dots: false,
            speed: 1500,
            prevArrow:
                "<button type='button' class='testimonial-arrow-btn prev-btn'><i class='icon-arrow-left-2'></i></button>",
            nextArrow:
                "<button type='button' class='testimonial-arrow-btn next-btn'><i class='icon-arrow-right-2'></i></button>",
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        autoplay: true,
                        slidesToShow: 1,
                    },
                }
            ],
        });

        $('#trigger_testimonial_prev').on('click', function () {
            $('.testimonial-slider-wrapper .prev-btn').trigger('click');
        });
        $('#trigger_testimonial_next').on('click', function () {
            $('.testimonial-slider-wrapper .next-btn').trigger('click');
        });

        
         /*
       Jquery Tilt Js
       ============================*/
        $('.tilt-animate').tilt({
            maxTilt: 12,
            perspective: 1500,
        })


        // Home-one Service
        $(".service-slider").slick({
            slidesToShow: 3,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: false,
            slidesToScroll: 1,
            loop: true,
            dots: false,
            speed: 1500,
            prevArrow:
                "<button type='button' class='case-arrow-btn prev-btn'><i class='icon-arrow-left-2'></i></button>",
            nextArrow:
                "<button type='button' class='case-arrow-btn next-btn'><i class='icon-arrow-right-2'></i></button>",
            responsive: [
                {
                    breakpoint: 1199,
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
                    },
                },
            ],
        });

        // Portfolio Slider
        $(".portfolio-slider-wrapper").slick({
            slidesToShow: 3,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: true,
            slidesToScroll: 1,
            loop: true,
            dots: false,
            speed: 1500,
             variableWidth: true,
            prevArrow:
                "<button type='button' class='case-arrow-btn prev-btn'><i class='icon-arrow-left-2'></i></button>",
            nextArrow:
                "<button type='button' class='case-arrow-btn next-btn'><i class='icon-arrow-right-2'></i></button>",
            responsive: [
                {
                    breakpoint: 1399,
                    settings: {
                        slidesToShow: 2,
                        variableWidth: false,
                    },
                },
                {
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 2,
                        variableWidth: false,
                    },
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
             variableWidth: false,
                    },
                },
            ],
        });

        // Home-one Review
        $(".testimonial-slider").slick({
            slidesToShow: 1,
            infinite: true,
            autoplay: false,
            draggable: true,
            arrows: true,
            slidesToScroll: 1,
            loop: true,
            dots: false,
            speed: 1500,
            prevArrow:
                "<button type='button' class='review-arrow-btn prev-btn'><i class='icon-arrow-left-2'></i></button>",
            nextArrow:
                "<button type='button' class='review-arrow-btn next-btn'><i class='icon-arrow-right-2'></i></button>",
        });

        // Home-one Team-member slider
        $("#team_slider").slick({
            slidesToShow: 4,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: true,
            slidesToScroll: 1,
            loop: true,
            dots: false,
            speed: 1500,
            variableWidth: true,
             prevArrow:
                "<button type='button' class='team-arrow-prev'><i class='icon-arrow-left-2'></i></button>",
            nextArrow:
                "<button type='button' class='team-arrow-next'><i class='icon-arrow-right-2'></i></button>",
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 2,
                        variableWidth: false,
                    },
                },
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 2,
                        variableWidth: false,
                    },
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                        variableWidth: false,
                    },
                },
                {
                    breakpoint: 550,
                    settings: {
                        slidesToShow: 1,
                        variableWidth: false,
                    },
                }
            ],
        });

         $('#home-one-team-prev').on('click', function (e) {
             e.preventDefault()
            $('.team-arrow-prev').trigger('click');
        });
        $('#home-one-team-next').on('click', function (e) {
            e.preventDefault()
            $('.team-arrow-next').trigger('click');
        });
        // client-logo slider home-one
        $(".client-logo-slider-wrapper").slick({
            slidesToShow: 5,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: false,
            slidesToScroll: 1,
            loop: true,
            dots: true,
            speed: 1500,

            responsive: [
                {
                    breakpoint: 767,
                    settings: {
                        autoplay: true,
                        slidesToShow: 3,
                    },
                },
                {
                    breakpoint: 424,
                    settings: {
                        autoplay: true,
                        slidesToShow: 2,
                    },
                },
            ],
        });

        // Brand Slider Style 2
        $("#brand_slider").slick({
            slidesToShow: 1,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: false,
            slidesToScroll: 1,
            loop: true,
            dots: true,
            speed: 1500,
        });


        // Process Step Slider
        $(".process-step-slider").slick({
            slidesToShow: 1,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: false,
            slidesToScroll: 1,
            loop: true,
            dots: false,
            speed: 800,
            asNavFor: '.process-step-slider-tab',
            prevArrow:
                "<button type='button' class='process-arrow-btn prev-btn'><i class='icon-arrow-left-2'></i></button>",
            nextArrow:
                "<button type='button' class='process-arrow-btn next-btn active'><i class='icon-arrow-right-2'></i></button>",
                responsive: [
                {
                    breakpoint: 767,
                    settings: {
                        autoplay: true,
                        slidesToShow: 1,
                        arrows: false,
                    },
                },
            ],
        });

        // Process Step Slider Tab
        $('.process-step-slider-tab').slick({
            slidesToShow: 3,
            slidesToScroll: 3,
            loop: true,
            infinite: true,
            asNavFor: '.process-step-slider',
            dots: false,
            centerMode: true,
            focusOnSelect: true,
            arrows:false,
            responsive: [
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
                    },
                }
            ],
        });

        $(".home-two-testimonial-card-slider").slick({
            slidesToShow: 1,
            infinite: false,
            autoplay: true,
            draggable: true,
            arrows: false,
            slidesToScroll: 1,
            loop: false,
            dots: true,
            speed: 1500,
            responsive: [
                {
                    breakpoint: 767,
                    settings: {
                        autoplay: true,
                        slidesToShow: 1,
                    },
                },
            ],
        });

        // Portfolio Slider
        $("#portfolio_slider_three").slick({
            slidesToShow: 3,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: true,
            slidesToScroll: 1,
            loop: true,
            dots: false,
            speed: 1500,
            variableWidth: true,
            prevArrow:
                "<button type='button' class='portfolio-card-arrow-btn active prev-btn'><i class='icon-arrow-right-2'></i></button>",
            nextArrow:
                "<button type='button' class='portfolio-card-arrow-btn next-btn'><i class='icon-arrow-left-2'></i></button>",
            responsive: [
                {
                    breakpoint: 1399,
                    settings: {
                        slidesToShow: 2,
                        variableWidth: false,
                    },
                },
                {
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 2,
                        variableWidth: false,
                    },
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
                        variableWidth: false,
                    },
                },
            ],
        });

        // Service Slider Three
        $("#service_slider_three").slick({
            slidesToShow: 4,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: true,
            slidesToScroll: 1,
            loop: true,
            dots: false,
            speed: 1500,
            variableWidth: true,
            prevArrow:
                "<button type='button' class='home-three-service-arrow-btn prev-btn'><i class='icon-arrow-left-2'></i></button>",
            nextArrow:
                "<button type='button' class='home-three-service-arrow-btn next-btn'><i class='icon-arrow-right-2'></i></button>",
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 4,
                    },
                },
                {
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 2,
                        variableWidth: false,
                    },
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                        variableWidth: false,
                    },
                },
                {
                    breakpoint: 660,
                    settings: {
                        slidesToShow: 2,
                        variableWidth: false,
                    },
                },
                {
                    breakpoint: 659,
                    settings: {
                        slidesToShow: 1,
                        variableWidth: false,
                    },
                },
            ],
        });


        $('.prev_btn_custom').on('click', function (e) {
            e.preventDefault()
            $('.prev-btn').trigger('click');
        });
        $('.next_btn_custom').on('click', function (e) {
            e.preventDefault()
            $('.next-btn').trigger('click');
        });


        // Price switch
        $('.price-switch').on('click', function () {
            $('.switch-price-card').toggleClass(' reverse ');
        });

        // Home-three review slider
        $(".home-three-review-slider").slick({
            slidesToShow: 3,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: true,
            slidesToScroll: 1,
            loop: true,
            dots: false,
            speed: 1500,
            prevArrow:
                "<button type='button' class='home-three-review-arrow-btn prev-btn'><i class='icon-arrow-left-2'></i></button>",
            nextArrow:
                "<button type='button' class='home-three-review-arrow-btn next-btn'><i class='icon-arrow-right-2'></i></button>",
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
                    },
                },
            ],
        });

        $('.home-three-review-arrow-btn prev_btn_custom').on('click', function () {
            $('.home-three-review-arrow-btn prev-btn').trigger('click');
        });
        $('.home-three-review-arrow-btn next_btn_custom').on('click', function () {
            $('.home-three-review-arrow-btn next-btn').trigger('click');
        });


        /*
       Post Gallery Slider
       ============================*/
        $(".post-gallery").slick({
            slidesToShow: 1,
            infinite: false,
            autoplay: true,
            draggable: true,
            arrows: true,
            slidesToScroll: 1,
            loop: true,
            dots: false,
            speed: 300,
            prevArrow:
                "<button type='button' class='post-gallery-btn prev-btn'><i class='fa fa-arrow-left'></i></button>",
            nextArrow:
                "<button type='button' class='post-gallery-btn next-btn'><i class='fa fa-arrow-right'></i></button>",
        });

        /*
       Client Logo Slider
       ============================*/
        $(".brand-slider").slick({
            slidesToShow: 5,
            infinite: true,
            autoplay: true,
            draggable: true,
            arrows: false,
            slidesToScroll: 1,
            loop: true,
            dots: false,
            speed: 1500,
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 4,
                    },
                },
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 3,
                    },
                },
                {
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 3,
                    },
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 2,
                    },
                },
            ],
        });

        /*
       Jquery Nice Select Js
       ============================*/
        $('select').niceSelect();
        
        /*
       scrollUp
       ============================*/
        $.scrollUp({
            scrollText: '<i class="fa-light fa-arrow-up-long"></i>',
            easingType: "linear",
            scrollSpeed: 900,
            animation: "fade",
        });
        /*
       scrolldown
       ============================*/
        $("#scrolldown").on('click', function(e) {
            e.preventDefault()
        $('html, body').animate({
            scrollTop: $("#scrolldown-end").offset().top
        }, 1500);
        });

        /*
        ounter Js
        ============================*/
        $(".counter").counterUp({
            delay: 100,
            time: 2500,
        });

        /*
       Magnific Popup
       ============================*/
        $(".video-play").magnificPopup({
            disableOn: 700,
            type: "iframe",
            mainClass: "mfp-fade",
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false,
        });

        $('.isotope-grid').isotope({
            itemSelector: '.isotope-item',
            layoutMode: 'fitRows'
        });
       var $grid = $('.isotope-grid').isotope({
        itemSelector: '.isotope-item',
            layoutMode: 'fitRows'
        });
        // filter items on button click
        $('.filter-button-group').on( 'click', 'button', function() {
        var filterValue = $(this).attr('data-filter');
        $grid.isotope({ filter: filterValue });
        });
    });
})(jQuery);
