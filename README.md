# Instagram-Downloader

Download Instagram profiles

Things you need:
* curl: https://curl.haxx.se/download.html
* cacert.pem: https://curl.haxx.se/docs/caextract.html

How to use:
```Go to an instagram profile
Open dev tools
Go to network tab
Scroll down and hit see more
You'll see a request that says ?query_id=XXXXXXXXXXXXXXXX&variables=XXXXXXXXXX
Copy the query_id (X's after the equal sign and before the ampersand) and paste it into "GIMME" on line 3
You'll need to have cacert and curl in the same dir or on the PATH
```

Eventually probably should move to a system that makes more small requests instead of one giant request. Biggest account I've tried this on has 750 posts and that worked.
