/**
 * Created by Charizard on 3/4/2015.
 */

// On page ready
$(function(){
    // Fill in the modal with submitted login data
    $('#login_form').ajaxForm(function(data){
        $('.modal-body').html(data);
    });
});