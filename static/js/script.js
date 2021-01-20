var link = location.pathname;
var itemHref = document.getElementsByClassName('nav-link');
for(var i = 0; i < itemHref.length; i++) {
    if (itemHref[i].getAttribute('href') == link) {
        var item = document.getElementsByClassName('nav-item');
        item[i].setAttribute('class', 'nav-item active');
    }
}