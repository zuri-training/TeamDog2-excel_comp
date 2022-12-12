function toggleNav() {
    var x = document.getElementsByTagName("nav")[0];
    if (x.className === "bottomNav") {
       x.className += " openNav";
    } else {
       x.className = "bottomNav";
    }
 }
 document.querySelector(".hamburger").addEventListener("click", toggleNav);