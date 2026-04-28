
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