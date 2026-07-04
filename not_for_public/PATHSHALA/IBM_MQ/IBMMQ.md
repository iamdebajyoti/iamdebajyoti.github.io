## The IBM MQ quick reference for operational use
------
### runmqras command
> The **runmqras** command is an IBM MQ utility used to automatically collect troubleshooting and diagnostic information (known as MustGather data) into a single archive file for submission to IBM Support when reporting a problem.
> 
> ```runmqras -qmlist <<qmgr name>> -section defs,trace -caseno <<ibm case number, e.g. TS021456206>>```




### MQRC 2540
The IBM MQ reason code 2540 (Hex: 09EC) stands for MQRC_UNKNOWN_CHANNEL_NAME. It indicates that the channel name provided by the client application is not defined on the queue manager it is trying to connect to. [1, 2, 3] 
Common Causes

* Case Sensitivity: IBM MQ object names, including channel names, are case-sensitive. For example, MY.CHANNEL is not the same as my.channel.
* Incorrect Connection Details: You may be connecting to the wrong port or host, reaching a different queue manager where the intended channel does not exist.
* Missing Definition: The SVRCONN channel has not been created on the target queue manager.
* Encoding Issues: Setting the CCSID to 1200 in the client configuration can sometimes trigger this error due to conversion failures. [1, 3, 4, 5, 6, 7, 8, 9] 

Recommended Solutions

   1. Verify the Channel Name: Use the runmqsc command DISPLAY CHANNEL(your_channel_name) to confirm the exact spelling and case on the server.
   2. Check Port and Host: Ensure your application's CONNAME (Connection Name) points to the correct hostname and port (default is often 1414) for the specific queue manager.
   3. Inspect Error Logs: Check the queue manager's error logs (often found in /var/mqm/qmgrs/<QMGR_NAME>/errors/AMQERR01.LOG) for message AMQ9520, which provides more detail on why the channel was not recognized.
   4. Confirm Permissions: Ensure the user account attempting the connection has the appropriate authority to access the channel. [1, 2, 4, 6, 7, 8, 10, 11] 

[1] [https://stackoverflow.com](https://stackoverflow.com/questions/27304502/mqconn-error-2540-invalid-channel-name)
[2] [https://pitstop.manageengine.com](https://pitstop.manageengine.com/portal/en/kb/articles/why-am-i-getting-mqrc-unknown-channel-name-error-when-i-try-to-add-ibm-mq-monitor)
[3] [https://stackoverflow.com](https://stackoverflow.com/questions/54537571/queuemanager-is-not-connecting-given-exception-mqje001)
[4] [https://stackoverflow.com](https://stackoverflow.com/questions/31485831/channel-not-defined-remotely-issue-when-connecting-from-camel-to-a-websphere-m)
[5] [https://community.boomi.com](https://community.boomi.com/s/article/errorunabletoretrievejmsmessagecausedbycc2rc2540amq9520channelnotdefinedremotely)
[6] [https://mqseries.net](https://mqseries.net/phpBB2/viewtopic.php?t=76026)
[7] [https://mqseries.net](https://mqseries.net/phpBB2/viewtopic.php?t=76026)
[8] [https://www.ibm.com](https://www.ibm.com/docs/en/instana-observability/1.0.312?topic=mq-troubleshooting)
[9] [https://www.ibm.com](https://www.ibm.com/mysupport/s/defect/aCI0z0000004GCS/dt033234?language=en_US)
[10] [https://stackoverflow.com](https://stackoverflow.com/questions/31485831/channel-not-defined-remotely-issue-when-connecting-from-camel-to-a-websphere-m)
[11] [https://mqseries.net](https://mqseries.net/phpBB/viewtopic.php?t=77623&sid=cb21736f88401dddc32617bfd5785ff8)



https://share.google/aimode/l09mXnzjQ0bDUjUOB

### ibm mq add multiple CN to channel SSLPEER 
[solution from From Google AI](https://share.google/aimode/yw7sZyHnsnUx2Gbgs)


# QUICK TIPS
## MQ Command strings


### To list ONLY the queue manager names
```
dspmq | awk -F "(" '{ print $2 }' | awk -F ")" '{ print $1 }'
```

### LINUX - Failover / Fallback (PTH)
```
echo;  date +%F_%H-%M-%S-%A-%Z; echo; dspmq | grep -i -e NPT301 -e PGT301 -e EVT301
. /opt/mqmv9/v93037/bin/setmqenv -s -k
endmqm -s NPT301
endmqm -s PGT301
endmqm -s EVT301
sleep 60
echo;  date +%F_%H-%M-%S-%A-%Z; echo; echo "Failover Cluster 1"; echo; dspmq | grep -i -e NPT301 -e PGT301 -e EVT301
```
```
sleep 400
echo;  date +%F_%H-%M-%S-%A-%Z; echo; dspmq | grep -i -e NPT301 -e PGT301 -e EVT301
. /opt/mqmv9/v93037/bin/setmqenv -s -k
endmqm -s NPT301
endmqm -s PGT301
endmqm -s EVT301
sleep 60
echo;  date +%F_%H-%M-%S-%A-%Z; echo; echo "Failback Cluster 1"; echo; dspmq | grep -i -e NPT301 -e PGT301 -e EVT301
```
=========================================================================================================================================
```
echo;  date +%F_%H-%M-%S-%A-%Z; echo; dspmq | grep -i -e NPT302 -e PGT302 -e EVT302;
. /opt/mqmv9/v93037/bin/setmqenv -s -k;
endmqm -s NPT302;
endmqm -s PGT302;
endmqm -s EVT302;
sleep 60;
echo;  date +%F_%H-%M-%S-%A-%Z; echo; echo "Failover Cluster 2"; echo; dspmq | grep -i -e NPT302 -e PGT302 -e EVT302;
echo;
```
```
sleep 420;
echo;  date +%F_%H-%M-%S-%A-%Z; echo; dspmq | grep -i -e NPT302 -e PGT302 -e EVT302;
. /opt/mqmv9/v93037/bin/setmqenv -s -k;
endmqm -s NPT302;
endmqm -s PGT302;
endmqm -s EVT302;
sleep 60;
echo;  date +%F_%H-%M-%S-%A-%Z; echo; echo "Failback Cluster 2"; echo; dspmq | grep -i -e NPT302 -e PGT302 -e EVT302;
echo;
```

### Extract QMGR installation info
```
# for single queue manager
qmgr=""
source $(dspmq -m ${qmgr} -o installation | awk '{ print $3 }' | cut -d "(" -f 2 | cut -d ")" -f 1)/bin/setmqenv -s -k

# for multiple queue manager
declare -a qmgrs=() # place the name of the queue managers separated by space
source $(dspmq -m ${qmgr} -o installation | awk '{ print $3 }' | cut -d "(" -f 2 | cut -d ")" -f 1)/bin/setmqenv -s -k
```