// Link Counter
function displayLinks() {
    var siteList = document.getElementsByClassName("links");

    for (i = 0; i < siteList.length; i++) {
        linkList = siteList[i].getElementsByTagName("a");
    }

    var linkCount = document.getElementById("link-count").innerHTML = linkList.length;
}

// Collapse 
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}