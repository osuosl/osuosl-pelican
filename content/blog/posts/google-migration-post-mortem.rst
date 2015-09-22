Google Migration Post-mortem
============================
:date: 2014-07-03
:author: Justin Dugger
:slug: google-migration-post-mortem
:img: Justinblog1_0.gif
:order: 200

OSU administration recently approached the OSL asking us to help migrate their
email archives to Google. Through contacts with other local universities that
had made the switch recently, we discovered that Portland State University had
written and `published`_ an open source Python app to manage the process. In the
name of expedience, we decided to fork that project and use that as our base
from which to `extend`_.

Having had time to reflect, I’d like to share a few lessons from the experience:

#. **Enterprise means customized.** All software comes bundled with biases and
   assumptions; small teams may be better off adapting their organization to fit
   those assumptions, but there exists a threshold beyond which it is easier to
   adjust software to fit the organization's assumptions instead. Despite
   forking a completed application, we found ourselves making several
   customizations and undoing several assumptions made by upstream developers.

   It was constantly tempting to rewrite and generalize the software, but data
   migration in particular is usually only done once, so any benefits from
   investments made into code quality will mainly accrue to those that come
   after us. Instead of aiming for perfection, we settled on good enough to meet
   the client's needs, while leaving the app better off than we found it. We
   formalized Python library dependencies using pip, ported the application to
   the latest Django version, and adopted some Django app organizational
   practices `from Mozilla`_.

#. **Pace your app.** 3rd party APIs, including `Google`_, rate limit requests
   to prevent people like us from accidentally DDoSing their systems... kind of.
   The main limit is one mail per second per inbox. The clever engineer will
   recognize that with tens of thousands of inboxes, we can still push several
   thousand emails to Google per second, so long as the app is parallelized
   wisely.

   The app we selected used a task queue with worker nodes pulling from it.
   Syncing one inbox is a task, so we have n concurrent inbox sync tasks running
   in parallel. This design is simple to scale up/down, and properly divides up
   the work with the API's rate limit in mind. Task queues are a good model, and
   one I've used before for this sort of task, so we left the architecture
   alone.

   It was a good chance to learn about RabbitMQ deployment specifics and
   monitoring tools; unfortunately what I discovered was that most tools are
   instrumented for tasks per second while our application was best measured in
   tasks per hour. This wasn't a huge problem, but it meant that I had to write
   my own instrumentation to estimate how long syncing all users might take, or
   how many extra worker nodes to spin up to meet any given deadline.

#. **Config management FTW.** Especially for one-off apps that you don't expect
   to live long, it can be tempting to set up a VM and get it working, then just
   clone it into production a couple of times. It certainly makes the initial
   deploy simple, but making changes becomes difficult once you discover you
   need to scale up to several dozen worker VMs.

   I think most sysadmins understand that config management works well for high
   scale web environments at Google, Facebook or Amazon. What is lost on many
   sysadmins is how configuration management tools are also useful for
   collaboration. By using configuration management tools that treat the
   infrastructure like code, a new strategy emerges: manage ops like one manages
   devs. You provide them with a number of tools: revision control,
   production/development branches, peer review, etc. From this perspective,
   Chef and Puppet make all kinds of sense. It’s also great at documenting how
   your infrastructure is set up for coworkers.

   Or yourself, six months later:

     “Any software project is a collaborative project. It has at least two
     developers, the original developer and the original developer a few weeks
     or months later when the train of thought has long left the station.”
     --`Peter Hutterer`_

   Until you've tried it, you have no idea how useful it is to be able to run
   git grep on your infrastructure. It’s quite useful to know all the places
   that your infrastructure references a specific server you need to take
   offline, or what the Apache configuration looked like back before you tried
   to integrate LDAP authentication with the SVN repo.

So having learned and applied these lessons, what did we accomplish? By mid
December, roughly half of the student population had opted into the Google apps
domain. This greatly reduced the time spent during the last weekend of December
for the final sync of approximately 24k remaining inboxes. OSU Helpdesk was also
happy with the gradual migration; infrastructure changes implemented all at once
lead to large temporary increases in calls, and makes staffing and scheduling
much harder.

.. _published: https://github.com/sekondus/Goblin/
.. _extend: https://github.com/osuosl/goblin
.. _from Mozilla: http://playdoh.readthedocs.org/en/latest/
.. _Google: https://developers.google.com/admin-sdk/email-migration/v2/limits
.. _Peter Hutterer: http://who-t.blogspot.com/2009/12/on-commit-messages.html
