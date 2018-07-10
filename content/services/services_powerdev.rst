PowerLinux / OpenPOWER Development Hosting
==========================================
:slug: services/powerdev
:title: POWER Development Hosting
:menu: Services, POWERLinux/OpenPOWER Development Hosting, 3

The Open Source Lab partners with `IBM`_ to host `POWER`_ based servers in order
to provide an open platform for innovation to the open source community. Current
projects embrace open software projects ranging from KVM to OpenStack and open
collaboration with `OpenPOWER Foundation`_ partners, including `NVIDIA`_,
`Mellanox`_, `Ubuntu`_ and `Google`_, and open source based ISV and distribution
partners, such as `Chef`_, Red Hat, SUSE and Ubuntu, who support the latest
POWER hardware via production and development (Fedora, CentOS, OpenSUSE, and
Debian) distributions.

.. _IBM: http://www-03.ibm.com/linux/ltc/
.. _POWER: http://en.wikipedia.org/wiki/IBM_POWER_microprocessors
.. _OpenPOWER Foundation: http://openpowerfoundation.org
.. _NVIDIA: http://www.nvidia.com
.. _Mellanox: https://www.mellanox.com
.. _Ubuntu: http://www.ubuntu.com
.. _Google: https://opensource.google.com/
.. _Chef: https://www.chef.io/chef/

Members of the community can use these POWER servers to develop and test open
source projects on the `Power Architecture`_ platform and in a `PowerLinux`_
environment. Developers looking for assistance can go to the `Linux on IBM Power
Systems Developer`_ portal or `IBM Portal for OpenPOWER`_.

.. _Power Architecture: http://en.wikipedia.org/wiki/Power_Architecture
.. _PowerLinux: http://en.wikipedia.org/wiki/PowerLinux
.. _Linux on IBM Power Systems Developer: https://developer.ibm.com/linuxonpower/
.. _IBM Portal for OpenPOWER: https://www-355.ibm.com/systems/power/openpower/


* List of `Current Projects & Academic Partners`_

* List of `Former Projects & Academic Partners`_

.. _Current Projects & Academic Partners: /services/powerdev/current-projects
.. _Former Projects & Academic Partners: /services/powerdev/former-projects

Two clusters of POWER resources are hosted at the Open Source Lab:

OpenStack
---------

The first cluster is an OpenStack based cluster offering POWER8 (POWER9 once available)
LE instances running on KVM and providing access via OpenStack's API and GUI
interface.  These shared systems are intended for functional development and
continuous integration work, but are not ideal for performance testing.  We
start projects out with a small quota, but can increase given resource
availability and justification.

To request access to an OpenStack POWER instance, use our `OpenPOWER OpenStack request form`_.

.. _powerci:

POWER Continuous Integration (POWER CI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hosted via the OpenStack cluster is an OSL managed Jenkins service which is hosted at https://powerci.osuosl.org. This
service is intended to allow projects easier access to the POWER architecture via Jenkins.

Users can request access to register one or more GitHub repositories on the Jenkins server, where they can configure
the build process and the environment as needed.  Builds will run in a Docker container by default, but can also be run
in a virtual machine if need be. Users can also configure the system to run their tests, package any necessary files
and binaries after running the build, and archive the build artifacts on the Jenkins server for later access. The
service also supports providing e-mail notifications on build status and embedded build-notification for webpages.

To request access to the POWER CI service, use our `POWER CI request form`_.

GPU
---

The second cluster is an OpenPOWER GPU based acceleration cluster offering POWER8+ "Minsky" servers with NVIDIA P100
GPUs connected via NVLink. This cluster is hosted and provided by the `Center for Genome Research & Biocomputing
(CGRB)`_ at OSU through a partnership with the OSU Open Source Lab. This platform is powered using `Sun of Grid Engine
(SGE)`_ instead of our OpenStack infrastructure. This platform has access to a variety of software and libraries and
also includes access to GPU enabled Docker. For more information on how this infrastructure is setup, please read this
`PDF`_.

To request access to the OpenPOWER GPU cluster, use our `OpenPOWER GPU request form`_.

.. _OpenPOWER OpenStack request form: /services/powerdev/request_hosting
.. _POWER CI request form: /services/powerdev/request_powerci
.. _Center for Genome Research & Biocomputing (CGRB): http://cgrb.oregonstate.edu/
.. _Sun of Grid Engine (SGE): https://arc.liv.ac.uk/trac/SGE
.. _PDF: /downloads/OpenPOWER_Developement_GPU_Access.pdf
.. _OpenPOWER GPU request form: /services/powerdev/request_gpu
