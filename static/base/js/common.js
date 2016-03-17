
// Function to reset form Errors
function resetFormErrors() {
   // Cleaning up for field errors
   $('.errors').remove();
   $('#login-form').find('.has-error').removeClass('has-error');
   $('#login-form').find('.invalid').removeClass('invalid');
   // Cleaning up for non-field errors
   $('.non_field_errors').empty();
}

// Function to Display form errors in the form for AJAX calls
function getAndShowFormErrors(xhr, status, error, form_id) {
	var form_errors = xhr.responseJSON['errors'];
    form = $('#' + form_id);

	var i = 0;

	if('__all__' in form_errors) {
		var non_field_errors = form_errors['__all__'];
		var div = $('<div class="non_field_errors"/>');
		for(i = 0; i < non_field_errors.length; i++) {
			div.append('<small class="error">' + non_field_errors[i] + '</small>');
		}
		$(form).prepend(div);
		delete form_errors['__all__'];
	}
	for(var field_name in form_errors) {
		$('#id_' + field_name + '_container').addClass('has-error');
		$('#id_' + field_name).addClass('invalid');
		var field_errors_div = $('<div class="errors"/>');
		for(i = 0; i < form_errors[field_name].length; i++) {
			field_errors_div.append('<small class="error">' + form_errors[field_name][i] + '</small>');
		}
		$('#id_' + field_name + '_container').append(field_errors_div);
	}
}

UserLogin = (function() {
    function login(e) {
       e.preventDefault();
       var form = document.getElementById('login-form');
       var form_data = new FormData(form);
       var url = $(form).attr('action');

       $.ajax({
           url : url,
           type : 'POST',
           dataType: 'json',
           data : form_data,
           processData: false,
           contentType: false,
           success: function(data, status, xhr) {
               console.log('success');
               location.href = '/account/home/';
           },
           error: function(xhr, status, error) {
               //console.log(xhr);
               resetFormErrors();
               getAndShowFormErrors(xhr, status, error, 'login-form');
           }
       });
   }
   function init() {
       $('#login-btn').on('click', login);
   }
   return {
       'init' : init,
   };
})();

UserSignup= (function() {
    function login(e) {
       e.preventDefault();
       var form = document.getElementById('signup-form');
       var form_data = new FormData(form);
       var url = $(form).attr('action');

       $.ajax({
           url : url,
           type : 'POST',
           dataType: 'json',
           data : form_data,
           processData: false,
           contentType: false,
           success: function(data, status, xhr) {
               console.log('success');
               document.getElementById('signup-form').reset();
               /*
                * For now alerting the user about the email sent,
                * I will be using a flash message here. 
                *
                **/
               alert('Thanks for signing up. Please verify your email, by clicking on the verification link that we sent you to your email. We have sent your details to the moderator/admin for approval.');
           },
           error: function(xhr, status, error) {
               //console.log(xhr);
               resetFormErrors();
               getAndShowFormErrors(xhr, status, error, 'signup-form');
           }
       });
   }
   function init() {
       $('#signup-btn').on('click', login);
   }
   return {
       'init' : init,
   };
})();
