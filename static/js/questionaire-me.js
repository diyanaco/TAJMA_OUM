$(document).ready(function () {
  
  var container = $(this).find(".form");

  $(container)
    .find(".input-radio")
    .not(".input-block input")
    .on("click", function () {
      rescroll(this);
    });  // var radios = document.forms["formA"].elements["myradio"];
  // for (var i = 0, max = radios.length; i < max; i++) {
  //   radios[i].onclick = function () {
  //     alert(this.value);
  //   }
  // }
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

  $(window).on("scroll", function () {
    $(".question").each(function () {
      var etop = $(this).offset().top;
      var diff = etop - $(window).scrollTop();

      if (diff > 100 && diff < 300) {
        reinitState(this);
        moveNext(this);
      }
    });
  });

  function reinitState(e) {
    $(".question").removeClass("active");

    $(".question").each(function () {
      $(this).blur();
    });
    $(e).addClass("active");
    /*$(e).find('input').focus();*/
  }

  // function moveNext() {
  //   $('.input-radio input[type="radio"]').change(function (e) {
  //     alert('Radio Box has been changed!');
  //     $(e).next().click();
  //   });
  // }

  // function moveNext(e) {
  //   var radios = document.forms[$(e)].elements["myradio"];
  //   for (var i = 0, max = radios.length; i < max; i++) {
  //     radios[i].onclick = function () {
  //       alert(this.value);
  //     }
  //   }
  // }
  function rescroll(e) {
    $(window).scrollTo($(e), 200, {
      offset: { left: 100, top: -200 },
      queue: false
    });
  }

  function moveNext(e) {
    $(e).parent().parent().parent().next().click();
  }

  $('.answer').find('.input-radio input[type="radio"]').change(function (e) {
    alert('hello');
    moveNext(this);
  });


  // $(document.forms[0].elements[0]).change(function () {
  //   alert('Radio Box has been changed!');
  // });
});