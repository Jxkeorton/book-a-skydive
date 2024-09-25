$(document).ready(function(){
    // Trigger modal for editing booking
    $('.edit-booking-btn').click(function(){
        const bookingId = $(this).data('id');
        const fullName = $(this).data('full-name');
        const email = $(this).data('email');
        const weight = $(this).data('weight');
        const height = $(this).data('height');

        // Set values in the modal
        $('#full_name').val(fullName);
        $('#email').val(email);
        $('#weight').val(weight);
        $('#height').val(height);
        $('#booking_id').val(bookingId);

        // Show the modal
        $('#editBookingModal').modal('show');
    });

    // Handle form submission
    $('#editBookingForm').on('submit', function(e){
        e.preventDefault(); // Prevent default form submission

        const url = editBookingUrl // Replace the placeholder

        // Send an AJAX POST request to update the booking
        $.ajax({
            type: "POST",
            url: url,
            data: $(this).serialize(),
            success: function(response) {
                // Close the modal and refresh the page or update the list
                $('#editBookingModal').modal('hide');
                location.reload(); // Refresh to see the changes (or update the list dynamically)
            },
            error: function(error) {
                alert("An error occurred while updating the booking.");
            }
        });
    });
});