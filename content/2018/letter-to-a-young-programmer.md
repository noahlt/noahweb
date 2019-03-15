---
title: Letter to a Young Programmer
date: 2018-09-12
loc: Ingleside, San Francisco
desc: A playwright friend of mine started learning to write code, so I wrote a letter to explain my own attitude towards programming.
---

Dear M,

I was happy to hear that you recently took an introductory course in computer programming. Whether or not you decide to make a career change into software engineering, programming is a singular experience which has brought me great joy over the years, and I hope it will do the same for you.

Let me tell you about two oft-overlooked aspects of programming that I enjoy, in the hopes that they might be useful to you as you study the subject. Ignore the jaded engineers who complain about their jobs; naturally, programming in the real world is just as fraught with annoying frustrations as actually producing a play, but in the end I think it is worth it, and I hope that this note will give you a taste of what I find enjoyable and worthwhile in programming.

## Programming as writing: “ideas about methodology”

I believe that programming has more in common with writing than with math. I'm largely inspired by Structure and Interpretation of Computer Programs (SICP), the old MIT introductory computer science textbook, whose preface says:

> We want to establish the idea that a computer language is not just a way of getting a computer to perform operations but rather that it is a novel formal medium for expressing ideas about methodology. Thus, programs must be written for people to read, and only incidentally for machines to execute.

Only incidentally for machines to execute! What a spectacularly romantic perspective. To understand what exactly they mean, it helps to understand their term “ideas about methodology”.

Elsewhere, SICP describes two kinds of knowledge, declarative knowledge and imperative knowledge. Declarative knowledge consists of facts, assertions, and descriptions of the world; it is the stuff of science and history. Imperative knowledge, in contrast, consists of steps and instructions which describe how to do something; its subject matter is the methodology which programs describe.

Consider the notion of squaring a number. Mathematical notation provides a concise way to describe the result of squaring something: n<sup>2</sup> = n × n. But there are many ways to calculate this! You can multiply n by itself, of course. If you don't know how to multiply, you could add n repeatedly. Or you could arrange a square grid of dots and count the dots. Each of these methods produces the correct answer. In writing a program, we precisely describe each method, which in turn allows us to consider which method might be preferable in any given situation.

If a program communicates a methodology, the same way a play communicates a dramatic arc, then part of the work in programming is to communicate clearly. Just as two screenplays might have the same core idea, yet, in the details, impress the drama upon the audience with varying success, two programs might describe the same methodology but be more or less easily understandable.

The SICP authors continue:

> Our goal is that students who complete this subject should have a good feel for the elements of style and the aesthetics of programming.

What are the aesthetics of programming? Well-written programs have a kind of harmony to them, a cohesiveness, where things flow together naturally and work together well. This sense is difficult to convey to someone who has not read very much code, but of course the SICP authors note feeling these aesthetics as a “goal” for students who complete the subject, and I look forward to the near future when you have such a sense yourself.

## Programming as a practitioner: “product-minded”

That being said, as a practitioner, I obviously do not fully endorse the SICP assertion that programs “should be written only incidentally for machines to execute”. If I did, I would probably be a computer science professor, like the authors. No, my more fundamental drive has always been around what we could do with computers.

With that in mind, I am glad that your course is giving you the project of producing a game, where you can exercise your narrative skill. And I'm sure as you proceed through the course you will see how you might write programs that are helpful at your day job. But I suggest that you also keep your mind open to ideas about how you might write programs that are useful for yourself. Perhaps you might make one to count word frequencies in your prose (as I did last night), or track some of your personal finances, or help you capture and give structure to your ideas when you're brainstorming (another recent project of mine).

I am personally most motivated by ideas of how computation can improve my own life. The more you program, the easier it is to imagine ways in which computers can improve your life — which, in my case, has encouraged me to do more programming. In Silicon Valley people describe this sort of motivation as being “product-minded”, and this motivation has pulled me through lots of otherwise-frustrating programming tasks.

Even if you don't end up programming professionally, I hope that a bit of experience programming will give you a broader imagination about what computers could do for you and the people around you. The science-fiction author Bruce Sterling once wrote, on the experience of carrying a multitool in daily life:

> A multitool changes your perceptions of the world. Since you lack your previous untooled learned-helplessness, you will slowly find yourself becoming more capable and more observant. If you have pocket-scissors, you will notice loose threads; if you have a small knife you will notice bad packaging; if you have a file you will notice flashing, metallic burrs, and bad joinery. If you have tweezers you can help injured children, while if you have a pen, you will take notes. Tools in your space, saving your time. A multitool is a design education.

That same kind of change in perspective happens once you acquire some competency in computer programming. You notice not only all the normal complaints about user interfaces, but also you begin to see ways in which the programmers of the applications you use have been lazy, and become better at imagining ways in which the software you use could be better.

At a recent conference, the programming language designer Simon Peyton-Jones presented a slide which read:

> Why computing for every child?
>
> Reason 1: So that our young people understand, and have agency in, the world that surrounds them.
>
> - Create as well as consume
> - Understand as well as use
> - Technology not magic

Computers should be empowering, not constraining. Contemporary computing tends to follow the arrangement of users receiving fully-formed applications. At best, this model subjects you to the whims of a distant programmer who had their own reasons for writing a program. Unfortunately, the companies that fund most programming work have their own incentives, such as collecting more data for advertising, or to train an AI model, which may not be aligned with your goals.

Being able to write programs yourself will help you see the ever-growing digital part of the world with a critical eye, not take it for granted, and demand more from it — perhaps even enough to produce an application yourself. The Internet entrepreneur David Heinemeier Hansson recounts how, after struggling to learn programming for many years, he finally made progress:

> What made it click for me was programming in anger. Programming because I needed to. Programming because I gave a damn about what I was writing and I wanted it done sooner rather than later.

When you have an idea for how you want to change the world around you, and you can’t get it out of your head, and the only thing to do about it is to actually produce the program — that kind of imagination is what pulls me along to develop software.

## The opposite: programming as math, or puzzles

I guess I write all this in order to give you two counterpoints to the perspective that programming is math, or a series of puzzles to be solved. One stark example of this attitude comes from a review of Shenzhen I/O, a game about programming:

> It distills programming down to the fun parts, removing the inertia, self-inflicted complexity, overhead, uncertainty and drag of real programming. It’s just about coming up with clever tiny algorithms and micro-optimizing the heck out of them.

While this attitude is widespread, and is a fine motivation for those to whom it is motivating, I want to make sure you aren't stuck with that mindset, because it's not the only way to enjoy programming. I am not exceptionally good at math or puzzles, I probably never will be, and you probably are not either, but that should not stop either of us from programming. In this subject, as with all others, we must discover which aspect of it calls to each of us, rather than chaining ourselves to others’ ideas and expectations.

I hope that all of this provides a helpful perspective on programming, or, at least, is mildly interesting. Perhaps soon we will be chatting about the finer points of programming style.

Your friend,

Noah
