OSUOSL Website
==============

Now with 100% more [Pelican](https://github.com/getpelican/pelican)!

Developing
----------

To compile the HTML and host it on port 8000, just run the develop.sh script in
the ``scripts/`` directory:

```
$ scripts/develop.sh
```

This will install dependencies and start up an instance of Pelican on port 8000.
To stop the server, run ``make stopserver``. It can then be restarted with
``make devserver``.

This website uses the
[dougfir-pelican-theme](https://github.com/osuosl/dougfir-pelican-theme) on the
[master branch](https://github.com/osuosl/dougfir-pelican-theme/tree/master).
Information on metadata requirements can be found in the theme repo.
