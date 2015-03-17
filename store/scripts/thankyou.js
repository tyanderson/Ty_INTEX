/**
 * Created by Charizard on 3/6/2015.
 */
// On page loaded
$(function(){
    // On click of Delete button
    $.ajax({
        // The page to get
        url: '/store/cart.view',
        // Do when successful
        success: function(data){
            // Display shopping cart
            $('#receipt').html(data);
            $('.delete').css('display', 'none');
        }
    });
});