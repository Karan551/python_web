console.log("This first js file in django project.")
// ---------------To hide alert after 5 seconds--------
setTimeout(() => {
    $("#alert").hide()
  }, 5000);

//-----------To show password when user click on check box------
const checkBox = document.querySelector("#passwordCheckBox");
const passwordInput = document.querySelector("#login-password");
function showPassword() {
  if (checkBox.checked) {
    passwordInput.type = "text";
  } else {
    passwordInput.type = "password";
  }
}
// apply event on check box when user click.
checkBox.addEventListener("click", showPassword);


// ----------To check that user password and current password are equal or not and User password or Current Password length is greater than 4--------.
      
      
      /// -------------with jquery-------------
      $(document).ready(function () {
        $("#signup-btn").click(function (event) {
          if ($("#user-password").val() !== $("#confirm-password").val()) {
              // To prevent submit a form
            event.preventDefault();
             // To reset a form
            $("#sign-up-form")[0].reset();
            alert("Please Type current Password and user-password same.");
          } else if ($("#user-password").val().length <= 4 || ("#confirmPassword").val().length <= 4) {
            // To prevent submit a form
            event.preventDefault();
            // To reset a form
            $("#sign-up-form")[0].reset();
            alert(
              "Please Type current Password length is greater than 4 and user password length is greater than 4."
            );
          }
        });
      });