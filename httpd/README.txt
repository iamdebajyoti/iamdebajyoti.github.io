Apache was installed on Windows 10 as a service with the following command run via Command Prompt as Administrator
===========================================================================================================================



C:\DEB\Apache24\bin\httpd.exe -k install -f C:\DEB_CloudData\my_git_repos\iamdebajyoti.github.io\httpd\conf\httpd.conf

Location of the Apache Web server software :: C:\DEB\Apache24\bin\httpd.exe 
Command to install the service :: -k install 
Location of the config file :: -f C:\DEB_CloudData\my_git_repos\iamdebajyoti.github.io\httpd\conf\httpd.conf


Location of the config folder :: C:\DEB_CloudData\my_git_repos\iamdebajyoti.github.io\httpd\conf
Location of the log folder :: C:\DEB_CloudData\my_git_repos\iamdebajyoti.github.io\httpd\logs

Location of the web content :: C:\DEB_CloudData\my_git_repos\iamdebajyoti.github.io\httpd\www_local


Define SRVROOT  "C:/DEB/Apache24"
Define WWWROOT "${SRVROOT}/../../DEB_CloudData/my_git_repos/iamdebajyoti.github.io/httpd/www_local"
Define LOGROOT "${SRVROOT}/../../DEB_CloudData/my_git_repos/iamdebajyoti.github.io/httpd/logs"
Define CONFROOT "${SRVROOT}/../../DEB_CloudData/my_git_repos/iamdebajyoti.github.io/httpd/conf"
