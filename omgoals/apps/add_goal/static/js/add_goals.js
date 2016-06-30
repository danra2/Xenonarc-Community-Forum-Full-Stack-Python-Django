$(document).ready(function(){
    //Function to hide all animal pictures
   (function ( $ ) {
        $.fn.hideAnimals = function() {
            $("#penguin").hide();
            $("#horse").hide();
            $("#owl").hide();
        }
    })( jQuery );
    //Hide animal pictures initially
    $("#animals").hideAnimals();

    //Display animal picture with corresponding category
    $("#category").change(function() {
        $("#animals").hideAnimals();
        if ($(this).val() === 'career') {
            $("#penguin").show();
            $("#animal_name").val("Penguin");
        } else if ($(this).val() === 'spiritual') {
            $("#horse").show();
            $("#animal_name").val("Horse");
        } else if ($(this).val() === 'education') {
            $("#owl").show();
            $("#animal_name").val("Owl");
        }
    })

});
