const hamburgerIcon = document.getElementById("hamburger-id");
const timesIcon = document.getElementById("times-id");
const responsiveMenu = document.getElementById("navbar-class");
let menuOpen = false;

hamburgerIcon.addEventListener("click", (event)=>{
    elm = event.target
    elm.classList.toggle('hide-icon');
    timesIcon.classList.toggle('hide-icon');
    responsiveMenu.classList.toggle('hide-menu');
    menuOpen = true;
});

timesIcon.addEventListener("click", (event)=>{
    elm = event.target
    elm.classList.toggle('hide-icon');
    hamburgerIcon.classList.toggle('hide-icon');
    responsiveMenu.classList.toggle('hide-menu');
    menuOpen = false;
});







