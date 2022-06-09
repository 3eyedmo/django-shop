
const form = document.getElementById('register-form');
const email = document.getElementById('email-form');
const password1 = document.getElementById('password-form1');
const password2 = document.getElementById('password-form2');

const emailEmpty = document.getElementById('email-empty');
const emailInvalid = document.getElementById('email-invalid');
const emailRedundant = document.getElementById('email-redundant');

const pass1Empty = document.getElementById('pass1-empty');
const pass1_8_25 = document.getElementById('pass1-8-25');
const pass1Alpha = document.getElementById('pass1-alpha');

const pass2Equal = document.getElementById('pass2-equal');

function fail(elm){
    elm.classList.add('alert-warning');
    elm.classList.remove('text-success');
    let i = elm.firstElementChild;
    i.classList.add('fa-exclamation-circle');
    i.classList.remove('fa-check');
}
function success(elm){
    elm.classList.remove('alert-warning');
    elm.classList.add('text-success');
    let i = elm.firstElementChild;
    i.classList.remove('fa-exclamation-circle');
    i.classList.add('fa-check');
}

function isValidEmail(mail) {
    let emailPattern = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (emailPattern.test(mail)) {
        return true;
    }else {
        return false;
    }
}
function characterCheck(myString){
    let isAnyLowerCase = (myString !== myString.toUpperCase())
    let isAnyUpperCase = (myString !== myString.toLowerCase())
    let re = /[0-9]/;
    let isAnyNumericCase = (re.test(myString))
    return !(isAnyLowerCase && isAnyUpperCase && isAnyNumericCase)
}

let validForm;
let counter = 0;

let emptyEmail = true;
let invalidEmail = true;
let emptyPassword1 = true;
let lt8Password1 = true;
let alphaPassword1 = true;
let notEqualPassword2 = true;




function isValid(){
    // email check
	validForm = false;
    counter = 0;
    if (email.value === "" || email.value == null){
        counter += 1;
        if(!emptyEmail){
            fail(emailEmpty);
            emptyEmail = true;
        }else{
            emptyEmail = false;
        }
    }else {
        success(emailEmpty);
    }
    if (!isValidEmail(email.value)){
        counter += 1;
        if(!invalidEmail){
            fail(emailInvalid);
            invalidEmail = true;
        }else{
            invalidEmail = false;
        }
    }else {
        success(emailInvalid);
    }

    // password1 check
    if (password1.value.length === 0) {
        counter += 1;
        if(!emptyPassword1){
            fail(pass1Empty);
            emptyPassword1 = true;
        }else {
            emptyPassword1 = false;
        }
    }else {
        success(pass1Empty);
    }

    if (password1.value.length < 8 || password1.value.length > 25 ) {
        counter += 1;
        if(!lt8Password1){
            fail(pass1_8_25);
            lt8Password1 = true;
        }else {
            lt8Password1 = false;
        }
    }else {
        success(pass1_8_25);
    }
    if (characterCheck(password1.value)) {
        counter += 1;
        if(!alphaPassword1){
            fail(pass1Alpha)
            alphaPassword1 = true;
        }else {
            alphaPassword1 = false;
        }
    }else {
        success(pass1Alpha);
    }
    // password2 check
    if (password2.value !== password1.value) {
        counter += 1;
        if(!notEqualPassword2){
            fail(pass2Equal);
            notEqualPassword2 = true;
        }else {
            notEqualPassword2 = false;
        }
    }else {
        success(pass2Equal);
    }

    if (counter===0){
        validForm = true
    }
}


form.addEventListener('submit' , (e)=>{
    if (!validForm){
        e.preventDefault();
    }
})
setInterval(isValid , 200);