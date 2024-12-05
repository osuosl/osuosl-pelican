Cody Holliday on the Department of Energy Cyber Defense Competition 2018
------------------------------------------------------------------------
:title: Cody Holliday on the Department of Energy Cyber Defense Competition 2018
:date: 2018-04-23
:author: Cody Holliday
:slug: cody-holiday-cyber-defense

I took part in a Cyber Defense Competition hosted by the Department of Energy, and it was a fantastic experience! Our
team worked hard to ensure that we had a fighting chance at the competition, and we had much needed help from our
mentor.

The competition took place in a control center. One wall covered in flat screen TVs to create a huge monitor and the
other was lined with windows into the room where the Red Team worked. There was a table for each of the 6 teams, and on
each table was a small model of a natural gas extractor with two little houses around it. This little model simulated a
power plant -- the thing we would be defending against cyber attacks.

A team of normal users, known as the Green Team, needed to access the interface for this system and we had to stop any
malicious actors from accessing it.

The competition simulated a power plant defense scenario where a team of hackers would try to disrupt a town's power
supply. We were given three Linux virtual machines to use that were laden with backdoors and vulnerabilities. I was
responsible for removing the backdoors on those virtual machines as well as setting up LDAP logins for those hosts.
Unfortunately our LDAP users were in an Active Directory instance, so I needed to interface Kerberos with Active
directory to allow logins through LDAP. Despite my many attempts at configuring Kerberos I kept running into the
enigmatic "su: system error". In hindsight I should have investigated "su", but I had my blinders on trying to get LDAP
to work. Besides configuring LDAP, I removed a couple webservers that were running backdoor services and locked down
some service accounts that had way too many permissions.

The final network layout consisted of 8 virtual machines: one web server, one MySQL/FTP server, one HMI access server,
two Windows DNS/Active Directory servers, two honey pots, and one access server. Ssh access to the first three servers
was limited so that only the access server could connect to them via ssh.

The most exciting thing happened when our teammate Aiden had to literally fight off a Red Team member through the user
interface for our extractor. Red Team kept turning off the extractor, so Aiden turned it back on. Once Red Team knew we
were watching, they opened up a bunch of windows to keep us from turning the machine back on. We frantically threw a
firewall into place to block them while we reconfigured the controller for our extractor.

When we were nearing the end of the competition the Red Team taunted all the Blue Teams by playing Disco Inferno and
burning out the motors of all the extractors that were compromised.

By the end we were in 2nd or 3rd place nationally before the final scoring.  Once the final score had been released we
were surprised to see that other school had risen so much that we were in fourth nationally, but we were definitely
pleased to see that we had won first at our location. All in all it was a rewarding experience that I wish I could do
again this coming fall, but that is another story all to itself.
