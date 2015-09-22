My Experiences with Openstack
=============================
:date: 2014-09-15
:author: Geoff Corey
:slug: my-experiences-openstack
:img: Geoffbloggraphic2_0.jpg
:order: 200

In the simplest of terms, `OpenStack`_ is a massive undertaking. The goal of
OpenStack is to fit just about every use case imaginable. This goal brings with
it a daunting list of configuration options and requires a larger understanding
of networking and virtualization systems. Couple that with cryptic error
messages, and this makes for a system that can easily crush a newbie's
confidence and cause them to scrap the system altogether. Luckily, there are
some projects out there trying to lower the entry bar and get more people
introduced to OpenStack. Two of the projects most referred to are `DevStack`_
(which the OpenStack developers actually use for development and testing) and
`RDO Packstack from RedHat`_. Last summer, I began teaching myself OpenStack
using Packstack. This creates a Proof-Of-Concept (POC) deployment suitable to
get comfortable with the architecture, the concepts and even some architectural
design choices. Fast forward a few months and, having gathered a much larger
(and yet still very small) understanding of how OpenStack works, the OSL
deployed the POC Packstack setup and had our Systems Admins deploying VMs to
develop and test our Chef cookbooks. Next comes the most daunting challenge:
configuration management. Configuration management requires a much greater
understanding of the underlying system because you have to know which options
should be changed and which options should not. The problem with OpenStack in
configuration management is that there are so many options to set/change in each
OpenStack service. The other challenge is knowing how to choose the best option
for your use case. You can create your own management scripts or you can look
into the various other methods being developed (such as RedHat's RDO Foreman
using Puppet or Chef's Stackforge). I first started with RDO Foreman mostly due
to the RDO support community. This community is filled with helpful and
knowledgeable people who are working on the configuration management scripts.
Ultimately, however, we went with Stackforge over RDO Foreman, mainly because
the latter lacked some flexibility we required. It also turned out that the
Stackforge project would allow for us to run multiple environments as well as
allowing us to run OpenStack on IBM Power CPUs. After a lot of testing,
tweaking, frustration (head-desking, face palming, cursing), moments of
inspiration, sudden realizations, and wonderful moments of clarity, we had a
working test environment. Next, we had to reconcile the differences between the
testing environment and the production environment (as well as throwing in
things like changing from OpenStack's Havana release to Icehouse for good
measure). Currently, we are finishing up some testing of our x86 production
OpenStack cluster and we even have a production OpenPower OpenStack cluster.
Overall, this project has been an incredible opportunity that enabled me to
experience different roles in project management, build connections in the
various OpenStack community, learn more about the underlying systems that
OpenStack uses (kvm, networking in too much detail, web servers, etc.), and,
most of all, drastically increase my abilities to debug problems with little
information while being persistent in learning how to properly fix those bugs.
Ultimately the skills and concepts developed while working with OpenStack can
be transferred to almost any setting, making it a valuable teaching tool.

.. _OpenStack: http://www.openstack.org/
.. _DevStack: http://devstack.org/
.. _RDO Packstack from RedHat: https://openstack.redhat.com/Quickstart
