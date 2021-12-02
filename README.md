# PocketBridge

```
var secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"; // Replace this with your own secret

var f = document.createElement("form");
f.action = "http://localhost:5000";
f.method = "post";

var c  = document.createElement("textarea");
c.name = "content";
c.value = document.querySelector(document.URL.match(/^about:reader/) ? ".container" : "body").innerHTML;
f.appendChild(c);

var s = document.createElement("input");
s.name = "secret";
s.value = secret;
f.appendChild(s);

document.body.appendChild(f);

f.submit();
```

Create bookmarklet: https://chriszarate.github.io/bookmarkleter/
