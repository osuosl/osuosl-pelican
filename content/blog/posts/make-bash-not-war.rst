Make Bash, Not War
==================
:date: 2014-08-04
:author: Daniel Takamori
:slug: make-bash-not-war
:img: makebash.jpg
:order: 200

At the OSL we have shared workstations, most of which are named after colors. In
the NOC, I usually work at emerald.workstation.osuosl.bak (Figure 1). I use tmux
(Figure \*) to multiplex so I can have multiple terminals open in a single ssh
connection and connect to my session from anywhere. When splitting the terminal
ertically, the prompt can get so long that it's hard to see the command that I'm
entering (Figure 2). I'd like my prompt to automatically shorten itself in
narrow windows. Fortunately, my terminal already knows how much space it has
available: $COLUMNS is an environment variable which stores how wide your
current terminal is, and the default unixism is 80. So in order to save space,
I'd like to shorten my prompt to only a directory listing and a colored
character replacing the normal $ or >. Behold! (Figure 3, 4) Using a case
statement and filtering out the name of the workstation from the domain name, I
can color code my prompt based on hostname. This very easily lets me know
$HOSTNAME (again, this is an environment variable which contains /etc/hostname),
and indirectly /usr/bin/whoami since almost every other user will preface their
prompt with a $USER. This was a 10 minute exercise in learning how to write case
statements in bash and provide some cute utility to an otherwise stale prompt.
The other thing you might notice is that I directly add the unicode heart into
the prompt. This causes difficulty on TTYs and some terminal emulators where it
is replaced with a ♦ (which is an ASCII character). There should be a check to
make sure it can be loaded and replaced with something else if it fails. All in
all, this is just quick hack to make life prettier! `Source!`_

.. image:: /images/bashnotwarscreen.png
    :scale: 100%
    :align: center
    :alt: Bash Not War

.. _Source!: https://gist.github.com/dspt/113418b78abebab76d97
