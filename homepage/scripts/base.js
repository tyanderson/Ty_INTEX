/**
 * Created by Charizard on 3/4/2015.
 */
// WHen page is ready:
$(function(){
    // Toggles visibility of modal on #login click
    $('#login').on('click', function(){
        // Show the modal
        $('#login_form').modal('show');
        // Get login form with ajax
        $.ajax({
            // The page to get
            url: '/homepage/login',
            // Do when successful
            success: function(data){
                // Set the modal body's html to be 'data'
                $('#login_form').find('.modal-body').html(data)
            }
        });
    });

    // Open cart
    $('#cart_button').on('click', function() {
        showCart();
    })

    // Search
    $('#search_input').keypress(function(e){
        // Get search text
        var text = '/store/index.search/' + $('#search_input').val() + String.fromCharCode(e.which) + '/';
        // If 'Enter' key is pressed
        if(e.which == 13) {
            // Ajax
            e.preventDefault();
            $.ajax({
                url: text,
                type: "POST",
                success: function(data){
                    $('#items').html(data);
                }
            });
        };
        // Ajax
        $.ajax({
            url: text,
            type: "POST",
            success: function(data){
                $('#items').html(data);
            }
        });
    })

    // Show cart
    function showCart(){
        $('#cart_modal').modal('show');
        // Get login form with ajax
        $.ajax({
            // The page to get
            url: '/store/cart.view/',
            // Do when successful
            success: function(data){
                // Set the modal body's html to be 'data'
                $('#cart_modal').find('.modal-body').html(data)
            }
        });
    }
})