
$("#form_filter").submit(function() {
      if ($('#id_item_type').val() == 'Inventory'  & $('#id_period_end_accrual').val()=='True') {
        //$('#error_message').text ('For an Inventory Item, we cannot enable "Period-end Accrual"');
        $('#myModal').modal('show');
        return false;

      }
      else {    
        
        return true;
      }
    });

$("#add-field").click(function() {
        $('#add-field-form').toggle(100)
    });

// Toggle Sidebar and increase width of main accordingly
$('.sidebar-toggle').click(function(event) {
	/* Act on the event */
	console.log ($(".sidebar").attr('display'));
	$ ('.sidebar').toggle();
	if($('.sidebar').css('display') == 'none') {
		
		$(".main").attr("class", "col-sm-9 col-sm-offset-0 col-md-12 col-md-offset-0 main");
	} else {
		$(".main").attr("class", "col-sm-8 col-sm-offset-3 col-md-9 col-md-offset-3 main");
	}
	
});