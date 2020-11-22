// $(window).scroll(function() {
//     var scrollTop = $(this).scrollTop();
  
//     $('.question').css({
//       opacity: function() {
//         var elementHeight = $(this).height();
//         return 1 - (elementHeight - scrollTop) / elementHeight;
//       }
//     });
//   });

  // $(document).ready(function(){
  //   $(window).scroll(function(){
  //     if($(this).scrollTop() > 100){
  //       $(".question").css({"opacity" : "0"})
  //     }
  //     else {
  //       $(".question").css({"opacity" : "1"})
  //     }
  //   })
  // })

  $(window).on("scroll", function() {
    $(container).find(".question").each(function() {
      var etop = $(this).offset().top;
      var diff = etop - $(window).scrollTop();

      if (diff > 100 && diff < 300) {
        reinitState(this);
      }
    });
  });

  function reinitState(e) {
    $(container).find(".ques").removeClass("active");

    $(container).find(".ques").each(function() {
      $(this).blur();
    });
    $(e).addClass("active");
    /*$(e).find('input').focus();*/
  }