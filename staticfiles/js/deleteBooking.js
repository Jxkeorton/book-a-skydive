const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let bookingId = e.target.getAttribute("data-booking-id");
        // Set the delete confirmation link to the correct URL
        deleteConfirm.href = `/sport/delete_booking/${bookingId}/`;
        deleteModal.show();
    });
}
