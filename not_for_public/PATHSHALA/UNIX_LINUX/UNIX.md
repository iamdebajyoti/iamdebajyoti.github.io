
### [NIX] "ls" command output 4-digit year
> **In bash -**
>
> Displays the date and time in YYYY-MM-DD HH:MM format for all files, ensuring the 4-digit year is always present.
> ```shell
> ls -l --time-style=long-iso
> ```
> #### Full ISO 8601 format:
> ```shell
> ls -l --time-style=full-iso
> ```
> #### Custom Format (4-digit year + time):
> ```shell
> ls -l --time-style=+"%Y-%m-%d %H:%M:%S"
> ls -ld --time-style=+"%Y-%m-%d-%H-%M-%S"
> ```
> #### Using stat (If ls options are not supported):
> ```shell
> stat -c "%y %n" *
> stat -c "%y %N" *
> ```
>
> ##### By default, ls -l shows Month Day Time for files within the last six months, and Month Day Year for older files.
> ##### The --time-style options work on GNU ls, but often fail on FreeBSD, Solaris, or older AIX implementations.
> 
> 
> ```bash
> $  ls -l --time-style=
> ls: ambiguous argument ‘’ for ‘time style’
> Valid arguments are:
>   - [posix-]full-iso
>   - [posix-]long-iso
>   - [posix-]iso
>   - [posix-]locale
>   - +FORMAT (e.g., +%H:%M) for a 'date'-style format
> Try 'ls --help' for more information.
> ```

