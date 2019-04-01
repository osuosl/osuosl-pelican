Hosting Details
===============
:slug: services/hosting/details
:title: Hosting Details
:menu: Hosting, Hosting Details, 2

We offer a wide variety of services to our hosted clients so the OSL can help
offload work from your machine and/or infrastructure team. This list is not
exhaustive, but is intended to give a better idea of the types of services we
provide.


Managed vs. Unmanaged
---------------------

Most of our hosting falls into two categories, managed or unmanaged.

Managed
^^^^^^^

For managed hosting, we will take care of your system(s) using our configuration management which ensures your systems
are always up to date, stable with tested configurations, and automated. We currently use `Chef`_ to manage all of our
systems and can create a project-specific cookbook if you want to assist in managing the system. We'll also configure
and maintain all of the services running on your system(s) including monitoring them and backing up any data.

Managed systems are ideal for smaller projects that have simple requirements and don't want to deal with day-to-day
system administration tasks.

.. _Chef: https://www.chef.io/

Unmanaged
^^^^^^^^^

Unmanaged hosting means you control everything about your system(s). We only require that you keep one sudo-enabled
account on the system for us to use as needed for troubleshooting. We will not actively manage, monitor or back
up these systems unless requested. If you run into an issue with your unmanaged system(s), we're still available to
help of course!

Virtualization
--------------

.. image:: /images/student-sysadmin.jpg
    :scale: 100%
    :align: right
    :alt: Hosting Detail - Sysadmin

We currently have two virtualization clusters available for use: `Ganeti`_ and `OpenStack`_. Depending on the project's
use case, we host their VM(s) on either or both platforms. Both clusters are powered with the `KVM hypervisor`_.

OpenStack
^^^^^^^^^

OpenStack offers a full API and web interface which allows projects to manage their VM resources as they see fit. Our
OpenStack cluster currently offers the following services:

- Compute (nova)
- Cinder (cinder)
- Image (glance)
- Network (neutron)
- Orchestration (heat)

We plan to add more OpenStack services as needed by projects. Our cluster is currently running the Ocata release with
eight compute nodes. Storage is powered via a six-node Ceph cluster. If you need to dynamically create/destroy/manage
your services, our OpenStack cluster is the way to go.

.. _OpenStack: http://openstack.org

Ganeti
^^^^^^

We have used Ganeti for ten years and it continues to be the stable solution for long-running VMs that need minimal
changes. We have a cluster with eight nodes for small projects and offer VMs at a variety of sizes and platforms, all
with full redundant storage using DRBD. Ganeti is very simple to use and maintain; however, it doesn't provide a public
API to deploy and manage the VMs. We do have a simple web management interface which allows projects to access the
console and power the VM on and off as needed.

.. _Ganeti: http://www.ganeti.org/
.. _KVM hypervisor: http://www.linux-kvm.org/page/Main_Page

CI/CD Hardware Resources
------------------------

.. image:: /images/facebook-servers.jpg
    :scale: 100%
    :align: right
    :alt: Hosting Detail - CI/CD Hardware Resources

We understand that FOSS projects have growing demands for doing continuous integration and even continuous delivery
(CI/CD).  While there are free resources available to most FOSS projects using such services as Travis-CI or CircleCI,
most of those free resources have limits which many projects run into. Here at the OSL, we can help with those needs in
two ways:

- Access to virtual machine resources via our OpenStack cluster(s)
- Access to bare metal resources via OpenCompute hardware

Thanks to a hardware donation from Facebook in 2015, we have three `OpenCompute Project`_ (OCP) racks which contain a
total of 90 OpenRack V2 "`Winterfell`_" servers. These servers have 144 GB of RAM, 2 x Intel(R) Xeon(R) CPU E5-2660 0 @
2.20GHz and one 3TB 5400 RPM SATA disk. These servers are hosted in a smaller secondary data center near our offices
and have some limitations on cooling and publicly addressable IP addresses. Due to this limitation, these servers are
behind an IPv4 NAT network and require port forwarding to access the systems. We can open additional ports as needed
but these machines are best suited for running tests and building software.

