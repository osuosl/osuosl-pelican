Cody Holliday on Why we should stop using C
-------------------------------------------
:title: Cody Holliday on Why we should stop using C
:date: 2017-07-31
:author: Cody Holliday
:slug: cody-holliday-stop-using-c

Programming languages are a touchy topic in Computer Science. In certain crowds even mentioning a language will elicit
groans and eye-rolling. Conversely, there are crowds that will only use certain languages for all projects.

These people have lost sight of the fact that programming languages are tools.  Languages have certain problem sets
that they're really good at and some not so  much. If you were to ask me to do some complex math or signal processing,
I would point you to MATLAB. Would I use MATLAB for developing a GUI? Not in a million years.  So why do we choose C?
Well, C is efficient since it's practically one step above assembly and with a modern compiler it compiles down to a
small executable.  Plus modern compilers have extremely good optimization algorithms that can optimize your program
better than if you wrote it by hand in Assembly. This makes C a great tool for embedded programming and systems level
programming, which is why we have been using it for so long in these fields! However, a downside (and upside!) of C is
that it's like assembly. It will let you do whatever you want, even if that means shooting yourself in the foot. There
is no type safety, there is no memory protection, and no thread safety built into the language. You have to do all of
that yourself with mutexes, semaphores, and checks. It's good to know about these concepts and be able to design a
system that puts these protections in place, but every project should not be an exercise in memory management and
complex concurrency. We should move on to tools that help you rather than give you enough rope to hang yourself with.
With computers being as important as they are, security should be our number one priority when writing software. If
you're writing an application that does an  unbounded copy from input (ex. heartbleed) in your final release, you just
added another vector of attack to someone's computer.

We should be writing code that is safe and avoids all sorts of memory issues that can be solved by using the right
tools. Writing C is cool because it's freeing, but I think we should move to bigger and better tools that save us from
our own stupid mistakes and hit us over the head with them.

As for embedded programming, there are other options out there that maybe won't be as small as C, but will make your
device more secure.  (Insert plug for Rust here)
