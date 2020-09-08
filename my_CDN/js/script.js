//to open and close mobile menu on click
function mobileNav() {
  var x = document.getElementById("mobileNav");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else {
    x.className = x.className.replace(" w3-show", "");
  }
}



//for explore menu on click
function explore() {
  var x = document.getElementById("explore");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else {
    x.className = x.className.replace(" w3-show", "");
  }
}



//year for footer
var footeryear = new Date().getFullYear();
document.getElementById("footeryear").innerHTML = footeryear;





// share links
function FBshare() {
  window.open("https://www.facebook.com/sharer.php?title=" + document.title + "u=" + document.URL);
}

function TTshare() {
  window.open("https://twitter.com/intent/tweet?text=" + document.title + "&url=" + document.URL);
}

function WAshare() {
  window.open("https://web.whatsapp.com/send?text=" + document.title + " | " + document.URL);
}

function Emailshare() {
  window.open("mailto:?subject=" + document.title + "&body=" + document.URL);
}



//related tab
function relatedtab(evt, tab) {
  var i, x, tablinks;
  x = document.getElementsByClassName("tab");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < x.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" w3-green", "");
  }
  document.getElementById(tab).style.display = "block";
  evt.currentTarget.className += " w3-green";
}



// User Profile Accordion
function user_acc(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
    x.previousElementSibling.className += " w3-theme-d1";
  } else {
    x.className = x.className.replace("w3-show", "");
    x.previousElementSibling.className =
      x.previousElementSibling.className.replace(" w3-theme-d1", "");
  }
}



// delete confirmation
function toggle_delete() {
  var box = document.getElementById('delete_confirm');
  var word = document.getElementById('delete_button');
  if (box.style.visibility == 'visible') {
    box.style.visibility = 'hidden';
    word.innerHTML = 'Delete';
    word.classList.remove("w3-green");
    word.classList.add("w3-red");
  } else {
    box.style.visibility = 'visible';
    word.innerHTML = 'Cancel';
    word.classList.remove("w3-red");
    word.classList.add("w3-green");
  }
}