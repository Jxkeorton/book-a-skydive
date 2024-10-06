$(document).ready(function(){
    // Trigger modal for editing booking
    $('.edit-booking-btn').click(function(){
        const bookingId = $(this).data('id');
        const fullName = $(this).data('full-name');
        const email = $(this).data('email');
        const weight = $(this).data('weight');
        const height = $(this).data('height');
        const phoneNumber = $(this).data('phone-number');

        const type = $(this).data('type');

        console.log(phoneNumber);

        // Set values in the modal
        $('#full_name').val(fullName);
        $('#email').val(email);
        $('#weight').val(weight);
        $('#height').val(height);
        $('#phone_number').val(phoneNumber);
        $('#booking_id').val(bookingId);

        let url = '';

        if(type === 'course') {
            url = `/course/edit/${bookingId}/`;
        } else {
            url = `/tandems/edit/${bookingId}/`;
        }

        // Dynamically set the form action URL
        $('#editBookingForm').attr(
            'action',
            url
        );

        // Show the modal
        $('#editBookingModal').modal('show');
    });

     // Handle modal close on button or "x" click
     $('#editBookingModal .close, .btn-secondary').click(function() {
        $('#editBookingModal').modal('hide');  // Programmatically hide modal
    });

});