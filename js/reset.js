const email = document.getElementById('email');

const validateEmail = (email) => {
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (email.value.match(validRegex)) {
        alert("Valid email address!");
        return true;
    } else {
        alert("Invalid email address!");
        email.focus();
        return false;
    }
};