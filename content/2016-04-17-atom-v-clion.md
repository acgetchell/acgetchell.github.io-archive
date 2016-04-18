Title: Atom vs. CLion
Date: 2016-04-17
Category: Programming
Tags: c++

Today I decided to give [CLion][1] a try. I need all the help I can get.

[Atom][2] is very nice, and I've been using it since 0.1 for everything from
$\LaTeX$ing papers to writing this blog to everyday coding in C++. However, my
latest travails involve heavy use of the [debugger][3], and doing that on the
command line is not so nice. So I was lured in with the promise of a nice,
graphical debugger in an honest IDE.

After tinkering around with it for an hour or so, and trawling through the
forums, I've managed to get CLion to look very close to my Atom setup. Except
for the different colors used in syntax highlighting, but I'll get used to that,
or I can always customize the color scheme to Atom's material syntax if it
really bothers me.

So, here are the Pros and Cons.

Pros:

- Code completion is nice
- Refactoring is wonderful
- It's really nice to be working with a tool that understands the C++
constructs, instead of just doing some clever pattern matching

Cons:

- No option to use [Ninja][4] as my build tool. This increases build times
perceptibly
- Inexplicably builds in some hidden directory instead of the output directory
(but see the [roadmap for 2016.2][5])
- The debugger skips right past my set breakpoints

Sadly, that last one is pretty much a dealbreaker.

I've submitted a support request, and I really think that CLion 2016.2 looks
very promising.

But as of now I'll still be writing in Atom.






[1]: https://www.jetbrains.com/clion/
[2]: https://atom.io
[3]: http://lldb.llvm.org
[4]: https://ninja-build.org
[5]: https://blog.jetbrains.com/clion/2016/03/clion-2016-2-roadmap/