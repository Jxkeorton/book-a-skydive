const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.querySelectorAll(".btn-delete"); // Select all delete buttons
const deleteConfirm = document.getElementById("deleteConfirm");

// Add event listener to each delete button
deleteButtons.forEach(button => {
    button.addEventListener("click", (e) => {
        let bookingId = e.target.getAttribute("data-booking-id");
        let bookingType = e.target.getAttribute("data-booking-type"); 

        if (bookingType === 'tandem') {
            deleteConfirm.href = `/tandems/delete_booking/${bookingId}/`; // Tandem delete URL
        } else if (bookingType === 'course') {
            deleteConfirm.href = `/course/delete_booking/${bookingId}/`; // Course delete URL
        } else {
            deleteConfirm.href = `/sport/delete_booking/${bookingId}/`; // Default for experienced bookings
        }

        // Show the modal
        deleteModal.show();
    });
});
