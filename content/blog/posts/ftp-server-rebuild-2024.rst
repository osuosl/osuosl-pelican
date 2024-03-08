FTP Server Rebuild - March 2024
===============================

:date: 2024-03-07
:author: Lance Albertson
:slug: ftp-server-rebuild-2024
:img: OSLSignPicture.jpg
:tag: featured-stories

Service(s) affected:
--------------------

FTP mirroring service which includes (but not limited to) the following hostnames:

- ftp.osuosl.org
- ftp2.osuosl.org
- ftp-chi.osuosl.org
- ftp-nyc.osuosl.org
- ftp-osl.osuosl.org
- rsync.osuosl.org
- rsync2.osuosl.org

Reason for outage:
------------------

We will upgrade all three servers' operating system from CentOS 7 to AlmaLinux 8. Unfortunately, due to an issue with
how the disks were partitioned, we are unable to do in-place upgrades. This will require to do a full reinstall
including re-syncing all of the FTP content on each system after reinstallation. The re-sync will likely take multiple
days due to the size of the content.

This will be a multi-day outage and will only impact one server at a time. The affected server will be removed from the
DNS rotation of ftp.osuosl.org and rsync.osuosl.org during its outage which will minimize the impact of issues with
users. If projects or users are directly referencing ftp-osl, ftp-nyc, or ftp-chi, please make sure you change it to
ftp.osuosl.org otherwise you will be impacted by this maintenance.

Since ftp-osl acts as a primary for our mirror infrastructure, we will set up a temporary server to minimize the impact
of syncing while we reinstall the hardware running ftp-osl. This server will not be in the main DNS rotation, but it
will still be syncing content for the other servers.

Please check https://status.osuosl.org/ for any future updates to this planned outage.

Outage Window:
--------------

Currently proposed schedule for the servers:

- ftp-chi: 03/11/2024 - 03/15/2024
- ftp-nyc: 03/18/2024 - 03/22/2024
- ftp-osl: 04/01/2024 - 04/05/2024

Projects affected:
------------------

All projects with hosted content on our FTP mirror network.
