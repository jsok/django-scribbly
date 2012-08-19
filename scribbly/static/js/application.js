var Climbcare = (function() {
    var urls = {
        addToCart: "/cart/add_product_to_cart",
        removeFromCart: "/cart/remove_product_from_cart"
    };

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

    function BindCartModifyButton(selector) {
        $(selector).each(function (index){
            $(this).click(function () {
                var form = $(this).closest('form');
                var data = serializeJSON(form);
                AddToCart(data);

                // Stop submission of the form.
                return false;
            });
        });
    }

    function AddToCart(data) {
        $.ajax({
            url: urls.addToCart,
            data: data,
            type: "POST",
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            error: function(jqXHR, testStatus, errorThrown) {
                // Todo: Notify if fail
            },
            success: function(data, status, jqXHR) {
                // Update the button displayed next to the product
                var buttonDiv = "div.catalog-product-" + data["product-id"]
                $(buttonDiv).replaceWith(data["button-div"])
                $(".dropdown-toggle").dropdown();

                // Bind update button.
                BindCartModifyButton("button.js-cartmodifybutton");
            }
        }); 
    }

    return {
        InitCatalog: function() {
            BindCartModifyButton("button.js-cartmodifybutton");
        }
    };
})();

$(document).ready(function() {
    Climbcare.InitCatalog();
});
