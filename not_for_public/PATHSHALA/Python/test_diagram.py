# test_diagram.py


import diagram_lib
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.aggregator import *
from diagrams.onprem.analytics import *
from diagrams.onprem.auth import *
from diagrams.onprem.cd import *
from diagrams.onprem.certificates import *
from diagrams.onprem.ci import *
from diagrams.onprem.client import *
from diagrams.onprem.compute import *
from diagrams.onprem.container import *
from diagrams.onprem.database import *
from diagrams.onprem.dns import *
from diagrams.onprem.etl import *
from diagrams.onprem.gitops import *
from diagrams.onprem.groupware import *
from diagrams.onprem.iac import *
from diagrams.onprem.identity import *
from diagrams.onprem.inmemory import *
from diagrams.onprem.logging import *
from diagrams.onprem.mlops import *
from diagrams.onprem.monitoring import *
from diagrams.onprem.network import *
from diagrams.onprem.proxmox import *
from diagrams.onprem.queue import *
from diagrams.onprem.search import *
from diagrams.onprem.security import *
from diagrams.onprem.storage import *
from diagrams.onprem.tracing import *
from diagrams.onprem.vcs import *

from diagrams.


# from diagrams.aws.compute import EC2
# from diagrams.aws.database import RDS
# from diagrams.aws.network import ELB
import os

os.chdir(os.path.dirname(os.path.join(__file__)))
''' 
It sets the path of the output diagram file to the same path as the current script file.
It sets/shifts the current working directory of the script.

'''

with Diagram("Web Service", show=False):
    ELB("lb") >> EC2("web") << RDS("userdb") >> EC2("web")

# print(RDS.nodeid)

# print(RDS._rand_id())



with Diagram("mobile", show=False):
    mobile1 = M1("my mobile")
    tablet1 = T1("My tablet")
    container1 = D1("conta__1")
    system1 =  EC2("Website") 
    win2 = Windows("Windows user")
    win1 =  Windows("Windows user")
    srvr1 = Server("Windows server")
    
    tablet1 >> system1 >> container1
    mobile1 >> system1 >> container1
    win1 >> system1 >> container1
    win2 >> system1 >> container1



