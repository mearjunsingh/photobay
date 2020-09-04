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



//category filter in discover page
// Dropdown
function cat_filter_drop() {
  var x = document.getElementById("cat_filter");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else {
    x.className = x.className.replace(" w3-show", "");
  }
}
// Filter
function cat_filter() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("cat_filter_input");
  filter = input.value.toUpperCase();
  div = document.getElementById("cat_filter");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}



//status filter in discover page
// Dropdown
function stat_filter_drop() {
  var x = document.getElementById("stat_filter");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else {
    x.className = x.className.replace(" w3-show", "");
  }
}



//ort filter in discover page
// Dropdown
function ort_filter_drop() {
  var x = document.getElementById("ort_filter");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else {
    x.className = x.className.replace(" w3-show", "");
  }
}




// share links
function FBshare() {
  window.open("https://www.facebook.com/sharer.php?title="+document.title+"u="+document.URL);
}

function TTshare() {
  window.open("https://twitter.com/intent/tweet?text="+document.title+"&url="+document.URL);
}

function WAshare() {
  window.open("https://web.whatsapp.com/send?text="+document.title+" | "+document.URL);
}

function Emailshare() {
  window.open("mailto:?subject="+document.title+"&body="+document.URL);
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