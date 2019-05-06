Jonathan Frederick on Packer Templates project at the OSL
---------------------------------------------------------
:title: Jonathan Frederick on Packer Templates project at the OSL
:date: 2018-01-19
:author: Jonathan Frederick
:slug: jonathan-frederick-packer
:tags: student-stories

At the OSL we use Packer to build our images, because of the reproducible and easy work-flow it allows. We can create
an entire operating system image based off a Linux distribution without any interaction! With this we are looking to
add much more complete and automated testing.

To help with this we have decided to create a Github repository called Packer Templates. This is what the OSL will be
using to generate OpenStack operating system images that many of our hosted projects use. We have been hard at work
making this a reality for around 2 months and counting, and we still have a lot of work to do!

.. image:: /images/Packer_logo_smaller.jpg
  :align: right
  :alt: Packer Logo

In order to get any Linux distribution to install automatically, you have to use their version of automated
installation. They all have different names and syntax, but generally all follow the same pattern:

1.  Boot the installation image and specify the web address holding the auto installation file through the bootloader
2.  Watch it install! (and hopefully not fail!)

Because we are using packer with QEMU (Virtual Machine software), even step #1 can be automated through VNC, meaning
you just run the program and it does everything for you! One of the major reasons we made this into a Github repository
is so we can take this a step further: automated testing. Each time we make a pull request with some changes to the
installation scripts, we have Jenkins build the system images, then test them to make sure they work. We don't have to
worry about some change in a script breaking an unrelated system, and we don't introduce bugs through adding features!
