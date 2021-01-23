$(document).ready(function () {

  var container = $(this).find(".form");
  highlighMenu(this)
  hideButton(this)

  $(container)
    .find(".input-radio")
    .not(".input-block input")
    .on("click", function () {
      rescroll(this);
    });

  $(window).on("scroll", function () {
    $(".block").each(function () {
      var etop = $(this).offset().top;
      var diff = etop - $(window).scrollTop();

      if (diff > 100 && diff < 300) {
        reinitState(this);
        // moveNext(this);
      }
    });
  });

  $('.answer').find('.input-radio input[type="radio"]').change(function (e) {
    moveNext(this);
  });

  function reinitState(e) {
    $(".block").removeClass("active");

    $(".block").each(function () {
      $(this).blur();
    });
    $(e).addClass("active");
  }

  function rescroll(e) {
    $(window).scrollTo($(e), 200, {
      offset: { left: 100, top: -200 },
      queue: false
    });
  }

  function moveNext(e) {
    $(e).parent().parent().parent().next().click();
  }

  function highlighMenu(e) {
    // this will get the full URL at the address bar
    var url = window.location.href;
    $(".nav-item").each(function () {
      // checks if its the same on the address bar
      if (url.indexOf("?type=1") > -1 || url.indexOf("?type=2") > -1 || url.indexOf("?type=3") > -1){
        //document.getElementById("menu1").style.display = "none";
      }
    });
  };
  function hideButton(e) {
    // this will get the full URL at the address bar
    var url = window.location.href;
    if (url.indexOf("?type=mod") > -1) {
      document.getElementById("buttonUpdate").style.display = "none";
    }
  }
});