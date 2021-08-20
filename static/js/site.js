function displayLinks() {
    var siteList = document.getElementById("sites");
    var linkList = siteList.getElementsByTagName("a");

    console.log(linkList.length);

    var linkCount = document.getElementById("link-count").innerHTML = linkList.length;
}