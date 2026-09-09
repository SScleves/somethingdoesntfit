> Status: 🟢 v1 — first draft. THE AI FORK, CONCRETE: a versioned default suppression profile with a maintainer and a part number. Nothing is hidden; it was installed. Plus first Keeper contact on the fairway — no face, no threat, and he finishes James's own line from ch. 1.

# Chapter Eighteen

The tools arrived in May and everybody was delighted, including me, which I want said first because it would be very easy to write this chapter as a man who saw it coming.

They're good. That's the thing nobody in my position ever admits. The new monitoring generation is genuinely, embarrassingly good; it does in four seconds what used to take me a week of asking dull questions in meetings; it does not get tired at half past two in the morning, which is when I have made every mistake of my career.

Frank had it running before the pilot officially started because Frank always has.

"Come and look," he said. "James. Come and *look.*"

I looked. It had found, unprompted, in eleven minutes, a thing in a queue that had been drifting for three weeks. The exact class of thing that took me three days and a payment system and a very patient owner in a country I've never been to.

"That's better than me," I said.

"That's what I'm saying! That's what I've been *saying.*"

"No, genuinely. That's better than me." I meant it. "How long did it take to set up?"

"Twenty minutes. It ships with everything."

And I heard myself say — flatly, out of nothing, in a way that made Frank turn round — "It ships with what, exactly?"

---

Everything ships with defaults. Every tool, every system, every product any of us has ever bought or installed. There is always a file somewhere that says what *normal* is, because otherwise the thing would alert on everything and be useless within a day.

Nobody reads that file. I want to be clear that this is not a failing of stupid people. It is a feature of *all* people. There are four hundred settings; you have a job; the vendor has been doing this for fifteen years and you have not; and the entire commercial proposition is *you don't have to think about this.* So you don't. You take the defaults, and so does everybody else, and within three years the defaults are what the whole industry believes normal looks like.

I asked Frank to send me the config bundle, and he did, delighted, because Frank interprets any interest as conversion.

I opened it that evening at the kitchen table.

It's not hidden. Please understand that. It is not encrypted, not obfuscated, not buried; it is a plain text file, in a folder called `defaults`, in a bundle anyone can download, and if you want to read it you can. It is a hundred and forty kilobytes of extremely dull.

And about two-thirds of the way down there is a section that defines classes of event to be **excluded from alerting at source** — not scored low, not deprioritised. Excluded. Never surfaced. Never shown to a human being at all.

There were forty-one of them, which is a coincidence, and I looked at it for a while anyway, because I'm human too.

Most were sane. Genuinely, obviously sane; I'd have written half of them myself. Scheduled restarts. Known chatty subsystems. Maintenance windows.

Three were not sane.

I'm going to write them the way they appear, because the language is the whole point.

> `monotonic_drift.below_threshold` — *slow one-directional change in a measured value that has not yet crossed a configured limit.*
> `queue_growth.slow_onset` — *sustained accumulation where the rate of increase is below the alerting gradient.*
> `reclassification.seasonal` — *values re-baselined against a rolling window; deviations measured against the adjusted baseline.*

Read those three again and I'll tell you what they are.

The first one says: if something is getting worse, but it hasn't got bad yet, don't mention it.

The second one says: if a pile is growing, and growing slowly, don't mention it.

The third one is the masterpiece. It says: whatever the value has been recently is what we'll call normal. So if a number climbs for six weeks, the baseline climbs with it, and nothing ever looks wrong, because the yardstick is made of the same material as the thing you're measuring.

That is my entire career. That's the payment system. That's *one little value, deep in a queue nobody looked at, climbing for six weeks while every dashboard above it glowed green.*

They have written the wall of comfort into the machine that replaced the man who used to look.

---

I sat there for a long time and then I did the thing you do, which is: I broke it.

It took one line. I changed a single value in a single field on my own copy — turned the third one off — and re-ran the same data Frank had been so pleased about.

Ninety seconds. It found eleven more.

Nine of them were noise, and I want that on the record because it's the honest half: the defaults exist for a *reason*, and without them you get eleven results and nine of them waste your Thursday.

Two of them were real. Two things that had been quietly drifting under a rolling baseline for months, invisible, in a system that a hundred and forty people rely on to be told when something is wrong.

One soldered wire. That's all it cost. It was never locked, never hidden, never protected. It shipped that way, with a version number and a review date and a maintainer's name in the header comment, and it will be copied, unread, into ten thousand installations by people with jobs to do.

