# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
import os

os.chdir(os.path.dirname(os.path.join(__file__)))
''' 
It sets the path of the output diagram file to the same path as the current script file.
It sets/shifts the current working directory of the script.

'''

with Diagram("Web Service", show=False):
    ELB("lb") >> EC2("web") << RDS("userdb") >> EC2("web")

print(RDS.nodeid)

print(RDS._rand_id())