script_location = %dp0
cd "C:\DEB\apps\"
"C:\DEB_CloudData\Dropbox\Apps\nuget\nuget.exe" install python -Version 3.9.7 -OutputDirectory .
cd "C:\DEB\apps\python.3.9.7\tools\"
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
cd "C:\DEB\apps\python.3.9.7\tools\Scripts"
pip3.9 -V
pip3.9 install -r requirements.txt