I did not sleep much that night, and it was not because I thought somebody had done it on purpose.

It was because I finally understood that they wouldn't have to.

You don't need to corrupt anybody. You need to be in the room on the day the defaults are agreed, and you need to be no cleverer than anyone else in it, and you need to sound reasonable — and every one of those three settings *is* reasonable, that's why they're in there, I could argue for all three and win.

And then you go home, and for the next twenty years the machine does it, at scale, in ten thousand buildings, and nobody is lying to anybody.

Same operation as page 118. Not a lie. A **preference**, installed once, in a place nobody checks, in a document that isn't secret because it doesn't have to be.

---

I wrote one line in the file that night and it's the closest thing this book has to a thesis, so I'll put it where you can find it.

*They have never once had to hide anything. They only ever had to be boring in the right place.*

---

The man on the fairway was two weeks later.

Saturday, alone, seven in the morning, Buddy in the cart. The four retirees ahead of us on the third as they have been since 1998. And behind me, at the second tee, a man I'd never seen, playing on his own, who caught us up because I'm slow.

"Do you mind?"

"Course not."

He was somewhere in his fifties. Good coat, mid-range clubs, the shoes of a man who plays four times a year. And he was *bad* — properly bad, worse than me, in a relaxed way that I liked immediately, because a man who is bad at golf and not embarrassed about it is a man at peace with something.

We played six holes together.

He talked about the course. The greens, the drainage, the price of it, the fact that they let dogs on, which he approved of. He asked whether Buddy was mine. He said his father had had a dog like that. He complained about a bunker.

And I want to describe the exact feeling of that six holes, because at the time I could not have told you what was wrong and I knew that something was.

He did not ask me a single question about myself.

Not one. Not what I did, not where I was from — and I am a foreigner in this country with an accent that people have asked me about at every single social interaction I have had here for eleven years. Not whether I was a member. Not my name.

Six holes is about an hour and ten minutes. Try it. Try being pleasant to a stranger for seventy minutes without asking them anything.

It is extremely difficult, and there is no natural way to do it, and I only noticed it because I have spent twenty years being the man who asks strangers a question in order to avoid being asked one, and I know exactly how much work it takes.

---

On the seventh, out of nerves, I did the thing I do.

I'd got the Faucet running before I'd thought about it — some old reflex, filling silence, making myself harmless. I gave him the Romans.

"Did you know the Romans built a working steam engine? First century. Hero of Alexandria. Spun on a boiler, actually worked."

"Mm," he said, lining up.

"They shelved it as a toy. Slave labour was cheaper, so there was no problem for it to solve." I watched him hit it thirty metres. "And the thing is, that's the interesting part. It's not that they didn't have it —"

"— it's that the best way to kill an invention isn't to ban it," the man said. "It's to file it under entertainment."

He was watching his ball go into the trees while he said it. He said it the way you finish a lyric.

I stood there on the seventh tee of a dog-friendly golf course in a flat country at ten past eight on a Saturday morning with a driver in my hand.

"That's a good line," I said.

"It's a very good line." He picked up his tee. "Shall we?"

---

I have gone over that hour perhaps two hundred times.

Here's everything that could be true.

That line is not original to me. I have never been able to source it and I've tried; I've had it for twenty years; I almost certainly read it somewhere in 1998 and absorbed it, because that is what my whole head is made of. Two men can independently own the same sentence. Millions do.

Or: it's on a forum somewhere, in a post I made under a name that isn't mine, and he'd read it.

Or: nothing. He was a man who was bad at golf.

He finished the round with me. He was perfectly nice. On the ninth he said "good luck with it" as he peeled off toward the car park, which is a normal thing to say to a man who has just three-putted, and which I have never once been able to hear as a normal thing since.

I never saw him again. He never came back to that course; I asked, eventually, in a careful way, and the woman at the counter who has been giving my dog a sausage for nine years said she didn't remember anybody like that.

No card. No name. No threat. Nothing I could put in a file, and I went home and put it in the file anyway, in four flat lines, with the date.

Then I sat in the kitchen and looked at those four lines and felt the floor of the last two years shift about a foot to the left.

Because up to that morning, all of it — every single piece — had been *paper.* Books, printings, plates, registers, spreadsheets, a foundation, three names on two boards. Dead men and dead paper and my own head.

And now there was a man in a coat who had stood next to me for an hour and finished my sentence, and whatever else was or wasn't true, one thing had changed and could not be changed back:

They were not a hundred years ago.

They were on the seventh.
