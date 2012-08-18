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

function serializeJSON(form) {
  var params = {};
  jQuery.each(jQuery(form).serializeArray(), function(index,value) {
    params[value.name] = value.value;
  });
  return params;
}

function inform_product_added_to_cart(data, status, jqXHR) {

      // Change the Add button to an Update button
      var buttonid = "button#" + data["product-id"]
      var buttondiv = $(buttonid).closest("div")
      $(buttondiv).replaceWith(data["button-div"])
      buttonid = "button#" + data["product-id"]
      $(buttonid).dropdown()
}

function add_product_to_cart(data) {
    $.ajax({
      url: "/cart/add_product_to_cart",
      data: data,
      type: "POST",
      beforeSend: function (xhr) {
          xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      },
      error: function(jqXHR, testStatus, errorThrown) {
        // Todo: Notify if fail
      },
      success: inform_product_added_to_cart,
    }); 
}

$("button.js-addbutton").each(function (index){
  $(this).click(function (){
    var form = $(this).closest('form');
    var data = serializeJSON(form);
    add_product_to_cart(data);
  });
});

}); // document.ready