These resources provide can be used in any way that is needed, whether it's integrating with `Jenkins`_, `Buildbot`_,
`Gitlab CE`_, or any other CI/CD system you use.

.. _OpenCompute Project: https://www.opencompute.org/
.. _Winterfell: https://www.opencompute.org/wiki/Server/SpecsAndDesigns-old#Open_Rack_compatible_server_design
.. _Jenkins: https://jenkins.io/
.. _Buildbot: https://buildbot.net/
.. _Gitlab CE: https://gitlab.com/gitlab-org/gitlab-ce/

FTP Mirroring
-------------

We have a cluster of three servers behind the `ftp.osuosl.org`_ name with a total bandwidth capacity of more than 50
gigabits per second. These servers are hosted geographically across the United States. Instead of pushing files and
releases out from your own server, let us take care of the dirty work for you. We currently host approximately 100
projects on our mirroring servers using around 11TB of disk space. We do our best to host as many projects as we can,
however space is limited.

.. _ftp.osuosl.org: http://ftp.osuosl.org/

E-Mail
------

Mail Relaying
^^^^^^^^^^^^^^

We have a number of local mail relays that OSL-hosted servers can use to help relieve some of the pressure that mail
can put on your servers. These relays do spam and virus tagging.

Mailing Lists
^^^^^^^^^^^^^

We use `Mailman`_ for any mailing list needs. We can help you migrate old lists or create new lists that are centrally
managed on our system.

.. _Mailman: http://www.list.org/

Website Hosting
---------------

We offer website hosting for projects that require dynamic backend server support. We currently support hosting sites
which require languages such as PHP, Python, and Ruby. We don't support every web application but we'll do our best to
try and support a widely used platform. If you have a website that needs a home, let us know and we'll see how we can
help.

Database Hosting
----------------

We offer high performance hosted `MySQL`_ or `PostgreSQL`_ accounts for our clients on our cluster of database servers.

.. _MySQL: http://mysql.com/
.. _PostgreSQL: http://www.postgresql.org/

Co-Location Hosting
-------------------

For those projects that need more than just a single virtual machine or website, we do offer co-location hosting. We
have limited space, power and cooling but we generally can host something provided there is a warranted need for it.
Please note that the OSL generally prefers projects to virtualize as much of their infrastructure as possible.

We require all servers to have sliding rails and cable management arms. Hardware must be purchased from a vendor rather
than built by hand to ensure it operates as intended. We prefer that hardware also includes dual power, some type of
out-of-band management (i.e. IPMI, iLO, iDRAC, etc) and a three-year basic hardware warranty. We prefer not to host any
machines larger than 2U, but can work with our clients to accommodate larger servers if needed.

Monitoring
----------

Realtime
^^^^^^^^

We use `Nagios`_ to monitor our managed hosts and send alerts to `PagerDuty`_ when services go down. We are able to
offer fine-grained monitoring and notification to our hosted clients as needed. In addition, we use `Prometheus`_ with
`Grafana`_ to track various metrics of our infrastructure.

.. _Nagios: http://nagios.org/
.. _PagerDuty: http://pagerduty.com/
.. _Prometheus: https://prometheus.io/
.. _Grafana: https://grafana.com/

Trend Graphs
^^^^^^^^^^^^

We primarily use `Munin`_ to monitor the health of servers at the OSL. Statistics such as CPU usage, load, memory,
network traffic and more can all be monitored and historically tracked.

.. _Munin: http://munin-monitoring.org/

Backups
-------

This service is to be used for disaster recovery rather than data recovery, meaning we keep backups for a limited
period of time (usually long enough to provide a couple of full data sets that can be used to rebuild a server as
opposed to recovering files from long ago). We currently utilize `rdiff-backup`_ for file storage backups and a variety
of other tools for database backups.

.. _rdiff-backup: http://www.nongnu.org/rdiff-backup/
