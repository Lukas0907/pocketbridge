# PocketBridge

```
var secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"; // Replace this with your own secret

if (document.URL.match(/^about:reader/)) {
    var f = document.createElement("form");
    f.action = "https://pocketbridge.superwayne.org";
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

Create bookmarklet: https://chriszarate.github.io/bookmarkleter/
