$(document).ready(function(){
    //Function to hide all animal pictures
    var milestoneNum = 1;

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
        if ($(this).val() === 'Career') {
            $("#penguin").show();
            $("#animal_name").val("Penguin");
        } else if ($(this).val() === 'Spiritual') {
            $("#horse").show();
            $("#animal_name").val("Horse");
        } else if ($(this).val() === 'Education') {
            $("#owl").show();
            $("#animal_name").val("Owl");
        }
    });

    $("#plus").click(function() {
        if (milestoneNum < 5) {
            milestoneNum++;
            $('#milestone_insert').before('<div class="form-group"><label for="milestone'+milestoneNum+'" class="col-sm-2 control-label">Milestone #'+milestoneNum+'</label><div class="col-sm-9"><input class="form-control milestone" type="text" placeholder="Ex: Run 2 laps around the track" name="milestone'+milestoneNum+'" /></div>');
        }
        if (milestoneNum === 5) {
            $('#plus').hide();
        }

    });
});
