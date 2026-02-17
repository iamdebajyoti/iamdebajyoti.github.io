import os
os.environ["PATH"] += os.pathsep + 'C:\\Dev\\Graphviz-14.1.1-win64\\bin'

####################################################################################################
# Basic
####################################################################################################

from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram("Simple Diagram"):
    EC2("web")

####################################################################################################
# Jupyter Notebooks
####################################################################################################

from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram("Simple Diagram") as diag:
    EC2("web")
diag


####################################################################################################
# Options
####################################################################################################

from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram("Simple Diagram", outformat="jpg"):
    EC2("web")

from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram("Simple Diagram Multi Output", outformat=["jpg", "png", "dot"]):
    EC2("web")

from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram("Simple Diagram", filename="my_diagram"):
    EC2("web")

from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram("Simple Diagram", show=False):
    EC2("web")

from diagrams import Diagram
from diagrams.aws.compute import EC2

graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

with Diagram("Simple Diagram", show=False, graph_attr=graph_attr):
    EC2("web")



####################################################################################################
# Custom
####################################################################################################
# Custom with local icons
####################################################################################################

.
├── custom_local.py
├── my_resources
│   ├── cc_heart.black.png
│   ├── cc_attribution.png
│   ├──...

from diagrams import Diagram, Cluster
from diagrams.custom import Custom


with Diagram("Custom with local icons\n Can be downloaded here: \nhttps://creativecommons.org/about/downloads/", show=False, filename="custom_local", direction="LR"):
  cc_heart = Custom("Creative Commons", "./my_resources/cc_heart.black.png")
  cc_attribution = Custom("Credit must be given to the creator", "./my_resources/cc_attribution.png")

  cc_sa = Custom("Adaptations must be shared\n under the same terms", "./my_resources/cc_sa.png")
  cc_nd = Custom("No derivatives or adaptations\n of the work are permitted", "./my_resources/cc_nd.png")
  cc_zero = Custom("Public Domain Dedication", "./my_resources/cc_zero.png")

  with Cluster("Non Commercial"):
    non_commercial = [Custom("Y", "./my_resources/cc_nc-jp.png") - Custom("E", "./my_resources/cc_nc-eu.png") - Custom("S", "./my_resources/cc_nc.png")]

  cc_heart >> cc_attribution
  cc_heart >> non_commercial
  cc_heart >> cc_sa
  cc_heart >> cc_nd
  cc_heart >> cc_zero


####################################################################################################
# Custom with remote icons
####################################################################################################

from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from urllib.request import urlretrieve

with Diagram("Custom with remote icons", show=False, filename="custom_remote", direction="LR"):

  # download the icon image file
  diagrams_url = "https://github.com/mingrammer/diagrams/raw/master/assets/img/diagrams.png"
  diagrams_icon = "diagrams.png"
  urlretrieve(diagrams_url, diagrams_icon)

  diagrams = Custom("Diagrams", diagrams_icon)

  with Cluster("Some Providers"):

    openstack_url = "https://github.com/mingrammer/diagrams/raw/master/resources/openstack/openstack.png"
    openstack_icon = "openstack.png"
    urlretrieve(openstack_url, openstack_icon)

    openstack = Custom("OpenStack", openstack_icon)

    elastic_url = "https://github.com/mingrammer/diagrams/raw/master/resources/elastic/saas/elastic.png"
    elastic_icon = "elastic.png"
    urlretrieve(elastic_url, elastic_icon)

    elastic = Custom("Elastic", elastic_icon)

  diagrams >> openstack
  diagrams >> elastic

  