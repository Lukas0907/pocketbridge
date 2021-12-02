# PocketBridge

```
// Settings

var secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"; // Replace this with your own secret
var url = "http://localhost:5000";

// Implementation

if (document.URL.match(/^about:reader/)) {
    var f = document.createElement("form");
    f.action = url;
    f.method = "post";

    var c  = document.createElement("textarea");
    c.name = "content";
    c.value = document.querySelector(".container").innerHTML;
    f.appendChild(c);

    var s = document.createElement("input");
    s.name = "secret";
    s.value = secret;
    f.appendChild(s);

    document.body.appendChild(f);

    f.submit();
} else {
    alert("Reader view needs to be toggled first");
}
```

1. Change secret and URL.
2. Create bookmarklet: https://chriszarate.github.io/bookmarkleter/
3. Install [Activate Reader View Add-On](https://addons.mozilla.org/firefox/addon/activate-reader-view/) to force Reader View on any page.
