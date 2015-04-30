msg="username=ismelser&password=5260&submit=Login\n---\n"
url="https://cas-us.stevenson.pirates/auth/perfigo_weblogin.jsp?cm=ws32vklm&uri=http%3A%2F%2Fgoogle.com%2F"
echo -e ${msg}|lynx -useragent="Lynx" ${url} -post_data