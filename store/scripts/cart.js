/**
 * Created by Charizard on 3/6/2015.
 */
// On page loaded
$(function(){
    // On click of Delete button
    $('.delete').on('click', function(){
        // Send ajax call to refresh cart modal
        $.ajax({
            // The page to get
            url: '/store/cart.delete/' + $(this).attr('data-item_id'),
            // Do when successful
            success: function(data){
                // Display shopping cart
                $('#cart_modal').find('.modal-body').html(data)
            }
        });
    });
});