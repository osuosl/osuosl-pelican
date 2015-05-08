Skip to main content ` OREGON STATE UNIVERSITY`_ ` `_ `School of
Electrical Engineering and Computer Science`_


`OSU Open Source Lab`_
======================


  +

    + `Home`_
    + `About Us`_

        + `Summary`_
        + `Staff`_
        + `Employment`_
        + `DevOps BootCamp`_
        + `Advisors`_
        + `Contact`_
        + `Open Source Lab logos`_
        + `GOSCON`_

    + `Blog`_
    + `Services`_

        + `Hosting`_
        + `Development`_
        + `Request Hosting`_
        + `PowerLinux / OpenPOWER Development Hosting`_
        + `Supercell`_

    + `GSoC`_
    + `Donate`_

        + `Sponsors`_
        + `Why Do We Give to the OSL?`_


  +

    + `Calendar`_
    + `Library`_
    + `Maps`_
    + `Online Services`_
    + `Make a Gift`_




+ `Home`_
+ `About Us`_

    + `Summary`_

        + `Student Experience`_
        + `FAQ`_

    + `Staff`_
    + `Employment`_
    + `DevOps BootCamp`_
    + `Advisors`_
    + `Contact`_
    + `Open Source Lab logos`_
    + `GOSCON`_

+ `Blog`_
+ `Services`_

    + `Hosting`_

        + `Hosted Projects`_
        + `Hosting Details`_
        + `Hosting Policy`_

    + `Development`_
    + `Request Hosting`_
    + `PowerLinux / OpenPOWER Development Hosting`_

        + `PowerLinux / OpenPOWER Request Form`_

    + `Supercell`_

        + `Feedback Form`_
        + `Sponsors`_


+ `GSoC`_
+ `Donate`_

    + `Sponsors`_
    + `Why Do We Give to the OSL?`_





Supercell
---------




What is Supercell?
~~~~~~~~~~~~~~~~~~

The OSUOSL Supercell cluster is a service that will enable projects to
do testing for their software on various operating systems. This
generally falls into the following types of requirements:


+ Continuous build integration on various architectures/operating
  systems
+ Run-time tests of application
+ Low-level debugging (for non-x86 architectures)


Currently the cluster consists of x86-based virtualization machines
using `Linux KVM`_ and managed via `Ganeti`_. Users of the system will
interact with their VM's via `Ganeti Web Manager`_ to create, remove
and access the VNC console to their VM's. The majority of the
Supercell infrastructure is powered by `Gentoo Linux`_.

Supercell is currently in early beta as a few partner open source
projects help us test out the cluster. You can sign up to receive an
announcement when the cluster is opened up for additional testers by
completing our `Feedback Form`_.


Which guest operating systems does Supercell support?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The current supported guest operating systems are:




+ Debian 32/64bit
+ CentOS 32/64bit
+ Gentoo 32/64bit
+ Gentoo 32/64bit Hardened
+ Ubuntu 32/64bit



Do you have plans to support other guest operating systems?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We hope to eventually add support for the following operating systems:


+ Fedora
+ FreeBSD
+ OpenSUSE
+ Windows


We need your help to determine which guest operating systems the
community would most like to see us support. Please take a moment to
fill out our `Feedback Form`_ to share your thoughts and to be
notified when Supercell is ready for use by more open source projects.


What about testing on OSX?
~~~~~~~~~~~~~~~~~~~~~~~~~~

We currently have two Mac OS X XServe machines available for testing
software on. We only offer shared ssh accounts currently.


Do you have plans to support architectures beyond x86?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We hope to eventually support other architectures, but that is a long-
term goal. Eventually, we would like to support the following
architectures:


+ Alpha
+ ARM
+ ARMel
+ HPPA
+ IA-64
+ MIPS
+ MIPSel
+ PowerPC
+ SPARC





What kind of hardware is used for the Supercell cluster?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hardware Type CPU RAM Disk Services 2 x Dell R815 4 x Opteron 6172
(2.1 Ghz, 12-core) 128G 6 x 300GB 10K SAS Ganeti Node Dell R510 2 x
Intel E5620 (2.4Ghz, 4-core) 12G 12 x 1T 7.2K near-line SAS NFS
Storage 2 x Apple Xserve Intel Xeon (2.26Ghz, 4-core) 24G 1 x 160G 7.2
SATA Mac OS X testing



