# PocketBridge

With PocketBridge it's possible to store the DOM of the current web page in Pocket.
This way, articles that require a login can be read from Pocket as well.

## Setup

### Backend

1. Deploy the PocketBridge Flask app on your server.
2. Copy `default_settings.py` to `settings.py` and set the shared PocketBridge secret key.

### Bookmarklet

1. Change secret and URL so that they match your settings.
2. Create bookmarklet (e.g. using https://chriszarate.github.io/bookmarkleter/)

```
// Settings

var secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"; // Replace this with your own secret
var url = "http://localhost:5000";  // Replace this with the URL of your PocketBridge instance

// Implementation

var f = document.createElement("form");
f.action = url;
f.method = "post";

// Convert all images to JPEG via the pocket proxy
// This is necessary for Pocket on the Kobo ereader. Otherwise it can be removed.
for (let img of document.querySelectorAll("img")) {
    img.src = "https://pocket-image-cache.com//filters:format(jpg)/" + img.src;
    img.removeAttribute("srcset");
}

var c = document.createElement("textarea");
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
