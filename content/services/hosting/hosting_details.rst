Hosting Detail
==============
:slug: services/hosting/details
:title: Hosting Detail
:order: 14
:menu_parent: t4s1


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

We offer virtual machines utilizing an open source stack consisting of `Ganeti`_
and the `KVM hypervisor`_. We have a cluster for small projects and offer VMs
that range in specs from 512M RAM/10G disk to 2G RAM/30G disk, all with full
redundancy. For more information, see our article on `Ganeti at the OSUOSL`_.

.. _Ganeti: http://code.google.com/p/ganeti/
.. _KVM hypervisor: http://www.linux-kvm.org/page/Main_Page
.. _Ganeti at the OSUOSL: http://www.lancealbertson.com/2010/12/ganeti-at-the-osuosl/


Additionally, we can host virtualization clusters and maintain the
virtualization backend (using Ganeti and KVM), but allow clients to manage their
own clusters. Most Linux/BSD distributions are currently supported, and we can
can quickly deploy Debian, Ubuntu, CentOS and Gentoo. Other operating systems
will need to be installed manually.


DNS Management
--------------

We offer Web-based DNS management and IP allocation through Maintain, a
homegrown project of the OSL. Hosted clients can be given access to administer
their own domain name using our Web interface. For more information about the
Maintain application itself and how you can use it for managing DNS, IP and DHCP
in your own organization, see `maintainproject.osuosl.org`_.

.. _maintainproject.osuosl.org: http://maintainproject.osuosl.org/


Nagios Monitoring
-----------------

We use `Nagios`_ to monitor our managed hosts and send alert pages when things
go down. We are able to offer fine-grained monitoring and notification to our
hosted clients.

.. _Nagios: http://nagios.org/


Graph Monitoring
----------------

Either `Cacti`_ or `Munin`_ can be setup to monitor the health of servers at the
OSL. Statistics such as CPU usage, load, memory, network traffic and more can
all be monitored and historically tracked.

.. _Cacti: http://www.cacti.net/
.. _Munin: http://munin-monitoring.org/


Database Management
-------------------

We offer hosted `MySQL`_ or `PostgreSQL`_ accounts for our clients on our
cluster of database servers. Access to your database is available using
`phpMyAdmin`_ or `phppgadmin`_. We also offer CLI access.

.. _MySQL: http://mysql.com/
.. _PostgreSQL: http://www.postgresql.org/
.. _phpMyAdmin: http://www.phpmyadmin.net/
.. _phppgadmin: http://phppgadmin.sourceforge.net/


Backups
-------

This service is to be used for disaster recovery rather than data recovery,
meaning we keep backups for a limited period of time (usually long enough to
provide a couple of full data sets that can be used to rebuild a server as
opposed to recovering files from long ago). Backups are handled by a server with
close to 30 terabytes of attached storage using `Bacula`_.

.. _Bacula: http://www.bacula.org/


FTP Mirroring
-------------

We have a cluster of FTP servers behind the `ftp.osuosl.org`_ name with a total
bandwidth of more than 3 gigabit per second. Instead of pushing files and
releases out from your own server, let us take care of the dirty work for you.
For the current cluster status, see our `FTP Map`_.

.. _ftp.osuosl.org: http://ftp.osuosl.org/
.. _FTP Map: http://ftpmap.osuosl.org/


Mail Relaying
-------------

We have a number of local mail relays that OSL-hosted servers can use to help
relieve some of the pressure that mail can put on their servers. These relays do
spam and virus tagging.


Shared Website Hosting
----------------------

We offer shared website hosting for projects that don't quite need a full VM for
their site. Currently we support hosting `PHP`_-, `Rails`_- and `Django`_-based
websites. We are currently unable to host most Java-based Web applications,
though we intend to add support for these in the future.

.. _PHP: http://www.php.net/
.. _Rails: http://rubyonrails.org/
.. _Django: http://www.djangoproject.com/


Project Co-Location Hosting
---------------------------

For those projects that need more than just a single virtual machine or shared
website, we do offer co-location hosting. We have limited space, power and
cooling but we generally can host something provided there is a warranted need
for it. Please note that the OSL generally prefers projects to virtualize as
much of their infrastructure as possible.

We require all servers to have sliding rails and cable management arms. Hardware
must be purchased from a vendor rather than built by hand to ensure it operates
as intended. We prefer that hardware also includes dual power, some type of
out-of-band management (i.e. iLO, iDRAC, etc) and a three-year basic hardware
warranty. We prefer not to host any machines larger than 2U, but can work with
our clients to accomodate larger servers if needed.


PowerPC Development
-------------------

We offer many resources for PowerPC developers. These resources range from
dedicated PPC systems to those available for open developer accounts. See our
PowerPC development site, `powerdev.osuosl.org`_ for more information.

.. _powerdev.osuosl.org: http://powerdev.osuosl.org/
