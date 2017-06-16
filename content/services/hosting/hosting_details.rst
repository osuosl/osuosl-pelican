Hosting Details
===============
:slug: services/hosting/details
:title: Hosting Details
:menu: Hosting, Hosting Details, 2

We offer a wide variety of services to our hosted clients so the OSL can help
offload work from your machine and/or infrastructure team. This list is not
exhaustive, but is intended to give a better idea of the types of services we
provide.

Virtualization
--------------

.. image:: /images/sysadmin.jpg
    :scale: 100%
    :align: right
    :alt: Hosting Detail - Sysadmin

Ganeti
^^^^^^

We offer virtual machines utilizing an open source stack consisting of `Ganeti`_ and the `KVM hypervisor`_. We have a
cluster for small projects and offer VMs at a variety of sizes and platforms, all with full redundant storage. Ganeti
is an Infrastructure as a Service (`IaaS`_) platform that we primarily use for long running VMs that need minimal
changes. We provide minimal admin access to the VMs to project owners.

.. _Ganeti: http://www.ganeti.org/
.. _KVM hypervisor: http://www.linux-kvm.org/page/Main_Page
.. _IaaS: https://en.wikipedia.org/wiki/Cloud_computing#Infrastructure_as_a_service_.28IaaS.29

OpenStack
^^^^^^^^^

*ETA late 2017*

We're working on offering access to an `OpenStack`_ cluster hosted at the OSL for projects to use in late 2017. We've
been running an internal cluster for several years and have been working on getting the platform in a stable state for
us to start offering to the projects. For now the target is primarily for compute services but we may expand that later
as the need arises.

.. _OpenStack: http://openstack.org

FTP Mirroring
-------------

We have a cluster of three servers behind the `ftp.osuosl.org`_ name with a total bandwidth capacity of more than 50
gigabits per second. These servers are hosted geographically across the United States. Instead of pushing files and
releases out from your own server, let us take care of the dirty work for you. We currently host approximately 100
projects on our mirroring servers using around 8TB of disk space. We do our best to host as many projects as we can,
however space is limited.

.. _ftp.osuosl.org: http://ftp.osuosl.org/

E-Mail
------

Mail Relaying
^^^^^^^^^^^^^^

We have a number of local mail relays that OSL-hosted servers can use to help relieve some of the pressure that mail
can put on their servers. These relays do spam and virus tagging.

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
offer fine-grained monitoring and notification to our hosted clients as needed.

.. _Nagios: http://nagios.org/
.. _PagerDuty: http://pagerduty.com/

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