Where can I learn more about the Supercell architecture?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To learn more about how the Open Source Lab uses Ganeti, check out
Lance Albertson's `blog post`_ and his presentation from `LinuxCon
2010`_.


When can I use Supercell?
~~~~~~~~~~~~~~~~~~~~~~~~~

Supercell is currently in early beta. We're rolling out the service to
a few project partners for use, and we look forward to their feedback
on how we can improve Supercell. We hope to open it up to the wider
open source community very soon.


How much will it cost for open source projects to use Supercell?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have no plans to charge open source projects for using this
service. The creation of Supercell was made possible through a
generous monetary and hardware donation from `Facebook`_ and their
`Open Source Team`_. The OSU Open Source Lab is currently seeking
additional `Sponsors`_ for the Supercell project.

` `_



`Contact`_
++++++++++


`EECS`_
+++++++


`Donate`_
+++++++++





` `_

` `_
` `_ ` `_ ` `_ ` `_ ` `_


Newsletter Sign Up
------------------


+ E-mail Address *




Contact Info
~~~~~~~~~~~~
`Copyright`_ 2015 Oregon State University
`Disclaimer`_
OSU Open Source Lab
Kerr Admin B211
Corvallis, OR 97331
General Inquiries:
`info@osuosl.org`_
Support for Project Infrastructure
`support@osuosl.org`_
Questions about Donations:
`donations@osuosl.org`_


+ `Home`_
+ `About`_

    + `Staff`_
    + `Employment`_
    + `Advisors`_
    + `Logos`_
    + `Contact`_

+ `Blog`_
+ `Services`_

    + `Hosting`_
    + `Development`_
    + `OpenPOWER`_
    + `Supercell`_

+ `Donate`_

    + `Sponsors`_



.. _LinuxCon 2010: http://www.lancealbertson.com/slides/ganeti-linuxcon10/#1
.. _Feedback Form: /services/supercell/request
.. _Logos: /about/logos
.. _Blog: /blog
.. _School of Electrical Engineering and Computer Science: http://eecs.oregonstate.edu
.. _info@osuosl.org: mailto:info@osuosl.org
.. _blog post: http://www.lancealbertson.com/2010/12/ganeti-at-the-osuosl/
.. _Staff: /about/people
.. _Development: /services/development
.. _Gentoo Linux: http://www.gentoo.org
.. _Student Experience: /students
.. _Make a Gift: https://securelb.imodules.com/s/359/campaign/index.aspx?sid=359&gid=34&pgid=1982&cid=3007
.. _About: /about
.. _Linux KVM: http://www.linux-kvm.org/page/Main_Page
.. _Services: /services
.. _Hosting: /services/hosting
.. _Supercell: /services/supercell
.. _Hosting Policy: /services/hosting/policy
.. _donations@osuosl.org: mailto:donations@osuosl.org
.. _Hosted Projects: /communities
.. _FAQ: /donate/faq
.. _DevOps BootCamp: /about/devops-bootcamp
.. _support@osuosl.org: mailto:support@osuosl.org
.. _Home: /
.. _Online Services: http://oregonstate.edu/main/online-services
.. _OpenPOWER: /services/powerdev
.. _Donate: /donate
.. _Ganeti: http://code.google.com/p/ganeti/
.. _GOSCON: /about/goscon
.. _EECS: http://eecs.oregonstate.edu/
.. _Employment: /about/employment
.. _Maps: http://oregonstate.edu/campusmap
.. _Sponsors: /services/supercell/sponsors
.. _Facebook: http://facebook.com
.. _Advisors: /about/advisors
.. _Request Hosting: /request-hosting
.. _PowerLinux / OpenPOWER Request Form: /services/powerdev/request_hosting
.. _Open Source Team: http://developers.facebook.com/opensource/
.. _Hosting Details: /services/hosting/details
.. _Why Do We Give to the OSL?: /donate/why-do-we-give-osuosl
.. _Library: http://osulibrary.oregonstate.edu
.. _Sponsors: /sponsors
.. _Sponsors: /sevices/supercell/sponsors
.. _Contact: /contact
.. _Copyright: http://oregonstate.edu/copyright
.. _Calendar: http://calendar.oregonstate.edu
.. _Disclaimer: http://oregonstate.edu/disclaimer
.. _Ganeti Web Manager: http://code.osuosl.org/projects/ganeti-webmgr
.. _GSoC: /gsoc
.. _OREGON STATE UNIVERSITY: http://oregonstate.edu


