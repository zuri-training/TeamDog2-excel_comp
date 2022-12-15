const email = document.getElementById('email')
const password = document.getElementById('password')
const form = document.getElementById('form')

form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (email.value === '') {
        alert('Input your email');
        validateEmail();
    } else if (password.value === '') {
        alert('Provide your password')
    } else if (password.value.length < 6) {
        alert('password must be more than 6')
    }
})

const validateEmail = (email) => {
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (email.value.match(validRegex)) {
        alert("Valid email address!");
        password.focus();
        return true;
    } else {
        alert("Invalid email address!");
        email.focus();
        return false;
    }
};
