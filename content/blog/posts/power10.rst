Now Providing Access to POWER10 for Open Source Projects
========================================================

:date: 2024-08-15
:author: Lance Albertson
:slug: power10
:img: OSLSignPicture.jpg
:tag: featured-stories

We are is excited to announce a major upgrade to our OpenPOWER cluster, which will greatly benefit our open source
projects. In collaboration with IBM, we have successfully integrated `POWER10`_ capabilities into our current OpenPOWER
cluster, powered by `OpenStack`_ using `KVM`_ on `PowerVM`_. This enhancement represents a significant step forward in
our commitment to providing cutting-edge resources to the open-source community supporting the POWER ecosystem.

.. _POWER10: https://en.wikipedia.org/wiki/Power10
.. _OpenStack: https://www.openstack.org/
.. _KVM: https://linux-kvm.org/page/Main_Page
.. _PowerVM: https://en.wikipedia.org/wiki/PowerVM

A Leap in Computing Power: POWER10
----------------------------------

POWER10, IBM’s latest processor architecture, is designed to deliver a significant leap in performance, efficiency, and
security. It represents a new era of computing, addressing the ever-growing demands of modern applications. By
introducing POWER10, we ensure that our projects have access to state-of-the-art technology, facilitating improved
performance and innovation on the POWER platform.

A Shift from OPAL to PowerVM
----------------------------

One notable change with the POWER10 architecture is the removal of the capability to boot bare metal systems using the
`OPAL`_ firmware, which previously provided native support for KVM. A `recently released POWER10 firmware`_
reintroduces the ability to run KVM, now leveraging the PowerVM hypervisor instead of OPAL. Users should see no real
differences when using VMs except in a few rare cases such as no capability of using nested virtualization currently.

.. _OPAL: https://wiki.osdev.org/OPAL
.. _recently released POWER10 firmware: https://www.ibm.com/support/pages/node/7160349

Seamless Integration with OpenStack
-----------------------------------

Our integration of POWER10 into our existing OpenStack environment was a critical requirement which was the primary
reason we were delayed on introducing POWER10. We worked closely with IBM to beta test this new KVM enabled firmware
along with upstream Linux Kernel patches, ensuring that the transition was smooth and that the new capabilities could
be easily accessed by our projects. This effort underscores our commitment to staying at the forefront of technological
advancements and providing robust, reliable resources to our users.

Continued Support for POWER8 and POWER9
---------------------------------------

In addition to the new POWER10 capabilities, we will continue to offer support for POWER8 and POWER9 platforms for the
foreseeable future. This ensures a comprehensive range of options for our projects, allowing them to choose the most
suitable architecture for their specific needs. Our goal is to provide a versatile and powerful platform for the
open-source community to thrive.

Getting access to POWER10
-------------------------

To get access to POWER10, please fill out `this form`_. If you already have access to our POWER8 or POWER9 systems,
feel free to fill this form out again.

Thank you to IBM for making this possible!

.. _this form: /services/powerdev/request_hosting
