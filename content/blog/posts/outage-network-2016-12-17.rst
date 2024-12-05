Network Outage 2016-12-17 Post-mortem
#####################################

:date: 2016-12-19
:author: Lance Albertson
:slug: network-outage-2016-12-17

Issue Summary
-------------

At approximately 8:28 AM PST (1628 UTC) we lost all our network connectivity in our Corvallis data center affecting all
of our customers hosted in the data center. Network connectivity was restored at approximately 11:15 AM PST (1915 UTC).
The root cause was due to our ISP losing power to their switches which provide our Internet connectivity due to a
problem with the generator.

Timeline
--------

.. csv-table::
  :header: Time, Description
  :widths: 4, 20

  8:20AM PST (approx), OSU electricians start a planned power outage affecting the building our systems are housed in.
  8:28AM PST, OSL received a page regarding several networks being off-line.
  9:12AM PST, "OSL arrives on-site and confirms our primary data center is powered on and that none of the systems
  had been rebooted."
  9:30AM PST, "OSL confirms the root cause is a UPS problem in the basement data center which houses our ISP network
  equipment."
  11:07AM PST, Power restored in basement data center.
  11:15AM PST, OSL Network was restored.

**Total Outage: 2 hours 49 minutes**

Root Cause
----------

A scheduled power outage led to a power failure in the core switch room. The failure was caused by the generator power
being out of phase going into the UPS.  The out of phase condition was rejected by the UPS and caused the UPS to run on
batteries until they expired. The generator started and ran fine and the transfer switch moved to emergency position
fine. The generator power being out of phase was the problem. When power was lost in the core switch room, the NERO
routers went off-line taking our connectivity to the Internet down as well.

We aren't positive why the generator was out of phase but we have an idea. Once we confirm that is correct we will
update this post-mortem to reflect that. In the meantime, the OSU electricians are following up with prior maintenance
logs to see if those may have caused the issue.

Resolution
----------

The problem was fixed by rewiring the UPS to match the phases the generator was producing. On the following day
(12/18/2016) a fix was applied at 10AM to rewire the generator outputs and fix the out of phase situation.  The fix was
successful and there were no additional service interruptions.

Corrective and Preventive Measures
----------------------------------

OSU is currently investigating options to avoid this in the future. OSU is also currently working on building out a
second fiber plant on the other side of campus as a backup. Once that is completed (hopefully within the next year),
this should remove the single point of failure we have currently with our upstream Internet connection. As of right
now, all external connectivity goes through this single data center.

Problems during Recovery
^^^^^^^^^^^^^^^^^^^^^^^^

Even though this outage was not directly caused by OSL equipment, we did discover a few problems during the outage:

- An email was sent by OSU on December 1 announcing the planned outage, however the OSL was not notified until the day
  prior to the outage at the end of the work day.
- Email communication was completely down due to the fact all of our relays are in the Corvallis data center. We relied
  on communicating via our IRC channel and our Twitter account.
- No off-site status page was published nor in an updated state.
- Lack of network access to our jumphost made it very difficult to log into off-site hosts.

Changes that need to be made
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Ensure the OSL gets planned outages related to the building the data center is located in a timely manner and to more
  than one person. And also ensure we notify our customers in a timely fashion for such planned outages.
- We will be deploying an external Email relay in the coming months.
- We have updated our status page and linked it to our monitoring services so that it will be updated automatically.
  This status page can be found at http://status.osuosl.org (Thank you `Status.io`_ for donating the service!).
- We are investigating ways to allow our admins access to the systems in a secure manner while also not having to rely
  on the jumphost in case of emergencies.

.. _Status.io: http://status.io

If there are any further questions, please contact us via our IRC channel (#osuosl) on Freenode or via our support
ticket system.
