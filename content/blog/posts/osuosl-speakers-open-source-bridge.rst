OSUOSL Speakers at Open Source Bridge
=====================================
:date: 2010-05-10
:author: OSUOSL Admin
:slug: osuosl-speakers-open-source-bridge
:order: 200

We're always excited to see open source events happening, especially when they
are in our home state of Oregon! `Open Source Bridge`_ will have its second
annual conference June 1-4, and the Oregon State University Open Source Lab will
be well represented at the event where five of our staff (plus one OSUOSL
alumnus) will be speaking. We've got a lot of cool stuff going on at the OSUOSL
and are excited to have a chance to share some of the things we've been up to.

Want to hear about how we are handling virtualization at the OSUOSL? Lance
Albertson will be giving a talk titled
"`Creating a low-cost clustered virtualization environment using Ganeti`_" which
describes our recent migration to a redundant and easily scalable virtualization
setup using the open source project, `Ganeti`_. Come and hear about the
ups-and-downs and other juicy details of our migration from the old Xen-based
setup with central disk storage to the new Ganeti setup which uses local storage
on servers combined with DRBD for redundancy.

Maybe virtualization isn't your thing, but you'd be more interested to hear
about interactive "touchscreen" displays such as the one we use in our data
center to show network graphs, FTP downloads, and other general information.
Peter Krenesky and Rob McGuire-Dale will talk about our
`Touchscreen application`_ during their talk,
"`Building Interactive Displays with Touchscreen 2.0`_". This talk will show off
some of the cool features of Touchscreen 2.0 which has been built using Django
and jQuery.

At the OSUOSL we host a lot of high-traffic websites. From an open source
project's point of view, the more traffic to your site the better! However, from
a system administration point of view, more traffic tends to mean more headaches
as you try to keep sites fast and responsive during a flood of traffic. This can
be especially challenging when dealing with dynamic web applications such as
Drupal. Rudy Grigar and Greg Lund-Chaix have a talk titled
"`Making Drupal Go Fast with Varnish and Pressflow`_" which describes how the
combination of Varnish and Pressflow can be used to cache much more content than
a standard Drupal install -- leading to faster websites and happier servers.
They will get into details about Varnish and Pressflow and give some real-world
examples of similar setups at the OSUOSL.

We're also very happy to see Alex Polvi, a former student employee at OSUOSL,
come to give his talk: "`libcloud: a unified interface into the cloud`_". Alex
is the CEO at `Cloudkick`_ where they use `libcloud`_ to build their cloud
management and monitoring services. libcloud is an Apache Incubator project
which provides a unified interface into many cloud providers such as Amazon EC2,
Slicehost, and Rackspace.

Hopefully you're as excited as we are to head to Open Source Bridge and check
out these and many other great talks. See you there!

.. _Open Source Bridge: http://opensourcebridge.org/
.. _Creating a low-cost clustered virtualization environment using Ganeti: http://opensourcebridge.org/sessions/368
.. _Ganeti: http://code.google.com/p/ganeti/
.. _Touchscreen application: http://trac.osuosl.org/trac/touchscreen
.. _Building Interactive Displays with Touchscreen 2.0: http://opensourcebridge.org/sessions/404
.. _Making Drupal Go Fast with Varnish and Pressflow: http://opensourcebridge.org/sessions/309
.. _libcloud\: a unified interface into the cloud: http://opensourcebridge.org/sessions/419
.. _Cloudkick: http://www.cloudkick.com/
.. _libcloud: http://incubator.apache.org/libcloud/
