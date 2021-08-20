function search() {
    var input, filter, ul, li, span, a, i, txtValue, title;
    input = document.getElementById("srch");
    filter = input.value.toUpperCase();
    ul = document.getElementById("sites");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        span = li[i].getElementsByTagName("span")[0];    
        txtValue = span.textContent || span.innerText;
        a = span.firstChild;
        title = a.title;
        if ((txtValue.toUpperCase().indexOf(filter) > -1) || (title.toUpperCase().indexOf(filter) > -1)) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
    }