$(document).ready(function() {

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

$("button.js-addbutton").each(function (index){
  var pk = $(this).data("pk");

  $(this).click(function (){
    $.ajax({
      url: "/cart/add_product_to_cart",
      data: {'pk': pk},
      type: "POST",
        beforeSend: function ( xhr ) {
          xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      },
      success: function(data, textStatus, jqXHR) {
        console.log(data.product)
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.log(testStatus + " error: " + errorThrown)
      }
    }); 
  });
});

});
