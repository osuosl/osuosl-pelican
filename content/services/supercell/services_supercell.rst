Supercell
=========
:slug: services/supercell
:title: Supercell
:order: 20
:menu_parent: t4
:menu_gchild: t4s3

.. image:: /images/supercell.png
    :scale: 40%
    :alt: Supercell


What is Supercell?
------------------

The OSUOSL Supercell cluster is a service that will enable projects to do
testing for their software on various operating systems. This generally falls
into the following types of requirements:

- Continuous build integration on various architectures/operating systems
- Run-time tests of application
- Low-level debugging (for non-x86 architectures)


Currently the cluster consists of x86-based virtualization machines using `Linux
KVM`_ and managed via `Ganeti`_. Users of the system will interact with their
VM's via `Ganeti Web Manager`_ to create, remove and access the VNC console to
their VM's. The majority of the Supercell infrastructure is powered by `Gentoo
Linux`_.

.. _Linux KVM: http://www.linux-kvm.org/page/Main_Page
.. _Ganeti: http://code.google.com/p/ganeti/
.. _Ganeti Web Manager: http://code.osuosl.org/projects/ganeti-webmgr
.. _Gentoo Linux: http://www.gentoo.org/


Supercell is currently in early beta as a few partner open source projects help
us test out the cluster. You can sign up to receive an announcement when the
cluster is opened up for additional testers by completing our `Feedback Form`_.

.. _Feedback Form: /services/supercell/request


Which guest operating systems does Supercell support?
-----------------------------------------------------

The current supported guest operating systems are:

- Debian 32/64bit
- CentOS 32/64bit
- Gentoo 32/64bit
- Gentoo 32/64bit Hardened
- Ubuntu 32/64bit


Do you have plans to support other guest operating systems?
-----------------------------------------------------------

We hope to eventually add support for the following operating systems:

- Fedora
- FreeBSD
- OpenSUSE
- Windows


We need your help to determine which guest operating systems the community would
most like to see us support. Please take a moment to fill out our `Feedback
Form`_ to share your thoughts and to be notified when Supercell is ready for use
by more open source projects.

.. _Feedback Form: /services/supercell/request


What about testing on OSX?
--------------------------

We currently have two Mac OS X XServe machines available for testing software
on. We only offer shared ssh accounts currently.


Do you have plans to support architectures beyond x86?
------------------------------------------------------

We hope to eventually support other architectures, but that is a long-term goal.
Eventually, we would like to support the following architectures:

- Alpha
- ARM
- ARMel
- HPPA
- IA-64
- MIPS
- MIPSel
- PowerPC
- SPARC





What kind of hardware is used for the Supercell cluster?
--------------------------------------------------------
+---------------+-------------------+---------+--------------------+---------------+
| Hardware Type | CPU               | RAM     | Disk               | Services      |
+===============+===================+=========+====================+===============+
| 2 x Dell R815 | 4 x Opteron 6172  | 128G    | 6 x 300GB 10K SAS  | Ganeti Node   |
|               | (2.1 Ghz, 12-core)|         |                    |               |
+---------------+-------------------+---------+--------------------+---------------+
| Dell R510     | 2 x Intel E5620   | 12G     | 12 x 1T 7.2K       | NFS Storage   |
|               | (2.4Ghz, 4-core)  |         | near-line SAS      |               |
+---------------+-------------------+---------+--------------------+---------------+
| 2 x Apple     | Intel Xeon        | 24G     | 1 x 160G 7.2 SATA  | Mac OS X      |
| Xserve        | (2.26Ghz, 4-core) |         |                    | testing       |
+---------------+-------------------+---------+--------------------+---------------+



Where can I learn more about the Supercell architecture?
--------------------------------------------------------

To learn more about how the Open Source Lab uses Ganeti, check out Lance
Albertson's `blog post`_ and his presentation from `LinuxCon 2010`_.

.. _blog post: http://www.lancealbertson.com/2010/12/ganeti-at-the-osuosl/
.. _LinuxCon 2010: http://www.lancealbertson.com/slides/ganeti-linuxcon10/#1


When can I use Supercell?
-------------------------

Supercell is currently in early beta. We're rolling out the service to a few
project partners for use, and we look forward to their feedback on how we can
improve Supercell. We hope to open it up to the wider open source community very
soon.


How much will it cost for open source projects to use Supercell?
----------------------------------------------------------------

We have no plans to charge open source projects for using this service. The
creation of Supercell was made possible through a generous monetary and hardware
donation from `Facebook`_ and their `Open Source Team`_. The OSU Open Source Lab
is currently seeking additional `Sponsors`_ for the Supercell project.

.. _Facebook: http://facebook.com/
.. _Open Source Team: http://developers.facebook.com/opensource/
.. _Sponsors: /services/supercell/sponsors
