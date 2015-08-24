Vim Trick FTW!
==============
:date: 2014-06-11
:author: Emily Dunham
:slug: vim-trick-ftw
:img: emilyvim.png

Recently, I learned a useful Vim trick. One of our hosted clients has a Dokuwiki
instance that we help manage, and they were having problems with a lot of spam
user accounts being created. We added a CAPCHA to the wiki to make it less
convenient for new spammers to join, but there were a lot of bad accounts
already existing. By "a lot," I mean there were 112,808 accounts listed in
``users.auth.php``, and only about a dozen real project personnel using the wiki
on a regular basis.

To clean it out, we decided the best course of action would be deleting every
account except those with admin privileges, because most of the real humans were
in the admin group and those who weren't could get the project leader to re-add
their accounts. The benefit of clearing out a hundred thousand spammers would,
in this case, outweigh the inconvenience of manually recreating a couple of real
accounts.

It turns out that DokuWiki's interface isn't set up to bulk delete users based
on group membership -- one really shouldn't get that many spammers in to begin
with, so this is an unusual case. However, I'm not forced to use only the
graphical interface. DokuWiki's configurations are stored in .php files in
``/var/www/wikiname/conf``. Each line in ``users.auth.php`` represents one user
account, and is of the form
``user:MD5password:Real Name:email:groups,comma,separated``.

I was familiar with the Vim command ``:d/pattern/g`` to delete all lines
containing a pattern, but this time I needed to delete all lines that didn't
have 'admin' in them. A little research revealed the command ``:v/pattern/d``,
which deletes all lines except those which match the pattern. Since many of the
spammers (73 out of our 112,808, but still too many to hand-delete each) were
using ``admin@`` email addresses, simply deleting all the lines without 'admin'
in them wasn't good enough. Instead, since I know all the users in the admin
group have their group permissions in the form "admin,user," the command that
removed everyone except the admin users was ``:v/admin,user/d``.

If you're newer to the Bash shell, you may be wondering how I got the specific
numbers of spammers. I made a backup of the users.auth.php file before deleting
users, just in case the client changed their mind. Since DokuWiki had
automatically created a ``users.auth.php.bak``, I created my own backup of the
users.auth with ``cp users.auth.php users.auth.php.bak2``. Now I can look back
at the user list full of spammers and say ``wc -l users.auth.php.bak2`` to count
the lines in it (since there's one account per line) and
``grep admin@ users.auth.php.bak2 | wc -l`` to count how many of the former
users had ``admin@`` email addresses.
