
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