###### 0.0.0.0.1. Top
Table to Contents
- [1. \[NIX\] File and Folder Management](#1-nix-file-and-folder-management)
  - [1.1. "ls" command output 4-digit year](#11-ls-command-output-4-digit-year)
  - [1.2. \[RHEL\] TAR GZIP ZIPPING XTRACTING](#12-rhel-tar-gzip-zipping-xtracting)
- [2. SHELL Scripting](#2-shell-scripting)
  - [2.1. Array in Shell](#21-array-in-shell)
    - [2.1.1. Array Declaration, Population, Manipulation, Reference,](#211-array-declaration-population-manipulation-reference)
- [3. AWK Programming](#3-awk-programming)
  - [3.1. awk matching](#31-awk-matching)
- [4. MAN Pages](#4-man-pages)
  - [4.1. man](#41-man)
  - [4.2. export man pages as html](#42-export-man-pages-as-html)
- [5. OS Internals](#5-os-internals)
  - [5.1. \[AIX\] check RAM, CPU - basic details](#51-aix-check-ram-cpu---basic-details)
    - [5.1.1. For all CPU details and RAM](#511-for-all-cpu-details-and-ram)
  - [5.2. \[RHEL\] check CPU performance](#52-rhel-check-cpu-performance)
  - [5.3. \[RHEL\] To check if a server is physical or virtual](#53-rhel-to-check-if-a-server-is-physical-or-virtual)
  - [5.4. \[AIX\] OS version and patch details](#54-aix-os-version-and-patch-details)
- [6. Operating System and Fix Pack Levels](#6-operating-system-and-fix-pack-levels)
- [7. History of Installed Filesets and Updates](#7-history-of-installed-filesets-and-updates)
- [8. Interim Fixes (iFixes / eFixes)](#8-interim-fixes-ifixes--efixes)
- [9. Commands to Check Patch History](#9-commands-to-check-patch-history)
- [10. Log Files to Review](#10-log-files-to-review)
- [11. Operating System Patch Commands](#11-operating-system-patch-commands)
  - [11.1. Setting the Shell Prompt](#111-setting-the-shell-prompt)
- [12. Microsoft Defender](#12-microsoft-defender)
  - [12.1. \[RHEL\] Microsoft Defender Exclusion](#121-rhel-microsoft-defender-exclusion)
- [13. Networking](#13-networking)
  - [13.1. Network analysis and investigation](#131-network-analysis-and-investigation)
- [14. Calculating DISK Usage](#14-calculating-disk-usage)
  - [14.1. \[AIX\]](#141-aix)
      - [14.1.0.1. Option 1: The Native AIX Command (Recommended)](#14101-option-1-the-native-aix-command-recommended)
      - [14.1.0.2. Option 2: Human-Readable Format (AIX 7.1+)](#14102-option-2-human-readable-format-aix-71)
      - [14.1.0.3. Option 3: Emulating -maxdepth 1 with find and du](#14103-option-3-emulating--maxdepth-1-with-find-and-du)
  - [14.2. Finding lines before and after \[AIX\]](#142-finding-lines-before-and-after-aix)
- [15. Annexure](#15-annexure)
        - [15.0.0.0.1. Documentation Style](#150001-documentation-style)
        - [15.0.0.0.2. Pending](#150002-pending)
- [1. Check for Overriding Files](#1-check-for-overriding-files)
- [2. Login Shell vs. Non-Login Shell](#2-login-shell-vs-non-login-shell)
- [3. Verify Syntax and Execution Errors](#3-verify-syntax-and-execution-errors)
- [4. Check File Permissions](#4-check-file-permissions)
- [1. Check for Overriding Files](#1-check-for-overriding-files-1)
- [2. Login Shell vs. Non-Login Shell](#2-login-shell-vs-non-login-shell-1)
- [3. Verify Syntax and Execution Errors](#3-verify-syntax-and-execution-errors-1)
- [4. Check File Permissions](#4-check-file-permissions-1)
- [Step 1: Run this diagnostic command](#step-1-run-this-diagnostic-command)
- [Step 2: What the results mean](#step-2-what-the-results-mean)

[Back to Top](#top)

## 1. [NIX] File and Folder Management

### 1.1. "ls" command output 4-digit year
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
> ###### By default, ls -l shows Month Day Time for files within the last six months, and Month Day Year for older files.
> ###### The --time-style options work on GNU ls, but often fail on FreeBSD, Solaris, or older AIX implementations.
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
[Back to Top](#top)

### 1.2. [RHEL] TAR GZIP ZIPPING XTRACTING

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

[Back to Top](#top)

## 2. SHELL Scripting
### 2.1. Array in Shell
#### 2.1.1. Array Declaration, Population, Manipulation, Reference, 


## 3. AWK Programming

### 3.1. awk matching
> #### awk + match + regex
> 
> [Google AI Mode](https://share.google/aimode/0JGrgzYEPAhjoSMmq)

[Back to Top](#top)

## 4. MAN Pages

### 4.1. man
### 4.2. export man pages as html
```
man <command_name> | awk 'BEGIN {print "<html><body><pre>"} {gsub(/&/, "&amp;"); gsub(/</, "&lt;"); gsub(/>/, "&gt;"); print} END {print "</pre></body></html>"}' > <command_name>.html
```
[Back to Top](#top)

## 5. OS Internals
### 5.1. [AIX] check RAM, CPU - basic details
```
date; hostname; echo; echo; prtconf -m; echo; echo; svmon -G -O unit=GB; echo; echo; lsattr -El mem0; echo; echo;
```
#### 5.1.1. For all CPU details and RAM
```
prtconf -ckLmsv
```
### 5.2. [RHEL] check CPU performance

~~~shell
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
~~~

[Back to Top](#top)

### 5.3. [RHEL] To check if a server is physical or virtual
> Run as root
```
dmidecode -t system
```

### 5.4. [AIX] OS version and patch details
~~~shell
oslevel -s
uname -a
~~~
To list the latest installed updates, service packs, or temporary patches on AIX, use the oslevel, lslpp, or emgr commands. [1, 2, 3] 
## 6. Operating System and Fix Pack Levels

* oslevel -s: Displays the current Technology Level (TL), Service Pack (SP), and build date of your AIX operating system (e.g., 7300-01-01-2246).
* oslevel -q: Lists all known maintenance levels installed on the system. [1, 4] 

## 7. History of Installed Filesets and Updates

* lslpp -h: Lists the complete installation history for all software filesets and updates, showing timestamps for when individual components were applied.
* lslpp -L: Displays only the latest version of currently installed filesets. [1, 2] 

## 8. Interim Fixes (iFixes / eFixes)

* emgr -l: Lists all active, temporary, or interim security patches currently applied to the AIX kernel and filesets. [3] 

If you are trying to check for new available patches online rather than installed ones, let me know your exact AIX version and whether you have access to IBM Fix Central or emgr_check_ifixes. [5, 6] 

[1] [https://community.spiceworks.com](https://community.spiceworks.com/t/is-there-a-way-to-check-the-history-of-updates-done-to-the-aix-server/908021)
[2] [https://emmanuel.iffly.free.fr](http://emmanuel.iffly.free.fr/doku.php?id=aix:aix_package)
[3] [https://aix4admins.blogspot.com](https://aix4admins.blogspot.com/2012/06/ifix-interim-fix-or-ifix-previously.html)
[4] [https://www.ibm.com](https://www.ibm.com/support/pages/fix-pack-information-lslpp-list-rpm-packages-using-rpm-4913-3aix61p)
[5] [https://www.ibm.com](https://www.ibm.com/docs/en/aix/7.2.0?topic=notes-aix-720-release)
[6] [https://techchannel.com](https://techchannel.com/systems-management/using-emgr-check-ifixes-aix-7-3/)


---
You can find the installation date and update history for patches on AIX by using the lslpp -h command, checking the installation logs in /var/adm/ras/, or reviewing the core operating system fileset history. Most users on the [Spiceworks Community](https://community.spiceworks.com/t/is-there-a-way-to-check-the-history-of-updates-done-to-the-aix-server/908021) agree that tracking update history via lslpp is the standard approach. [1, 2, 3, 4] 
## 9. Commands to Check Patch History

* Run lslpp -h bos.rte to display the complete installation and update timestamps for the base operating system fileset.
* Run lslpp -ah <fileset_name> or lslpp -hc to get a detailed history of specific packages or a colon-separated list of all applied updates.
* Run oslevel -s to verify your current Technology Level (TL) and Service Pack (SP) combination. [1, 2, 4] 

## 10. Log Files to Review

* Check the modification time or contents of /var/adm/ras/bosinstlog to see when the system or base image was last loaded or upgraded.
* Check timestamps on core system files or logs inside /var/adm/ras/ for recent maintenance activity. [3] 

If you have a specific fileset or log file you are trying to parse, let me know and I can help you write a more targeted command to pull the exact date.

[1] [https://community.unix.com](https://community.unix.com/t/date-patch-was-installed/186305)
[2] [https://sites.google.com](https://sites.google.com/site/uyestebandiaz/tips-aix/how-to/displays-the-installation-aix-date)
[3] [https://community.ibm.com](https://community.ibm.com/community/user/discussion/aix-install-date)
[4] [https://community.spiceworks.com](https://community.spiceworks.com/t/is-there-a-way-to-check-the-history-of-updates-done-to-the-aix-server/908021)

---
To find the AIX patch level, run oslevel -s, oslevel -r, or instfix -i | grep AIX_ML at the command line. [1, 2, 3] 
## 11. Operating System Patch Commands

* oslevel -s: Shows the full technology level, service pack, and build date (for example: 7100-05-03-1838).
* oslevel -r: Shows the base technology level maintenance package.
* instfix -i | grep AIX_ML: Lists all applied maintenance level fix packages on the system. [2, 3, 4, 5] 

· 1970 M01 1
If you'd like, I can help you:

* Decode the specific Technology Level (TL) and Service Pack (SP) values from your command output.
* Look up recommended updates for your version of AIX.


[1] [https://community.spiceworks.com](https://community.spiceworks.com/t/checking-patch-level-on-aix/903150)
[2] [https://serverfault.com](https://serverfault.com/questions/100875/how-do-i-tell-which-aix-version-am-i-running)
[3] [https://somireddy.wordpress.com](https://somireddy.wordpress.com/2013/07/17/aix-howto-determine-installed-technology-level/)
[4] [https://stackoverflow.com](https://stackoverflow.com/questions/52496505/how-to-check-if-an-aix-system-is-up-to-date-updates-security-fixes)
[5] [https://support.microfocus.com](https://support.microfocus.com/kb/doc.php?id=7754654)




[Back to Top](#top) 


### 11.1. Setting the Shell Prompt
> This shows only the working/current folder

```bash
export PS1="[ $(whoami) @ $(hostname):\$(basename "$(pwd)") ] "
# or
export PS1="\u@\h:\W\$ "
```

> This shows the whole path to the current folder
```shell
export PS1="[ $(whoami) @ $(hostname):\$(pwd) ] "
```

> Limit the number of directories shown
```shell
export PROMPT_DIRTRIM=<some number>
# eg. 
export PROMPT_DIRTRIM=3 # to restrict to last 3 directories
```

> Trim to just the parent and current folder
```
export PS1="\u@\h:\W\$ "
export PROMPT_DIRTRIM=2
```
> **Check your PS1 variable**
> ```echo $PS1```
> The PROMPT_DIRTRIM feature only works if your prompt configuration (PS1) utilizes the \w escape sequence (which stands for full path). It will not work if your prompt explicitly references the $PWD variable. If you see \w: - the trim feature is supported. Make sure you aren't currently inside a short directory tree (e.g., if you set PROMPT_DIRTRIM=2, you must go at least 3 directories deep to see it truncate). 
> If you see $PWD or $(pwd): - the trim feature is overridden. Reset your prompt to use \w instead: ```PS1='\u@\h:\w\$ '```
>
> **Verify your Bash version**
> The PROMPT_DIRTRIM variable requires Bash 4.0 or higher. Check your shell version: ```bash --version```
>
> **Overrides in PROMPT_COMMAND**
> Check if you have a PROMPT_COMMAND active. This environment variable runs a command right before rendering your prompt and frequently overwrites standard PS1 configurations. ```echo $PROMPT_COMMAND```

---
[Back to Top](#top)

## 12. Microsoft Defender

### 12.1. [RHEL] Microsoft Defender Exclusion
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

[Back to Top](#top)

## 13. Networking

### 13.1. Network analysis and investigation
```
netstat -tunlp | more
netstat -nr
ip route get << ip address>>
ping <<hostname>>
nslookup <<fqdn>>
```
*fqdn = fully qualified domain name*

[Back to Top](#top)

## 14. Calculating DISK Usage
### 14.1. [AIX]
To find disk usage with a maximum depth of 1 on AIX, use the standard command du -s * because the native AIX du binary does not support the Linux-style --max-depth=1 or -d 1 flags.
##### 14.1.0.1. Option 1: The Native AIX Command (Recommended)
This summarizes the size of each top-level file and directory in your current path without recursing deeper into the screen output:
~~~bash
du -s *
~~~
> How it works: The shell expands the asterisk * to all immediate files and subdirectories. The -s flag forces du to provide only a summary (total size) for each of those individual arguments.To include hidden files: Run du -s .[^.]* * instead.
##### 14.1.0.2. Option 2: Human-Readable Format (AIX 7.1+)
If you are running a modern version of AIX, the du command supports the -g (Gigabytes), -m (Megabytes), and -k (Kilobytes) flags to make the output easier to interpret:
~~~bash
du -sm *
~~~
##### 14.1.0.3. Option 3: Emulating -maxdepth 1 with find and du
If you need a strict equivalent that calculates the exact block sizes specifically for the top tier without utilizing shell globbing expansion, you can use find to prune deeper paths:
~~~bash
find . -maxdepth 1 -exec du -s {} \;
~~~

[Back to Top](#top)


### 14.2. Finding lines before and after [AIX]
awk -v B=1 -v A=1 '/has insufficient authority to access object/ {for (i=NR-B; i<NR; i++) if (i in lines) print lines[i]; print; c=A; next} c && c-- {print} {lines[NR]=$0; delete lines[NR-B-1]}' /MQTST/data/MQD76/errors/AMQERR01.LOG





>
## 15. Annexure
#############################################################################
###### 15.0.0.0.1. Documentation Style
> * For main topic use H2 and Camel case
> * For sub topic/s use H3/H4 and Camel case
> * For variations under sub-topics use H5 and Sentence case
> * For less important notes under a sub-topic use H6
> * Mention [NIX] and/or [RHEL] and/or [AIX] and/or [Debian] to indicate the OS flavour
###############################################################################




[Back to Top](#top)



###### 15.0.0.0.2. Pending

https://stackoverflow.com/questions/60021897/passing-a-parameter-to-a-bash-alias



Your ~/.profile file is likely not triggering because Bash skips it entirely if ~/.bash_profile or ~/.bash_login exists in your home directory, or because you are opening a standard terminal window which initializes as a non-login shell. Bash only evaluates the first initialization file it finds in a specific order during a login session. [1, 2, 3] 
## 1. Check for Overriding Files
Bash looks for login configuration files in your home directory in this strict order: [4] 

   1. ~/.bash_profile
   2. ~/.bash_login
   3. ~/.profile

If Bash finds ~/.bash_profile, it stops searching and ignores ~/.profile completely. [2, 3, 5, 6] 

* Run ls -a ~ in your terminal to see if .bash_profile exists.
* Fix: If it exists, open ~/.bash_profile and add this code at the bottom to force it to load your .profile:

if [ -f "$HOME/.profile" ]; then
    . "$HOME/.profile"fi

[1, 3, 7, 8] 

## 2. Login Shell vs. Non-Login Shell
When you boot your Linux PC and open a GUI terminal window (like GNOME Terminal or Konsole), it usually starts a non-login shell. Non-login shells completely bypass .profile and look directly for ~/.bashrc instead. [1, 9, 10, 11, 12] 

* Fix: Move environment variables, aliases, or commands meant for your terminal sessions out of ~/.profile and place them at the bottom of ~/.bashrc.
* Alternative Fix: Force your terminal application to run as a login shell. Open your terminal preferences (e.g., Preferences > Profiles > Command) and check the box for "Run command as a login shell". [10, 13, 14, 15, 16] 

## 3. Verify Syntax and Execution Errors
A silent syntax error early in the .profile script will cause the shell to abort execution before it reaches your custom commands.

* Test the file manually for errors by running: . ~/.profile or source ~/.profile
* Look closely for missing quotes, syntax typos, or broken paths that print errors to the console. [2, 17] 

## 4. Check File Permissions
If the file system permissions prevent your user account from reading the file, it cannot execute.

* Run ls -l ~/.profile to check access permissions.
* Fix permissions by running: chmod 644 ~/.profile [18] 

To help fix this quickly, could you tell me which Linux distribution you are using, and what specific commands you are trying to trigger?

[1] [https://superuser.com](https://superuser.com/questions/176404/bash-not-loading-profile-in-new-session-on-linux)
[2] [https://unix.stackexchange.com](https://unix.stackexchange.com/questions/29791/bash-profile-not-sourced-when-running-su)
[3] [https://www.facebook.com](https://www.facebook.com/groups/GNUAndLinux/posts/10166702535320019/)
[4] [https://www.baeldung.com](https://www.baeldung.com/linux/check-umask-all-users)
[5] [https://www.howtogeek.com](https://www.howtogeek.com/830549/whats-the-difference-between-bashrc-and-profile-on-linux/)
[6] [https://askubuntu.com](https://askubuntu.com/questions/1365828/alias-settings-nor-working-at-logon)
[7] [https://medium.com](https://medium.com/@mattphoolishis/show-your-git-branch-in-your-command-line-prompt-using-bash-profile-a9678aec6057)
[8] [https://askubuntu.com](https://askubuntu.com/questions/510709/i-cannot-find-bash-profile-in-ubuntu)
[9] [https://askubuntu.com](https://askubuntu.com/questions/40287/why-is-etc-profile-not-being-loaded-during-non-login-bash-shell-sessions)
[10] [https://forums.linuxmint.com](https://forums.linuxmint.com/viewtopic.php?t=416470)
[11] [https://www.redswitches.com](https://www.redswitches.com/blog/bashrc-vs-bash_profile-in-linux/)
[12] [https://quizlet.com](https://quizlet.com/282094264/linux-11-the-shell-flash-cards/)
[13] [https://askubuntu.com](https://askubuntu.com/questions/210044/what-can-cause-my-profile-file-to-not-be-loaded-when-a-new-terminal-shell-is-in)
[14] [https://askubuntu.com](https://askubuntu.com/questions/566399/why-isnt-profile-sourced-when-opening-a-terminal)
[15] [https://askubuntu.com](https://askubuntu.com/questions/438150/why-are-scripts-in-etc-profile-d-being-ignored-system-wide-bash-aliases)
[16] [https://askubuntu.com](https://askubuntu.com/questions/1531772/why-are-profile-bash-profile-and-etc-profile-executed-during-graphical-l)
[17] [https://askubuntu.com](https://askubuntu.com/questions/161249/bashrc-not-executed-when-opening-new-terminal)
[18] [https://www.instagram.com](https://www.instagram.com/reel/DWEilkME7JS/)

Your ~/.profile file is likely not triggering because Bash skips it entirely if ~/.bash_profile or ~/.bash_login exists in your home directory, or because you are opening a standard terminal window which initializes as a non-login shell. Bash only evaluates the first initialization file it finds in a specific order during a login session. [1, 2, 3] 
## 1. Check for Overriding Files
Bash looks for login configuration files in your home directory in this strict order: [4] 

   1. ~/.bash_profile
   2. ~/.bash_login
   3. ~/.profile

If Bash finds ~/.bash_profile, it stops searching and ignores ~/.profile completely. [2, 3, 5, 6] 

* Run ls -a ~ in your terminal to see if .bash_profile exists.
* Fix: If it exists, open ~/.bash_profile and add this code at the bottom to force it to load your .profile:

if [ -f "$HOME/.profile" ]; then
    . "$HOME/.profile"fi

[1, 3, 7, 8] 

## 2. Login Shell vs. Non-Login Shell
When you boot your Linux PC and open a GUI terminal window (like GNOME Terminal or Konsole), it usually starts a non-login shell. Non-login shells completely bypass .profile and look directly for ~/.bashrc instead. [1, 9, 10, 11, 12] 

* Fix: Move environment variables, aliases, or commands meant for your terminal sessions out of ~/.profile and place them at the bottom of ~/.bashrc.
* Alternative Fix: Force your terminal application to run as a login shell. Open your terminal preferences (e.g., Preferences > Profiles > Command) and check the box for "Run command as a login shell". [10, 13, 14, 15, 16] 

## 3. Verify Syntax and Execution Errors
A silent syntax error early in the .profile script will cause the shell to abort execution before it reaches your custom commands.

* Test the file manually for errors by running: . ~/.profile or source ~/.profile
* Look closely for missing quotes, syntax typos, or broken paths that print errors to the console. [2, 17] 

## 4. Check File Permissions
If the file system permissions prevent your user account from reading the file, it cannot execute.

* Run ls -l ~/.profile to check access permissions.
* Fix permissions by running: chmod 644 ~/.profile [18] 

To help fix this quickly, could you tell me which Linux distribution you are using, and what specific commands you are trying to trigger?

[1] [https://superuser.com](https://superuser.com/questions/176404/bash-not-loading-profile-in-new-session-on-linux)
[2] [https://unix.stackexchange.com](https://unix.stackexchange.com/questions/29791/bash-profile-not-sourced-when-running-su)
[3] [https://www.facebook.com](https://www.facebook.com/groups/GNUAndLinux/posts/10166702535320019/)
[4] [https://www.baeldung.com](https://www.baeldung.com/linux/check-umask-all-users)
[5] [https://www.howtogeek.com](https://www.howtogeek.com/830549/whats-the-difference-between-bashrc-and-profile-on-linux/)
[6] [https://askubuntu.com](https://askubuntu.com/questions/1365828/alias-settings-nor-working-at-logon)
[7] [https://medium.com](https://medium.com/@mattphoolishis/show-your-git-branch-in-your-command-line-prompt-using-bash-profile-a9678aec6057)
[8] [https://askubuntu.com](https://askubuntu.com/questions/510709/i-cannot-find-bash-profile-in-ubuntu)
[9] [https://askubuntu.com](https://askubuntu.com/questions/40287/why-is-etc-profile-not-being-loaded-during-non-login-bash-shell-sessions)
[10] [https://forums.linuxmint.com](https://forums.linuxmint.com/viewtopic.php?t=416470)
[11] [https://www.redswitches.com](https://www.redswitches.com/blog/bashrc-vs-bash_profile-in-linux/)
[12] [https://quizlet.com](https://quizlet.com/282094264/linux-11-the-shell-flash-cards/)
[13] [https://askubuntu.com](https://askubuntu.com/questions/210044/what-can-cause-my-profile-file-to-not-be-loaded-when-a-new-terminal-shell-is-in)
[14] [https://askubuntu.com](https://askubuntu.com/questions/566399/why-isnt-profile-sourced-when-opening-a-terminal)
[15] [https://askubuntu.com](https://askubuntu.com/questions/438150/why-are-scripts-in-etc-profile-d-being-ignored-system-wide-bash-aliases)
[16] [https://askubuntu.com](https://askubuntu.com/questions/1531772/why-are-profile-bash-profile-and-etc-profile-executed-during-graphical-l)
[17] [https://askubuntu.com](https://askubuntu.com/questions/161249/bashrc-not-executed-when-opening-new-terminal)
[18] [https://www.instagram.com](https://www.instagram.com/reel/DWEilkME7JS/)

It looks like you need some extra help getting those commands to run!
To figure out exactly why your .profile isn't working, let's run a quick diagnostic test.
## Step 1: Run this diagnostic command
Copy and paste this exact command into your terminal and press Enter:

ls -a ~ | grep -E 'bash_profile|bash_login|profile'

## Step 2: What the results mean

* If you see .bash_profile or .bash_login in the output, your system is actively ignoring .profile.
* If you only see .profile, your terminal app is likely opening as a "non-login" shell and needs to use .bashrc instead.

If you are unsure how to read the output, just paste the results here or let me know:

* What Linux distribution or OS are you running? (e.g., Ubuntu, Fedora, macOS)
* What exact command or alias are you trying to automate?

I can give you the exact copy-paste fix once we narrow it down!

