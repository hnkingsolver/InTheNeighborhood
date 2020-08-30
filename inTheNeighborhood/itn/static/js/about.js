// Get the modal
var modal = document.getElementsByClassName('modal');
// Get the button that opens the modal
var btn = document.getElementsByClassName("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close");

// When the user clicks on the button, open the modal

//Hannah
btn[0].onclick = function () {
    modal[0].style.display = "block";
}
//Tanner
btn[1].onclick = function () {
    modal[1].style.display = "block";
}
//Paul
btn[2].onclick = function () {
    modal[2].style.display = "block";
}
//Isaiah
btn[3].onclick = function () {
    modal[3].style.display = "block";
}
//Sher
btn[4].onclick = function () {
    modal[4].style.display = "block";
}
//Michelle
btn[5].onclick = function () {
    modal[5].style.display = "block";
}

// When the user clicks on <span> (x), close the modal

//Hannah
span[0].onclick = function () {
    modal[0].style.display = "none";
}
//Tanner
span[1].onclick = function () {
    modal[1].style.display = "none";
}
//Paul
span[2].onclick = function () {
    modal[2].style.display = "none";
}
//Isaiah
span[3].onclick = function () {
    modal[3].style.display = "none";
}
//Sher
span[4].onclick = function () {
    modal[4].style.display = "none";
}
//Michelle
span[5].onclick = function () {
    modal[5].style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
// var currentIndex;
// function display(index) {
//         modal[index].style.display = "block";
//         currentIndex = index;
// } 

// window.onclick = function (event) {

//     if (event.target == modal[index]) {
//         modal.style.display = "none";
//     }
// }

document.addEventListener("click", function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
});

