// Global
var siteList = document.getElementsByClassName("links");

// Link Counter
function displayLinks() {
    for (i = 0; i < siteList.length; i++) {
        linkList = siteList[i].getElementsByTagName("a");
    }

    var linkCount = document.getElementById("link-count").innerHTML = linkList.length;
}

// Link Counter Topic Specific
function displayLinksTopic() {
  siteDiv = siteList.item(0);
  ul = siteDiv.getElementsByClassName("content")
  topicLabels = document.getElementsByClassName("topic-count");
  for (i = 0; i < ul.length; i++) {
    
    linkList = ul[i].getElementsByTagName("a");
    topicCount = linkList.length;
    topicLabels.item(i).innerHTML = "(" + topicCount + ")"
  }


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