// $(window).scroll(function() {
//     var scrollTop = $(this).scrollTop();
  
//     $('.question').css({
//       opacity: function() {
//         var elementHeight = $(this).height();
//         return 1 - (elementHeight - scrollTop) / elementHeight;
//       }
//     });
//   });

  $(document).ready(function(){
    $(window).scroll(function(){
      if($(this).scrollTop() > 100){
        $(".question").css({"opacity" : "0"})
      }
      else {
        $(".question").css({"opacity" : "1"})
      }
    })
  })