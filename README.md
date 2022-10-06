# PocketBridge

```
// Settings

var secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"; // Replace this with your own secret
var url = "http://localhost:5000";

// Implementation

var f = document.createElement("form");
f.action = url;
f.method = "post";

// Convert all images to JPEG via the pocket proxy
for (let img of document.querySelectorAll("img")) {
    img.src = "https://pocket-image-cache.com//filters:format(jpg)/" + img.src;
    img.removeAttribute("srcset");
}

var c  = document.createElement("textarea");
c.name = "content";
if (document.URL.match(/^about:reader/)) {
    c.value = document.querySelector(".container").innerHTML;
} else {
    c.value = document.body.innerHTML;
}
f.appendChild(c);

var s = document.createElement("input");
s.name = "secret";
s.value = secret;
f.appendChild(s);

document.body.appendChild(f);

f.submit();
```

1. Change secret and URL.
2. Create bookmarklet: https://chriszarate.github.io/bookmarkleter/
3. Install [Activate Reader View Add-On](https://addons.mozilla.org/firefox/addon/activate-reader-view/) to force Reader View on any page.
