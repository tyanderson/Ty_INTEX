/**
 * Created by Charizard on 3/6/2015.
 */
// On page loaded
$(function(){
    // On click of Add to Cart button
    $('#add_to_cart').on('click', function(){
        // If item is not out of stock:
        if($('#quantity').val()!=null){
            // Show the modal
            $('#cart_modal').modal('show');

            // Set item_id
            var item_id = $(this).attr('data-item_id');

            // Send ajax call to add item to cart
            $.ajax({
                // The page to get
                url: '/store/cart/' + item_id + '/' + $('#quantity').val(),
                // Do when successful
                success: function(data){
                    // Display shopping cart
                    $('#cart_modal').find('.modal-body').html(data)
                }
            });
        }
    });
});