# SDN_LB_Webserver_schedulling_method
Task Scenario: • Implement, demonstrate and test an adaptive web service that applies a overlay- and tunnel-based load balancer • Use for the implementation Docker, NGINX, and Python in the MS Azure cloud • Focus is on Docker, MS Azure, Overlay (data plane) and Adaptation (control plane)


DV2603/ET2599:
Software Defined Networking
Project Assignment: Implementation and Demonstration of Load
Balancer for HTTP Requests in MS Azure using Virtualization Techniques
LP 2 / Nov 2023 - Jan 2024 (version: Dec 1, 2023)
Kurt Tutschku, Roman-Valentyn Tkachuk
Blekinge Institute of Technology (BTH),
Faculty of Computing
Department of Computer Science and Engineering (DIDA)
Project Technical Learning Objectives:
• Consider “Forwarding” as a function
• Implement overlay routing
• Cloud-native view: chains of services
implemented in the Cloud
Task Scenario:
• Implement, demonstrate and test an adaptive web service that applies
a overlay- and tunnel-based load balancer
• Use for the implementation Docker, NGINX, and Python in the MS Azure
cloud
• Focus is on Docker, MS Azure, Overlay (data plane) and Adaptation
(control plane)

Required Functionality (I)
• Web service:
• Implement a web service that displays a webpage
upon request by the client
• The service is provided by two or more different web
servers (server 2, server 3, etc.) and the servers
should answer according to the selected load
balancing scheme, e.g. round-robin
• There is a proxy (server 1) on the ingress
• The load balancing and alternating between servers is
obtained by a dedicated element, the load balancer
Required Functionality (II)
• Web servers :
• Each web server provides a similar webpage but the
response indicates which server is used à enables the
identification of the answering server
• The web server will send spontaneously updates
about their load status to the load balancer à needs
to be shown in the demo
• An administrator can impose load on a web server
from the inside, see Lab 1 (lecture on SDN
performance).
• The load balancer implements different adaptation
strategies: RR/WRR à needs to be demonstrated
Required Functionality (III)
• Round-robin (RR) and weighted round-robin (WRR)
• Both are scheduling techniques
• Round-Robin (RR, https://en.wikipedia.org/wiki/Round-
robin_scheduling):
• cycles over the queues/tasks and gives each queue/task one
service opportunity per cycle
• Weighted Round Robin (WRR,
https://en.wikipedia.org/wiki/Weighted_round_robin):
• is a generalization of Round-robin scheduling
• offers to each queue/task a fixed number of opportunities, the
work weight, set at configuration.
• allow influencing the portion of capacity received by each
queue/task.
Required Functionality (IV)
• Load Balancer
• The load balancer receives all HTTPS requests from the
proxy and forwards them to the appropriate web server
according to the applied balancing scheme (tunnel)
• The load balancer eventually forms a “queue” for each
web server
• The balancer needs to able be configured with an
• arbitrary number of available webservers
• With one of the required balacing schemes (all schemes need to
be selected by configuration)
à Needs to be demonstrated
Required Functionality (VI)
• Load Balancer
• The balancing scheme should be able to operate at least in the
following modes:
• Round-robin, i.e. alternation between web servers according to a given
order
• Weighted round-robin, i.e. alternation according to a given weighted
order (see below)
• Random, i.e. equal probability of choosing one of the web servers
randomly
à Needs to be demonstrated
• Workload sensitivity
• The balancer maintains a “process” (controller) which can receive
workload updates from the servers
• An update of the balancing is triggered by the (controller) using the
received information
• The controller changes the forwarding in the data plane by the load
balancer
Required Functionality (VII)
• Use of Docker and MS Azure cloud
• All elements (clients, load balancer, web servers) must
be implemented as Docker containers in MS Azure of
the BTH cloud
• Use of Nginx
• NGINX is a web server framework that can also be used
as a reverse proxy, load balancer, mail proxy, and HTTP
cache.
• Usage of embedded NGINX load balancer is not
allowed (prohibited).
• The information available at: https://nginx.org/
• Use of Python as a programming language
(exceptions possible after checking with course
responsible)
Requirements for Passing the Project
• Demonstrate the working system in one of the demo sessions:
(clients, load balancer - controller, overlays/tunnel), web servers:
• a) switching of the load balancing scheme and
• b) showing the effects of load sensitivity
• Writing a 3-4-page report (DIN A4, 11pt):
• Describing the used technology, architecture, and the sensitivity
observations
• Outline and name the used virtualization concepts and techniques and
outlines the parallels to the SDN technology discussed in the lecture
• Include a graphic of the architecture and one or more screenshots of the
adaptive behaviour
• Typical scientific structure of the text: intro, methods/technologies,
description of implementation and experiments, results, summary
• Work in pairs or alone (pairs recommended); submission by
CANVAS; Overall evaluation of the project: pass/fail
Date Day Time Location Topic
2023-12-01 Fri 3pm15 Zoom Project 1a: Organization, Requirements, and Technology
2024-01-10 Tue 1pm00 J1630 Project 1b: Student’s Demonstration of projects and results (part 1)
2024-01-11 Thu 8pm15 J1630 Project 1c: Student’s Demonstration of projects and results (part 2)
2024-01-14 Sun 23pm59 CANVAS Deadline: upload report
Project Dates (as Dec. 1, 2023)
Tack så mycket!
Frågor?
