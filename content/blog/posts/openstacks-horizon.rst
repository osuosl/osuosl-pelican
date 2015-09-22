Openstack's Horizon
===================
:date: 2014-02-20 22:32
:author: Melissa
:slug: openstacks-horizon
:img: tech-blog.png
:order: 200

*The first tech post is by Chance Zibolski, a community system administrator and
project lead of Ganeti Web Manager, a Web administration panel that allows
administrators and clients access to administer and use Google’s open source
cloud infrastructure.*

Recently the OSU Open Source Lab has been experimenting with different
technologies, in particular Openstack. We already use Ganeti as our production
virtual machine and cluster management system and have written a web front end
called Ganeti Web Manager. The whole purpose of the web manager is to allow us
to easily create new virtual machines for internal purposes and to provide our
customers with cheap, redundant VMs. Recently, the OSL released `Ganeti Web
Manager 0.10.2`_ and we’re getting close to finishing version 0.11. With this
release, we’ve begun to discuss the future of Ganeti Web Manager and where we
should be taking it. We’ve decided to eventually rewrite it. As the project lead
of Ganeti Web Manager, it’s been my job to explore what tools and libraries we
may want to use for new versions of the project.

.. _Ganeti Web Manager 0.10.2:
   https://github.com/osuosl/ganeti_webmgr/tree/0.10.2

This is what led me to Openstack. Recently, we deployed an Openstack test
cluster in our infrastructure, and I found that its web UI (known as Horizon)
provides a lot of awesome functionality to Openstack users. The dashboard
provides a full interface to the existing Openstack CLI tools, and lets users
create new VMs with a few clicks of a button, all using a web interface. I began
to explore how we might be able to use Horizon in order to accomplish our
rewrite. As I discovered on the `Horizon Github`_ page the project has already
been mostly separated out from the Openstack dashboard and can be used as a
general purpose dashboard library for Django. Horizon provides utilities from
mapping Django models to interactive/editable tables to creating tabbed page
layouts and multiple step modal windows for performing actions.

.. _Horizon Github: https://github.com/openstack/horizon/

.. image:: /images/openstack-screenshot.png
   :scale: 100%
   :align: center
   :alt: Openstack Screenshot

Openstack Horizon screenshot.

Utilizing the basic layout the pre-existing Openstack dashboard uses, I was able
to create a working prototype of a Horizon dashboard that interfaces with a
Ganeti cluster. (See the code here: https://github.com/osuosl/ganeti_horizon.)
It doesn’t do much—other than read cluster data and display it—and so far it
only has about three or four different pages created. Based on my testing, I
think Horizon is an excellent way to begin with a Django-based dashboard, and we
will likely use it in our rewrite.

If you will be writing a dashboard, I recommend taking a look at Horizon and
seeing if it might fit your needs. At first it may seem like it’s built for a
very specific use case, but you might be able to use it in your next dashboard
project.
