
$(".digit").on('click', function() {
  var num = ($(this).clone().children().remove().end().text());
  document.getElementById("input").value += num.trim();
  
});

$('.fa-long-arrow-left').on('click', function() {
  var strng=document.getElementById("input").value;
  document.getElementById("input").value=strng.substring(0,strng.length-1)
});


$("#call").on('click', function() {

  var display = document.getElementById("input").value 
  var string = display;
  var ussd_string = {"USSD_STRING": string}

  $.ajax({
      type: "POST",
      url: "/get_post_json",
      async: false,
      contentType: "application/json",
      data: JSON.stringify(ussd_string),
      dataType: "text",
      success: function(){
        // alert("success")
        swal("Successfully sent", "Thank you!", "success");
      },
      error: function(){
        // alert("error")
        swal("An error occured", "Check your connection and try again", "error");
      }
  });
});