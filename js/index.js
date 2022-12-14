const form = document.querySelector('form');
const input = document.querySelectorAll('.login-data form input');

form.addEventListener('submit', (e) =>{
    e.preventDefault();
        if (!input.value){
            input.parentElement.classList.add('error');
        }else{
            input.parentElement.classList.remove('error');
        }
});
