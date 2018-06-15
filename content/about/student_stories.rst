Student Stories
===============
:slug: student-stories
:title: Student Stories
:menu: Student Experience, Student Stories, 3
:img: 2017_BootCamp_smaller.jpg

Our Student Stories are a special collection of experiences and thoughts from
the students themselves. Check out what our student employees find exciting and
worth taking some time to tell you about.

Goodbye Letter from Graduating Senior, Cody Holiday 
------------------------------------------------------------------

6/14/18

The Open Source Lab has treated me well. I came here bright eyed and full 
of wonder, fascinated by the racks and racks of servers we had in the data 
center. Fascinated at the treasure trove of artifacts held in the back 
room from conventions passed, old CDs labeled "Fedora 10" or "Ubuntu 8". 
That scrap of paper on the wall of an IRC log with Linux Torvalds.

I may have been infatuated with the aura of the OSL, but the what made 
it all worthwhile were the people. Justin, Chris, Anthony, Lee, Jack 
(whose goodbye is below), Taylor, and Lance were the first people I 
interacted with and they really left an impression on me. They guided me 
along pretty heavily in the beginning since I had almost no idea what 
I was doing. I had been programming for a good portion of my life, but I 
had very little server knowledge and only half a year of Linux experience 
so it's safe to say I was out of my element. They were kind and patient 
enough to hold my hand as I learned.

When the school year came around I faced some new challenges. At that 
time I was taking senior design, which was the most difficult thing I 
had done up to that point. Everyone at the OSL was understanding and
supportive. They expressed their grievances about classes and I joined in 
about Operating Systems or midterm reports or exams. It made that struggle 
a little more bearable. They were incredibly helpful too. I asked everyone 
so many questions that I was afraid they would tell me to just google it, 
but they never did. 

The best thing about OSL is the community, because without it we would 
just be another hosting provider.

I would like to say thank you to Pam for keeping this place bright and 
cheerful and for helping me when I needed it the most. Thank you Lance 
for being patient with me and for orking closely with me on important 
projects. Thank you Samar for working so closely with me on OpenStack 
Taster and for making me an integral part of the development process. 
Thank you Justin for always being willing to answer my questions, even 
when they could have just been answered by the man pages. Thank you 
(in no particular order) to Annie, Aileen, Spencer, Andy, Jerry, Bailey, 
Jason, Hunter, Mohamed, JJ, Travis, Hannah, Cayden, Levi, Cody, Taylor, 
Chris, Anthony, Jack, Lee, Amanda, Jeffrey, and Morgan. You all created 
a wonderful environment to learn and to grow as a person. 

Good luck to you wherever you go.


Mohamed Eldebri on OSL's participation in the Corvallis Maker Fair
------------------------------------------------------------------

5/07/18

On April 28th, 2018, the OSL participated in the Corvallis Maker Fair for the
second year in a row. We hosted 2 booths, the first had demos of programs in
Python and Scratch, and the second had a HAProxy cluster with diskless nodes,
which was built and deployed by OSL student JJ Frederick.

Attendees learned about the basics of programming by modifying the source code
of the demoed programs to see how it changed the programs, learned about DevOps
basics and saw how easy it was to add their laptops to the cluster as a diskless
node, and also gained an appreciation of open source software.

Cody Holliday on the Department of Energy Cyber Defense Competition 2018
------------------------------------------------------------------------

4/23/18

I took part in a Cyber Defense Competition hosted by the Department of Energy,
and it was a fantastic experience! Our team worked hard to ensure that we had a
fighting chance at the competition, and we had much needed help from our mentor.

The competition took place in a control center. One wall covered in flat screen
TVs to create a huge monitor and the other was lined with windows into the room
where the Red Team worked. There was a table for each of the 6 teams, and on
each table was a small model of a natural gas extractor with two little houses
around it. This little model simulated a power plant -- the thing we would be
defending against cyber attacks.

A team of normal users, known as the Green Team, needed to access the interface
for this system and we had to stop any malicious actors from accessing it.

