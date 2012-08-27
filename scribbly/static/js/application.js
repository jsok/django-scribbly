var Climbcare = (function() {
    var urls = {
        addToCart: "/cart/add_product_to_cart",
        productSearch: "/api/product/search",
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

    function DisableSubmitOnQuantity(selector) {
        $(selector).each(function (index){
          $(this).keypress(function (event) {
            // Disable enter key from POSTing form
            if (event.which == 13)
              event.preventDefault();
          });
        });
    }

    function BindCartRemoveButtons(selector) {
        $(selector).each(function (index){
            BindCartRemoveButton(selector);
        });
    }

    function BindCartRemoveButton(selector) {
        $(selector).unbind('click');
        $(selector).click(function () {
            var data = {
              "product-id": $(this).data("product-id"),
              "quantity": 0
            }
            UpdateCart(data);

            // Stop submission of the form.
            return false;
        });
    }

    function BindCartModifyButtons(selector) {
        $(selector).each(function (index){
            BindCartModifyButton(selector);
        });
    }

    function BindCartModifyButton(selector) {
        $(selector).unbind('click');
        $(selector).click(function () {
            $(this).button('loading')
            var form = $(this).closest('form');
            var data = serializeJSON(form);
            UpdateCart(data)

            // Stop submission of the form.
            return false;
          });
    }

    function UpdateCartIcon(selector, innerHtml) {
      $(selector).replaceWith(innerHtml);
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
                var buttonDivSelector = "div.catalog-product-" + data["product-id"]
                $(buttonDivSelector).replaceWith(data["button-div"])
                $(".dropdown-toggle").dropdown();

                var buttonDiv = $(buttonDivSelector)
                buttonDiv.siblings("input.catalog-quantity").val(data["quantity"]);

                // Bind update button.
                BindCartModifyButton(buttonDiv.find("button.js-cartmodifybutton"));
                BindCartRemoveButton(buttonDiv.find("a.js-cartremovebutton"));
                UpdateCartIcon("li.js-cart-nav-item", data["cart-nav-item"]);
            }
        }); 
    }

    function BindSearchBox(selector) {
      $(selector).typeahead({
        source: function(query, process) {
          $.ajax({
            url: urls.productSearch,
            data: { 'q': query },
            beforeSend: function (xhr) {
              xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            error: function(jqXHR, testStatus, errorThrown) {
              // Todo: Notify if fail
            },
            success: function(data, status, jqXHR) {
              names = []
              // Extract the names from all results
              $(data.objects).each(function(result) {
                names.push(this["name"])
              });
              // Use typeahead callback to return results
              process(names)
            }
          })
        }
      });

    }

    return {
        InitCatalog: function() {
            BindCartModifyButton("button.js-cartmodifybutton");
            BindCartRemoveButton("a.js-cartremovebutton");
            DisableSubmitOnQuantity("input.catalog-quantity");
        },
        InitSearch: function() {
            BindSearchBox("input.js-product-search");
        }
    };
})();

$(document).ready(function() {
    Climbcare.InitCatalog();
    Climbcare.InitSearch();
});
