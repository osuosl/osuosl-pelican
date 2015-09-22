Helping Drupal Grow
===================
:date: 2009-02-05
:author: OSUOSL Admin
:slug: students/stories/drupal_infrastructure
:slug: blog/drupal_infrastructure
:order: 100

Submitted by OSUOSL Admin on February 5, 2009

When Drupal began to outgrow its infrastructure in the summer of 2005, its
developers appealed to the open source community for help. OSL offered to host
the equipment, and students Eric Searcy and Narayan Newton were put on the case.

"We attacked the problem from two different angles," says Newton, who now works
with Tag1 Consulting and is a member of the association that runs Drupal.
Searcy, now a systems administrator at InsightsNow in Corvallis, dealt with the
scaling of the Web side of Drupal while Newton worked with the database.

They planned several tiers of attack, starting with two load balancers that
became proxies that sent requests to Drupal's servers. It was easy then to know
which server was up or down and to add new nodes quickly. The load balancers
cached Drupal's Web pages, which would deliver older pages without needlessly
taxing the Web server.

Newton and Searcy also added more memory and a second powerful database server.
"At that point things started to stabilize," says Searcy. "Drupal had a huge
growth spurt during that period. Several times we solved things for a week. And
then the demand would rise even higher to exceed the performance gains we'd
made."

In order to balance the needs of the database and front end, Newton and Searcy
would help each other troubleshoot. "We'd have to communicate to find out where
the bottlenecks were," says Newton. "Sometimes, if the Web server was the
bottleneck, the database server wasn't seeing lots of activity and would be
fine. The minute the bottleneck was removed, you'd throw a lot onto the other
person."

Both Searcy and Newton credit the Open Source Lab with providing them with
real-world experience. "The opportunities on the systems administration side of
the Lab for university students are unique," says Newton. "I can't name any
other school that offers the same thing."

**Category:** `Student Stories`_

.. _Student Stories: /students/stories
