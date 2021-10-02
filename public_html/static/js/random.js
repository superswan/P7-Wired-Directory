function sampleSite() {
    var siteList = document.getElementsByClassName("links");

    for (i = 0; i < siteList.length; i++) {
        linkList = siteList[i].getElementsByTagName("a");
    }

    var linkCount = document.getElementById("link-count").innerHTML = linkList.length;

    var randomItem = linkList[Math.floor(Math.random()*linkList.length)];
    const randomLink = linkList[Math.floor(Math.random() * linkList.length)]
    url = randomLink.href

    console.log(randomLink)
    window.open(url, '_blank').focus();
}