The competition simulated a power plant defense scenario where a team of hackers
would try to disrupt a town's power supply. We were given three Linux virtual
machines to use that were laden with backdoors and vulnerabilities. I was
responsible for removing the backdoors on those virtual machines as well as
setting up LDAP logins for those hosts. Unfortunately our LDAP users were in an
Active Directory instance, so I needed to interface Kerberos with Active
directory to allow logins through LDAP. Despite my many attempts at configuring
Kerberos I kept running into the enigmatic "su: system error". In hindsight I
should have investigated "su", but I had my blinders on trying to get LDAP to
work. Besides configuring LDAP, I removed a couple webservers that were running
backdoor services and locked down some service accounts that had way too many
permissions.

The final network layout consisted of 8 virtual machines: one web server, one
MySQL/FTP server, one HMI access server, two Windows DNS/Active Directory
servers, two honey pots, and one access server. Ssh access to the first three
servers was limited so that only the access server could connect to them via
ssh.

The most exciting thing happened when our teammate Aiden had to literally fight
off a Red Team member through the user interface for our extractor. Red Team
kept turning off the extractor, so Aiden turned it back on. Once Red Team knew
we were watching, they opened up a bunch of windows to keep us from turning the
machine back on. We frantically threw a firewall into place to block them while
we reconfigured the controller for our extractor.

When we were nearing the end of the competition the Red Team taunted all the
Blue Teams by playing Disco Inferno and burning out the motors of all the
extractors that were compromised.

By the end we were in 2nd or 3rd place nationally before the final scoring.
Once the final score had been released we were surprised to see that other
school had risen so much that we were in fourth nationally, but we were
definitely pleased to see that we had won first at our location. All in all it
was a rewarding experience that I wish I could do again this coming fall, but
that is another story all to itself.

Jack Twilley on Leaving the OSL
-------------------------------

2/5/18

| ``About a decade ago, I was becoming disenchanted with my time in the computer``
| ``industry.  It wasn't *bad*, it just wasn't *me* anymore.  After some serious``
| ``soul searching, I decided to turn my hobby into my next career -- but I knew``
| ``that I needed formal education and training.  After some careful research, I``
| ``narrowed down my choices to two: UC Davis and Oregon State University.  Both``
| ``schools have top-tier records in my new field but it was the Open Source Lab``
| ``that tipped the balance.  After moving to Oregon I haven't once looked back.``
|
| ``After establishing residency and completing my associate degrees (all three)``
| ``at PCC, I finally moved to Corvallis.  I sent Lance my resume in February of``
| ``2013 and was hired the following month as a student software developer.  The``
| ``staff was welcoming and the students were amazing and inspirational.  I felt``
| ``like I was right where I needed to be.  I was surprised at how much pleasure``
| ``I took from mentoring so I got involved with Google's Summer of Code program``
| ``which was a great experience.  I even grew so attached to one of my projects``
| ``that I still support it long after it transitioned to another lab.  Yay PGD!``
|
| ``But all good things must come to an end.  After finishing my undergrad work,``
| ``I went on an internship and came back to start graduate school.  I suspected``
| ``then that I wouldn't be able to have my cake and eat it too and that I would``
| ``have to cut back on my commitments once my research got started, and my time``
| ``at the OSL would probably be the first to go.  This suspicion was reinforced``
| ``after my daughter was born last January and again by the financial situation``
| ``about which we all know.  I decided to wait to resign until after the summer``
| ``in case I was needed to help with the transition and now the summer is over.``
|
| ``I want to thank all the students with whom I have worked at the OSL.  You're``
| ``what makes the lab what it is: a finishing school for the finest students at``
| ``Oregon State.  I am proud to have worked with you as you launch your careers``
| ``and I firmly believe that you will continue making the world a better place.``
|
| ``Jack.``


Jonathan Frederick on Packer Templates project at the OSL
--------------------------------------------------------------

1/19/18

.. image:: /images/Packer_logo_smaller.jpg

