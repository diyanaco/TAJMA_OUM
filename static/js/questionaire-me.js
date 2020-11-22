// $(window).scroll(function() {
//     var scrollTop = $(this).scrollTop();

//     $('.question').css({
//       opacity: function() {
//         var elementHeight = $(this).height();
//         return 1 - (elementHeight - scrollTop) / elementHeight;
//       }
//     });
//   });

// $(document).ready(function () {
//   $(window).scroll(function () {
//     $('.question').each(function(){
//       if ($(this).scrollTop() > 100) {
//         $(this).addClass("active")
//     // });
//     // if ($(this).scrollTop() > 100) {
//     //   // $('.question').each(function (index) {
//     //   //   if (index == 0) {
//     //   //     $(this).addClass("active")
//     //   //   }
//     //   // });
//     //   $('.question').each(function() {
//     //       $(this).addClass("active")
//     //   });
//     //   // $(".question").css({"opacity" : "0"})
//     // }
//     // else {
//     //   $(".question").css({ "opacity": "1" })
//     }});
// })

  $(window).on("scroll", function() {
    $(".question").each(function() {
      var etop = $(this).offset().top;
      var diff = etop - $(window).scrollTop();

      if (diff > 100 && diff < 300) {
        reinitState(this);
      }
    });
  });

  function reinitState(e) {
    $(".question").removeClass("active");

    $(".question").each(function() {
      $(this).blur();
    });
    $(e).addClass("active");
    /*$(e).find('input').focus();*/
  }