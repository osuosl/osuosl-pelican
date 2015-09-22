Mysql1-vip Outage Post-Mortem
=============================
:date: 2015-08-07
:author: jordane
:slug: mysql1-vip-outage-post-mortem
:img: outagepic2_0.jpg
:order: 200

**Background**

On July 15th we ran into a number of issues with replication on mysql2 on a
couple of session tables. This caused replication to be paused, and a large
number of statements had to be skipped. Replication was restarted successfully.
On July 16th some more issues with the same tables were encountered, but in far
greater number. A ticket was created to track the issue. Replication was
restarted several times, but on the week of the 20th a decision was made to
entirely reload mysql2 and examine some alternative replication methods
(primarily row-based replication).

Our servers, mysql1 and mysql2, are running mysql 5.5. While documentation and
tribal knowledge claimed a master-slave replication set-up, they were configured
as master-master replication.

**What Happened**

On July 30th a decision was made to reload mysql2 at 4:00PM PDT to fix
replication errors. Slave replication was intentionally stopped. Databases were
dropped one at a time on mysql2 with a small delay between each drop.

As mentioned previously, mysql1 and mysql2 were unexpectedly set up in
master-master replication configuration. Therefore, though slave replication on
mysql2 was stopped,  mysql2 was still sending commands to mysql1. This caused
databases to be dropped on both machines. Thanks to the script delays we
realized after a few minutes that mysql1 was dropping databases and the script
was stopped. We then immediately started working to restore the databases.

**Why restores took so long**

As demand for the mysql cluster has grown, our backup strategy has shifted to be
optimized to save disk space, our greatest resource bottleneck. This has been a
worthwhile tradeoff in the past, as we have rarely had to do full restores. We
use mysql-zrm to back up mysql with heavy compression. Because of this strategy,
restores were largely CPU-bound instead of IO-bound.

We also discovered we had a couple of databases that had issues restoring due to
indexing and foreign keys. Each time one of these failed, we had to parse the
entire backup file (around 200GB), and pull out the bad database to restore
separately, and then pull out the rest of the unrestored databases.

A further complication was that our backups were pointed at mysql2, which was
out-of-date with mysql1, due to the initial synchronization failures.
Fortunately, we had the binary logs from the 17th through the 30th. This means
that though most data could be restored, some data from between the 15th and the
17th was lost.

These three factors combined meant a much slower, and much more labor-intensive
restore process than we had anticipated.

**Looking Forward**

We learned a lot of important lessons from this outage, both related to how we
run our mysql cluster, as well as how we plan and manage resources at the OSL in
general.

Most immediately, some of the most important changes we will implement for the
mysql service over the next month or two include:

#. Evaluating better replication strategies to mitigate the initial cause,
   including row-based replication

#. Storing binlogs as a backup on a separate server.

#. Doing backups using Percona XtraBackup, allowing for much faster full
   restores

#. Using mydumper rather than mysql-zrm to improve the speed of our logical
   backups

#. Work on our documentation and training for our complex systems, including

   #. Regularly testing full restores as part of our backup process on a spare
      server

   #. Gather more accurate ETAs for the restoration process

   #. Regularly audit the databases we host -- Multiple test and ballooning
      databases (100GB+) seriously delayed the restore process

#. Migrate to a bigger, more powerful mysql cluster (already planned before this
   outage)

In terms of the bigger picture, we recognize that we need to change how the lab
plans, monitors, and manages resources and projects. Despite our best efforts,
the backlog of hosting requests to the OSL continues to grow. We have, over the
years, worked hard to stretch our resources to provide services to as many
projects as we can. This has always come with tradeoffs, such as the compression
of backups to maximize disk use, and less redundancy than we would have wished.

We have for a while been concerned about how thinly resources have been
stretched, and have been working on a set of policy changes, as well as raising
funds to reinvest in the lab. Some of you may have heard our staff talk about
this plan -- we hope to talk to a lot more of you about this in the near future.
Our new FTP cluster, perhaps one of our most neglected pieces of infrastructure,
was an important first step in this renewal.

Over the next few months, the OSL will be looking at a number of different
services and policies, including:

#. Instituting a policy and mechanisms for better keeping the community informed

   #. Of outages, maintenance, etc.

   #. Of resource use & warning signs (dashboards)

#. Identifying and redesigning “core” services, including

   #. Defining and monitoring capacity limits

   #. Implementing redundancy and restore practices, including staff drills

   #. Migrating more of these services to Chef

   #. Instituting periodic review of documentation, policies and performance
      metrics

   #. Finding better ways of leveraging community expertise to supplement our
      own

#. Raising funds to refresh our most aging infrastructure, and catch up on the
   worst of our technical debt.

We want to thank you for your patience and support during this outage and over
the years we have served you. We realize that the length of this outage, and the
lack of progress reports was unacceptable, and we want you to know that we are
taking steps to reduce both the likelihood and the impact of future outages.