At the OSL we use Packer to build our images, because of the reproducible and
easy work-flow it allows. We can create an entire operating system image based
off a Linux distribution without any interaction! With this we are looking to
add much more complete and automated testing.

To help with this we have decided to create a Github repository called Packer
Templates. This is what the OSL will be using to generate OpenStack operating
system images that many of our hosted projects use. We have been hard at work
making this a reality for around 2 months and counting, and we still have a lot
of work to do!

In order to get any Linux distribution to install automatically, you have to use
their version of automated installation. They all have different names and syntax,
but generally all follow the same pattern:

1.	Boot the installation image and specify the web addess holding the autoinstallation file through the bootloader
2.	Watch it install! (and hopefully not fail!)

Because we are using packer with QEMU (Virtual Machine software), even step #1
can be automated through VNC, meaning you just run the program and it does
everything for you! One of the major reasons we made this into a Github repository
is so we can take this a step further: automated testing. Each time we make a pull
request with some changes to the installation scripts, we have Jenkins build the
system images, then test them to make sure they work. We don't have to worry about
some change in a script breaking an unrelated system, and we don't introduce bugs
through adding features!



Cody Holliday on Why we should stop using C
-------------------------------------------

07/31/2017

Programming languages are a touchy topic in Computer Science. In certain crowds
even mentioning a language will elicit groans and eye-rolling. Conversely, there
are crowds that will only use certain languages for all projects.

These people have lost sight of the fact that programming languages are tools.
Languages have certain problem sets that they're really good at and some not so  
much. If you were to ask me to do some complex math or signal processing, I would
point you to MATLAB. Would I use MATLAB for developing a GUI? Not in a million years.
So why do we choose C? Well, C is efficient since it's practically one step above
assembly and with a modern compiler it compiles down to a small executable. 
Plus modern compilers have extremely good optimization algorithms that can optimize
your program better than if you wrote it by hand in Assembly. This makes C a great
tool for embedded programming and systems level programming, which is why we have been
using it for so long in these fields! However, a downside (and upside!) of C is that 
it's like assembly. It will let you do whatever you want, even if that means shooting 
yourself in the foot. There is no type safety, there is no memory protection, and no
thread safety built into the language. You have to do all of that yourself with
mutexes, semaphores, and checks. It's good to know about these concepts and be able
to design a system that puts these protections in place, but every project should
not be an exercise in memory management and complex concurrency. We should move on to
tools that help you rather than give you enough rope to hang yourself with.
With computers being as important as they are, security should be our number one 
priority when writing software. If you're writing an application that does an  
unbounded copy from input (ex. heartbleed) in your final release, you just added 
another vector of attack to someone's computer.

We should be writing code that is safe and avoids all sorts of memory issues that
can be solved by using the right tools. Writing C is cool because it's freeing, but 
I think we should move to bigger and better tools that save us from our own stupid
mistakes and hit us over the head with them.

As for embedded programming, there are other options out there that
maybe won't be as small as C, but will make your device more secure.
(Insert plug for Rust here)

Amanda Kelner on Graduating
---------------------------

07/30/2017

As of September 8th, my time here at OSU will officially come to an end. As sad
as I'll be to leave my life here in Corvallis and as nervewracking it is to
enter the real world, I realized recently I've spent the last seventeen years of
my life in school and I'm ready to break free!

I'll be leaving with both a degree in English and in music performance, both of
which have taught me so much not just about their respective fields, but about
growing up and how to work with what you've got.

While I did not have the skills or the privilage to be a student developer or
systems administrator, I feel that my time here at the OSL has been incredibly
valuable. I've learned so much here that I would never have gained from a class.
The challenges I've faced and the experiences I've had taught me diligence,
patience, and flexibility. I firmly believe that my time here at the OSL has
shaped me into a person who is unafraid and excited to leave college.

I'm more than ready to start my new life, but I will miss the friends I've made
and the life I've created here at OSU. The best of luck to my peers and go
beavs!
