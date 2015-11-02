PowerLinux / OpenPOWER Development Hosting
==========================================
:slug: services/powerdev
:title: Development Hosting
:menu: Services, Development Hosting, 3

.. |br| raw:: html

    <br />

The Open Source Lab partners with `IBM`_ to host `POWER`_ based servers in order
to provide an open platform for innovation to the open source community. Current
projects embrace open software projects ranging from KVM to OpenStack and open
collaboration with `OpenPOWER Foundation`_ partners, including `Mellanox`_,
`Ubuntu`_ and `Google`_, and open source based ISV and distribution partners,
such as `Chef`_, Red Hat, SUSE and Ubuntu, who support the latest POWER hardware
via production and development (Fedora, OpenSUSE, and Debian) distributions.

Members of the community can use these POWER servers to develop and test open
source projects on the `Power Architecture`_ platform and in a `PowerLinux`_
environment. These shared systems are intended for functional development and
testing work, but are not ideal for performance testing.

We offer either POWER7+ big endian instances using LPARs or POWER8 big or little
endian instances running on KVM and providing access via OpenStack's API and GUI
interface. The POWER8 instances offer much more flexibility, giving the ability
to spin up or down instances on demand. We start projects out with a small
quota, but can increase given resource availability and justification.

To request access to a POWER server, use our `request form`_ and we will get
back to you shortly.

.. _IBM: http://www-03.ibm.com/linux/ltc/
.. _POWER: http://en.wikipedia.org/wiki/IBM_POWER_microprocessors
.. _OpenPOWER Foundation: http://openpowerfoundation.org
.. _Mellanox: https://www.mellanox.com
.. _Ubuntu: http://www.ubuntu.com
.. _Google: https://www.google.com
.. _Chef: https://www.chef.io/chef/
.. _Power Architecture: http://en.wikipedia.org/wiki/Power_Architecture
.. _PowerLinux: http://en.wikipedia.org/wiki/PowerLinux
.. _request form: /services/powerdev/request_hosting

Current Projects Hosted on POWER
--------------------------------

This is the list of projects using the POWER8 cluster powered by OpenStack at
the OSL.

Open Source Projects
~~~~~~~~~~~~~~~~~~~~

