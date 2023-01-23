$(document).ready(function () {
  $("#form").on("submit", function (e) {
    //var selected_days = $("input[type='checkbox'][name='days']:checked").val();
    var selected_days = $(".form-check-input:checkbox:checked")
      .map(function () {
        return $(this).val();
      })
      .get();
    var session_start = document.getElementById("session_start").value;
    var session_end = document.getElementById("session_end").value;

    var entry = {
      selected_days: selected_days,
      slot_start: session_start,
      slot_end: session_end,
    };
    fetch(`${window.origin}/profile/create-slot`, {
      method: "POST",
      body: JSON.stringify(entry),
      headers: new Headers({
        "content-type": "application/json",
      }),
    })
      .then((res) => res.json())
      .then((res) => {
        console.log(res);
        $("#selected_days").text(res.selected_days).show();
        $("#start_slot").text(res.slot_start).show();
        $("#end_slot").text(res.slot_end).show();
      })
      .catch((e) => console.log(e));
    e.preventDefault();
  });
});
