This project was originally created by [Brandon Rhodes for SVN & Mercurial](http://bitbucket.org/brandon/uncommitted/src).

I only added Git support which was trivial and changed it to default to using the `walk` method of traversing through the tree structure rather than the `locate` method which didn't work too well on my Mac.

I was looking for a way to [figure out which files needed committing on StackOverflow](http://stackoverflow.com/questions/2765253/git-status-across-multiple-repositories-on-a-mac) and was directed to this project by Ryan Wilcox. (Thanks Ryan!)

**INSTALLATION TIP:**

Open Terminal and type `sudo easy_install uncommitted` from above the directory level (i.e. directory is named `uncommitted`).
Then you can call the file with `uncommitted ~/Sites`

Below is the text from Brandon Rhodes about his vision for `uncommitted` (with changes to indicate the addition of `git`).

``uncommitted`` -- Scan Version Control For Uncommitted Changes
===============================================================

When working on one version controlled project on my hard drive, I often
flip over quickly to another project to make a quick change.  By the end
of the day I have forgotten about that other change and often find it
months later when I enter that repository again.  I needed a way to be
alerted at the end of each day about any uncommitted changes sitting
around on my system.

Thus was born this `uncommitted` script: using either your system
*locate(1)* command or by walking a filesystem tree on its own, it will
find version controlled directories and print a report on the standard
output about any uncommitted changes still sitting on your drive.  By
running it from a *cron(8)* job you can make this notification routine.

Running `uncommitted`
---------------------

By default `uncommitted` uses the *locate(1)* command to scan for
repositories, which means that it can operate quickly even over very
large filesystems like my home directory:

```shell
$ uncommitted ~
```

But you should **be warned:** because the *locate(1)* database is only
updated once a day on most systems, this will miss repositories which
you have created since its last run.  To be absolutely sure to see all
current repositories, you should instead ask `uncommitted` to search the
filesystem tree itself.  To do this on your `devel` directory, for
example, you would type this:

```shell
$ uncommitted -w ~/devel
```

Not only will the output of `-w` always be up-to-date, but it is usually
faster for small directory trees.  The default behavior (which can also
be explicitly requested, with `-l`) is faster when the directory tree
you are searching is very large.

Should you ever want a list of all repositories, and not just those with
uncommitted changes, you can use the `-v` verbose option:

```shell
$ uncommitted -v ~
```

You can always get help by running `uncommitted` without arguments or
with the `-h` or `--help` options.

Supported VCs
-------------

At the moment, `uncommitted` supports:

* `Mercurial`_ (.hg directories)
* `Git`_ (.git directories)
* `Subversion`_ (.svn directories)

It needs to support `Git`_ soon, since that DVCS is in widespread use.
However, I am not familiar enough with Git's output to write a function
for it myself.  When I tried out Git a few minutes ago, its status
messages were crazy, with all sorts of hash characters everywhere; it
looked like it was suffering from an acute lack of confidence, and was
therefore commenting out all of its own output.  Anyway, there is
probably some simple way to make Git report on uncommitted changes, but
I will leave it to a Git fan to figure out how, if they would like to
contribute a patch back.

I would also not be opposed to someone contributing a Bazaar plugin.
But CVS should probably never be supported by `uncommitted` because that
might imply that it is still an acceptable system to be using.

It occurs to me that there might already be some version control
abstraction layer that I should be using for this, rather than figuring
out how to run each version control system myself; a quick search of
PyPI suggests that I take a closer look at the `pyvcs`_ project.  Maybe
that can be a useful direction for the next phase of development!

Changelog
---------

**1.2.1** (2014 Jun 29)

*	*Improvement:* Ladislas updated `README.md` for better readability - http://github.com/tinyladi

**1.2** (2010 May 08)

*	*Feature:* Eapen added Git support - http://eapen.in 
*	*Bug:* Changed a line in the code from "st" to "status" as pointed out by Shaun (shaunsephton) [I had an alias for 'st' before]

**1.1** (2010 April 24)

*	*Bugfix:* changed *locate(1)* command line to use shell wildcards, since
  it does not support regular expressions under MacOS X.

*	*Bugfix:* all repositories were being called "Subversion" repositories.
	*	_Mercurial: http://mercurial.selenic.com/
	*	_Subversion: http://subversion.tigris.org/
	*	_Git: http://git-scm.com/
	*	_pyvcs: http://github.com/alex/pyvcs/blob/master/README.txt
