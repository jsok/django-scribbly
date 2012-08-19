var Climbcare = (function() {
    var urls = {
        addToCart: "/cart/add_product_to_cart",
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

    function BindCartRemoveButton(selector) {
        $(selector).each(function (index){
            $(this).click(function () {
                var data = {
                  "product-id": $(this).data("product-id"),
                  "quantity": 0
                }
                UpdateCart(data);
            });
        });
    }

    function BindCartModifyButton(selector) {
        $(selector).each(function (index){
            $(this).click(function () {
                var form = $(this).closest('form');
                var data = serializeJSON(form);
                UpdateCart(data);

                // Stop submission of the form.
                return false;
            });
        });
    }

    function UpdateCart(data) {
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

                $(buttonDiv).siblings("input.catalog-quantity").val(data["quantity"]);

                // Bind update button.
                BindCartModifyButton("button.js-cartmodifybutton");
                BindCartRemoveButton("a.js-cartremovebutton");
            }
        }); 
    }

    return {
        InitCatalog: function() {
            BindCartModifyButton("button.js-cartmodifybutton");
            BindCartRemoveButton("a.js-cartremovebutton");
        }
    };
})();

$(document).ready(function() {
    Climbcare.InitCatalog();
});