### awk
> ### awk + match + regex
> 
> [Google AI Mode](https://share.google/aimode/0JGrgzYEPAhjoSMmq)


### man
### export man pages as html
```
man <command_name> | awk 'BEGIN {print "<html><body><pre>"} {gsub(/&/, "&amp;"); gsub(/</, "&lt;"); gsub(/>/, "&gt;"); print} END {print "</pre></body></html>"}' > <command_name>.html
```

### [AIX] check RAM, CPU - basic details
```
date; hostname; echo; echo; prtconf -m; echo; echo; svmon -G -O unit=GB; echo; echo; lsattr -El mem0; echo; echo;
```
#### For all CPU details and RAM
```
prtconf -ckLmsv
```

### [RHEL] check CPU performance
```
top -b -n 3 1 | tee $(date +%Y%m%d-%H%M)__top_output.out
mpstat -P ALL | tee $(date +%Y%m%d-%H%M)__mpstat_output.out
uptime | tee $(date +%Y%m%d-%H%M)__uptime_output.out
sar -u 5 | tee $(date +%Y%m%d-%H%M)__sar_output.out
ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10 | tee $(date +%Y%m%d-%H%M)__top_10_ps_sorted_output.out
ps -eo pcpu,pid,user,args | sort -k 1 -r | tee $(date +%Y%m%d-%H%M)__all_ps_sorted_output.out
ps -eo user | sort -k 1 -r | uniq -c | tee $(date +%Y%m%d-%H%M)__all_ps_per-user-grouped_output.out
lscpu
sar -q
sar -q <<min(s)>> <<loops>> -o <<output file name>>
sar -q 1 10 -o <<output file name>>
sar -f /var/log/sa/sa<<date>> -s hh:mm:ss -e hh:mm:ss <<file name>>
sar -q -u -w -P ALL -f /var/log/sa/sa<<date>> -s hh:mm:ss -e hh:mm:ss -i 60


zip cpu_perf_report_$(date +%Y%m%d-%H%M).zip <> <> <>
```

### [RHEL] Microsoft Defender Exclusion
> #### For the full exclusion list ( run as any "logged on" user)
> ```
> sudo mdatp exclusion list
> ```
> #### For the full exclusion statistics ( run as any "logged on" user)
> ```
> sudo mdatp exclusion list | grep -i "Excluded" | uniq -c
> ```
> #### For the filtered exclusion list ( run as any "logged on" user)
> ```
> sudo mdatp exclusion list | grep -i "path"
> sudo mdatp exclusion list | grep -i "process name"
> ```

### [RHEL] To check if a server is physical or virtual
> Run as root
```
dmidecode -t system
```
### Network analysis and investigation
```
netstat -tunlp | more
netstat -nr
ip route get << ip address>>
ping <<hostname>>
nslookup <<fqdn>>
```
*fqdn = fully qualified domain name*

### [AIX] OS version and patch details
```
oslevel -s
uname -a
```

### [RHEL]

> To test the integrity of a .tar.gz file without extracting its contents to your disk, run the command  in your terminal. This forces the system to simulate decompression and read through the entire archive structure; any corrupt segments or truncated files will trigger an immediate error message. [1, 2, 3, 4, 5]  
> _Quick Testing Methods_
> Choose the command that best fits your exact testing needs: 
> 
> * Comprehensive Integrity Check 
>
> ```tar -tzf filename.tar.gz > /dev/null```
> 
> This decompresses the archive completely in your memory to verify that the file structure is flawless. [1, 3, 4, 6]  
> 
> * Fast Gzip-Only Check 
>
> ```gunzip -t filename.tar.gz```
>
> This only tests the integrity of the outer compression wrapper, skipping the deeper structure analysis. [7, 8, 9, 10, 11]  
> 
> * List Archive Contents 
>
> ```tar -tvf filename.tar.gz```
>
> This lists every stored file on your screen, which helps you manually confirm that all expected elements are present. [12, 13, 14, 15, 16]  
> 
> * Scripting and Automation 
>
> If you are writing an automated backup script, you can leverage the terminal's exit status ($?) to handle errors programmatically: [7, 17, 18]  
> ###### bash
> ```
> if tar -tzf archive.tar.gz > /dev/null 2>&1; then
>     echo "Success: The archive is valid and healthy."
> else
>     echo "Error: The archive is corrupted or incomplete."
> fi
> ```
>
> Windows Alternative 
> If you are on Windows, you can download and use 7-Zip to test the file. Right-click your  file, navigate to the 7-Zip submenu, and select Test archive to run a diagnostic scan. [19, 20, 21]  
> If you are encountering errors during execution, please share the exact error message or the operating system you are using so we can fix it. 
> 
> AI responses may include mistakes.
> 
> [1](https://serverfault.com/questions/293605/check-integrity-of-tar-gz-backup)
> [2](https://superuser.com/questions/216107/how-to-make-sure-a-tar-gz-file-is-valid-and-will-uncompress-correctly)
> [3](https://support.cpanel.net/hc/en-us/articles/1500000301382-How-to-test-the-integrity-of-TAR-and-ZIP-files)
> [4](https://stackoverflow.com/questions/41597207/verifying-a-tar-gz-is-not-corrupt)
> [5](https://stackoverflow.com/questions/52170315/is-it-possible-to-verify-if-tar-gz-file-is-corrupted)
> [6](https://recoverit.wondershare.com/what-is/gz-file-recovery.html)
> [7](https://stackoverflow.com/questions/2001709/how-to-check-if-a-unix-tar-gz-file-is-a-valid-file-without-uncompressing)
> [8](https://unix.stackexchange.com/questions/416303/how-to-check-validate-the-tar-gz-files-before-un-tar)
> [9](https://community.spiceworks.com/t/testing-integrity-of-a-tar-gz-file/909740)
> [10](https://superuser.com/questions/1068522/how-to-verify-whether-a-compressed-gz-is-corrupted-or-not)
> [11](https://www.reddit.com/r/bash/comments/1kqbdib/check_if_gzipped_file_is_valid_fast/)
> [12](https://askubuntu.com/questions/392885/how-can-i-view-the-contents-of-tar-gz-file-without-extracting-from-the-command-l)
> [13](https://www.cyberciti.biz/faq/list-the-contents-of-a-tar-or-targz-file/)
> [14](https://www.interserver.net/tips/kb/extract-tar-gz-files-using-linux-command-line/)
> [15](https://www.centron.de/en/tutorial/tar-command-in-linux-extract-files-unpack-archives/)
> [16](https://hostman.com/tutorials/how-to-extract-or-unzip-tar-gz-files-in-linux/)
> [17](https://unix.stackexchange.com/questions/129599/test-tar-file-integrity-in-bash)
> [18](https://transloadit.com/devtips/advanced-tar-techniques-for-efficient-file-archiving/)
> [19](https://stackoverflow.com/questions/67085151/how-can-i-check-if-tar-not-tar-gz-file-is-corrupt-or-not-in-ubuntu)
> [20](https://www.mathworks.com/matlabcentral/answers/818135-error-uncompressing-gz-files)
> [21](https://geekflare.com/dev/extract-unzip-tar-gz-files/)

