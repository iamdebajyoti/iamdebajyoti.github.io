import os
os.environ["PATH"] += os.pathsep + 'C:\\Dev\\Graphviz-14.1.1-win64\\bin'

# # diagram.py
# from diagrams import Diagram
# from diagrams.aws.compute import EC2
# from diagrams.aws.database import RDS
# from diagrams.aws.network import ELB
# from diagrams.generic.compute import *
# from diagrams.ibm.infrastructure import *
# from diagrams.ibm.applications import *


# with Diagram("Web Service", show=True, outformat="jpg"):
#     # ELB("lb") >> EC2("web") << ELB("lb") >> EC2("web") >> RDS("userdb") << EC2("web") >> ELB("lb")
#     lb1 = ELB("lb")
#     sys1 = EC2("web")
#     db1 = RDS("userdb")

#     lb1 >> sys1 >> lb1
#     sys1 >> db1


# with Diagram("MQ channels", show=True, outformat="jpg"):
    # EnterpriseApplications("AMH") >> Channels("SDR1") >> CloudMessaging("AMT201") >> Channels("RCVR1") >> EnterpriseApplications("NPP")

####################################################################################################
# BASIC
####################################################################################################

from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

with Diagram(name="Advanced Web Service with On-Premises (colored)", show=False):
    ingress = Nginx("ingress")

    metrics = Prometheus("metric")
    metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")

    with Cluster("Service Cluster"):
        grpcsvc = [
            Server("grpc1"),
            Server("grpc2"),
            Server("grpc3")]

    with Cluster("Sessions HA"):
        primary = Redis("session")
        primary \
            - Edge(color="brown", style="dashed") \
            - Redis("replica") \
            << Edge(label="collect") \
            << metrics
        grpcsvc >> Edge(color="brown") >> primary

    with Cluster("Database HA"):
        primary = PostgreSQL("users")
        primary \
            - Edge(color="brown", style="dotted") \
            - PostgreSQL("replica") \
            << Edge(label="collect") \
            << metrics
        grpcsvc >> Edge(color="black") >> primary

    aggregator = Fluentd("logging")
    aggregator \
        >> Edge(label="parse") \
        >> Kafka("stream") \
        >> Edge(color="black", style="bold") \
        >> Spark("analytics")

    ingress \
        >> Edge(color="darkgreen") \
        << grpcsvc \
        >> Edge(color="darkorange") \
        >> aggregator
    
####################################################################################################
# Less Edges
####################################################################################################

from diagrams import Cluster, Diagram, Node
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

with Diagram("\nAdvanced Web Service with On-Premise Less edges", show=False) as diag:
    ingress = Nginx("ingress")

    with Cluster("Service Cluster"):
        serv1 = Server("grpc1")
        serv2 = Server("grpc2")
        serv3 = Server("grpc3")

    with Cluster(""):
        blankHA = Node("", shape="plaintext", width="0", height="0")

        metrics = Prometheus("metric")
        metrics << Grafana("monitoring")

        aggregator = Fluentd("logging")
        blankHA >> aggregator >> Kafka("stream") >> Spark("analytics")

        with Cluster("Database HA"):
            db = PostgreSQL("users")
            db - PostgreSQL("replica") << metrics
            blankHA >> db

        with Cluster("Sessions HA"):
            sess = Redis("session")
            sess - Redis("replica") << metrics
            blankHA >> sess

    ingress >> serv2 >> blankHA

diag

####################################################################################################
# Merged Edges
####################################################################################################

from diagrams import Cluster, Diagram, Edge, Node
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

graph_attr = {
    "concentrate": "true",
    "splines": "spline",
}

edge_attr = {
    "minlen":"3",
}

with Diagram("\n\nAdvanced Web Service with On-Premise Merged edges", show=False,
            graph_attr=graph_attr,
            edge_attr=edge_attr) as diag:

    ingress = Nginx("ingress")

    metrics = Prometheus("metric")
    metrics << Edge(minlen="0") << Grafana("monitoring")

    with Cluster("Service Cluster"):
        grpsrv = [
            Server("grpc1"),
            Server("grpc2"),
            Server("grpc3")]

    blank = Node("", shape="plaintext", height="0.0", width="0.0")

    with Cluster("Sessions HA"):
        sess = Redis("session")
        sess - Redis("replica") << metrics

    with Cluster("Database HA"):
        db = PostgreSQL("users")
        db - PostgreSQL("replica") << metrics

    aggregator = Fluentd("logging")
    aggregator >> Kafka("stream") >> Spark("analytics")

    ingress >> [grpsrv[0], grpsrv[1], grpsrv[2],]
    [grpsrv[0], grpsrv[1], grpsrv[2],] - Edge(headport="w", minlen="1") - blank
    blank >> Edge(headport="w", minlen="2") >> [sess, db, aggregator]

diag