const email = document.getElementById('email')
const password = document.getElementById('password')
const form = document.getElementById('form')

form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (email.value === '') {
        alert('Email must be provided')
    } else if (password.value === '') {
        alert('Provide your password')
    } else if (password.value.length < 6) {
        alert('password must be more than 6')
    }
})
