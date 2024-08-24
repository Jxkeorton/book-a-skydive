const editButtons = document.getElementsByClassName("btn-edit");
const jumpType = document.getElementById("id_jump_type");
const bookingForm = document.getElementById("bookingForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let bookingId = e.target.getAttribute("data-booking-id");
    let currentJumpType = e.target.getAttribute("data-current-type");

    // Pre-fill the form with the current jump type
    jumpType.value = currentJumpType;

    // Change the button text to "Update"
    submitButton.innerText = "Update";

    // Set the form action to the edit_booking endpoint with the correct booking ID
    bookingForm.setAttribute("action", `/edit_booking/${bookingId}/`);
  });
}