+-----------------------------+------------------------------------------------+
|Apache Software Foundation   | The ASF is currently working on supporting     |
|                             | POWER builds for CouchDB and possibly other ASF|
|                             | projects in the future. The current goal is to |
|                             | support Cloudant on POWER.                     |
+-----------------------------+------------------------------------------------+
|CentOS                       | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the CentOS project.          |
+-----------------------------+------------------------------------------------+
|Cloud Foundry                | Supporting porting of Cloud Foundry on POWER,  |
|                             | continuous integration with Cloud Foundry, and |
|                             | builds integration with Cloud Foundry.         |
+-----------------------------+------------------------------------------------+
|CRIU                         | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the CRIU project.            |
+-----------------------------+------------------------------------------------+
|Drupal                       | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the Drupal project.          |
+-----------------------------+------------------------------------------------+
|DBSI                         | Supporting porting efforts of POWER8 ppc64le   |
|                             | for the DBSI project.                          |
+-----------------------------+------------------------------------------------+
|Gentoo                       | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the Gentoo project.          |
+-----------------------------+------------------------------------------------+
|Docker                       | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the Docker project.          |
+-----------------------------+------------------------------------------------+
|Glibc                        | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the GNU C Library, commonly  |
|                             | known as glibc project.                        |
+-----------------------------+------------------------------------------------+
|GoLang                       | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the GoLang project.          |
+-----------------------------+------------------------------------------------+
|Haskell                      | Implement native code generation on PowerPC    |
|                             | 64-bit little endian for "The Glorious Glasgow |
|                             | Haskell Compilation System" and as a           |
|                             | pre-release for openSUSE and SUSE Linux        |
|                             | Enterprise on POWER8 servers, while we are     |
|                             | waiting for upstream to release version 7.12.  |
|                             |                                                |
|                             | In a follow-up project they plan to do research|
|                             | on hardware transactional memory features of   |
|                             | POWER8 in addition and compared to Haskell's   |
|                             | software transactional memory implementation.  |
+-----------------------------+------------------------------------------------+
|JXCore                       | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the JXCore project. The goal |
|                             | is to provide stable POWER releases for both   |
|                             | Node.js and JXCore.                            |
+-----------------------------+------------------------------------------------+
|libjpeg-turbo                | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the libjpeg-turbo project.   |
+-----------------------------+------------------------------------------------+
|LLVM                         | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the LLVM project to run their|
|                             | buildbot instances. These instances build LLVM |
|                             | and run the test suites when patches are       |
|                             | checked in to ensure they run properly on the  |
|                             | POWER architecture.                            |
+-----------------------------+------------------------------------------------+
|LTTng                        | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the LTTng project.           |
+-----------------------------+------------------------------------------------+
|Node                         | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the Node project. The goal   |
|                             | is to provide stable POWER releases for        |
|                             | community builds of Node.js.                   |
+-----------------------------+------------------------------------------------+
|Nokogiri                     | BountySource ticket focused on fixing compiling|
|                             | issues of Nokigiri on the POWER8 architecture. |
+-----------------------------+------------------------------------------------+
|OpenJDK                      | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the OpenJDK project. The goal|
|                             | is to provide support for Java 7 and 8 which is|
|                             | being consumed by most major distributions.    |
+-----------------------------+------------------------------------------------+
|oVirt                        | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the oVit project.            |
+-----------------------------+------------------------------------------------+
|libjpeg-turbo                | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the libjpeg-turbo project.   |
+-----------------------------+------------------------------------------------+
|UAUC                         | Supporting University of Alberta and           |
|                             | Universidade de Campinas work on the POWER8    |
|                             | architecture.                                  |
+-----------------------------+------------------------------------------------+
|UMBC                         | Supporting University of Maryland, Baltimore   |
|                             | County work on the POWER8 architecture.        |
+-----------------------------+------------------------------------------------+
|Zarafa                       | Supporting porting efforts of POWER8           |
|                             | ppc64/ppc64le for the Zarafa project.          |
+-----------------------------+------------------------------------------------+

Academic Partners
~~~~~~~~~~~~~~~~~

+-----------------------------+------------------------------------------------+
|University of Alberta and    | The goal is to investigate the use of the      |
|Universidade de Campinas     | speculation support in POWER8 for the speeding |
|                             | up the sequential execution of programs.       |
|                             | Single-threaded speculation has been used in   |
|                             | the past, through trace-based compilation. The |
|                             | goal of this project is to investigate         |
|                             | multi-threaded speculation of alternative paths|
|                             | of execution in a sequential execution.        |
|                             |                                                |
|                             | This is a joint project between University of  |
|                             | Alberta (UofA) and Universidade de Campinas    |
|                             | (Unicamp).                                     |
+-----------------------------+------------------------------------------------+
|Berkeley Lab                 | BLCR is "Berkeley Lab Checkpoint/Restart", a   |
|Checkpoint/Restart           | kernel-level checkpointer implemented via a    |
|                             | loadable kernel module and a userspace library.|
|                             |                                                |
|                             | Project home: http://ftg.lbl.gov/checkpoint    |
+-----------------------------+------------------------------------------------+
| Harvey Mudd College         | Observationally Cooperative Multithreading     |
|                             | (OCM) provides a "kinder gentler" form of      |
|                             | concurrency, allowing programmers to imagine   |
|                             | that a single thread runs on the machine at any|
|                             | one time. With POWER8 hardware transactional   |
|                             | memory, it becomes possible to actually run    |
|                             | multiple threads at the same time while        |
|                             | *appearing* to be running only one at a time.  |
+-----------------------------+------------------------------------------------+
