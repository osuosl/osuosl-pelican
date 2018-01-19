Ganeti Production Rebuild - Dec 11-15 & 18-19, 2017
===================================================

:date: 2017-12-06
:author: Lance Albertson
:slug: ganeti-production-rebuild-2017
:img: OSLSignPicture.jpg
:tag: outages

Service(s) affected:
--------------------

All VMs running on our production Ganeti cluster will need to be non-live
migrated to their secondary nodes (i.e. shutdown and start is required). We
expect the outages for each VM to be short (under 5 minutes each). To see a
list of VMs that are affected and when please see this `page`_. We will ensure
the VMs are pingable after the reboot, but you may want to check that services
started properly for any services we don't already monitor.

.. _page: https://goo.gl/QEQsyu

No OpenStack services will be affected by this outage.

Outage Window:
--------------

This is a multi-day outage which will impact one hypervisor per day with an
outage window of approximately two hours. If we run into an issue that can't be
resolved during the day of the planned outage, we will be pushing back this
schedule a day and notify you of the change.

Currently proposed schedule for the hypervisors:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- gprod6: 12/11/2017 9:00AM - 11:00 AM PST (1700 - 1900 UTC)
- gprod4: 12/12/2017 9:00AM - 11:00 AM PST (1700 - 1900 UTC)
- gprod3: 12/13/2017 9:00AM - 11:00 AM PST (1700 - 1900 UTC)
- gprod7: 12/14/2017 9:00AM - 11:00 AM PST (1700 - 1900 UTC)
- gprod2: 12/15/2017 9:00AM - 12:00 PM PST (1700 - 2000 UTC)
- gprod1: 12/18/2017 1:00PM - 3:00 PM PST (2100 - 2300 UTC)
- gprod8: 12/19/2017 9:00AM - 11:00 AM PST (1700 - 1900 UTC)

Reason for outage:
------------------

We're in the midst of rebuilding our Ganeti clusters to CentOS 7 and managed
via Chef. We finished our rebuild of the internal cluster this week and are
ready to proceed with rebuilding our production cluster. We have a total of 8
hypervisors in this cluster, one of which has already been migrated to Chef.
All secondary instances attached to the affected node will remain and be
re-synced once the node has been rebuilt and added back as a node. All VM data
stored on nodes will remain intact during the rebuild as only the OS partition
will be rebuilt.

To minimize the impact of outages, we're going to ensure all VMs will be
migrated to a new Chef managed node so that we do not need to do another
downtime. Once all hosts have been migrated, we'll be re-balance the cluster
and use live-migration to move VMs so that no downtime will be noticed. We
cannot use live-migration during the migration due to KVM version differences
between the new and old hosts unfortunately. We're also going to take advantage
of this downtime to replace the RAID batteries on these nodes.

If you have any questions or concerns please let us know.

Please check http://status.osuosl.org/ for any future updates to this planned outage.

Projects affected:
------------------

All hosted VMs on our production Ganeti cluster.
