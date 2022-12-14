const form = document.querySelector('form');
const input = document.querySelectorAll('input');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    input.forEach(input => {
        if(!input.value){
            input.parentElement.classList.add('error-text');
        }else{
            input.parentElement.classList.remove('error-text');
            if (input.type == 'email'){
                if(validateEmail(input.value)){
                    input.parentElement.classList.remove('error-text');
                }else{
                    input.parentElement.classList.add('error-text');
                }
            }
        }
    });
});

const validateEmail = (email) => {
    return String(email)
      .toLowerCase()
      .match(
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      );
  };