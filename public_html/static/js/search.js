function search() {
    var input, filter, ul, li, span, a, i, txtValue, title;
    input = document.getElementById("srch");
    filter = input.value.toLowerCase();

    var siteList = document.getElementsByClassName("links").item(0);
    ul = siteList.getElementsByClassName("sites");
    //li = ul.getElementsByTagName("li");

    console.log(ul.length)
    for (i = 0; i < ul.length; i++) {
        topics = ul.item(i);
        li = topics.getElementsByTagName("li");
        
        for (j = 0; j < li.length; j++) {
            span = li[j].getElementsByTagName("span")[0];
            txtValue = span.textContent || span.innerText;
            a = span.firstChild;
            title = a.title;
            if ((txtValue.toLowerCase().indexOf(filter) > -1) || (title.toLowerCase().indexOf(filter) > -1)) {
                li[j].style.display = "";
            } else {
                li[j].style.display = "none";
            }
        }
    }
}