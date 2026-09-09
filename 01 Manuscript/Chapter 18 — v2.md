> Status: 🟢 v2 — fairway half rewritten per HANDOFF §6.18 and ADDENDUM 04. The anonymous no-questions stranger is replaced by DAVE, who asks lots of questions and is genuinely good company. Letrange's moves 1-3 (provoke / apologise / the operational question dressed as warmth). The line-finishing beat moves to ch. 21. Chapter 18.md v1 left untouched.

# Chapter Eighteen

The tools arrived in May and everybody was delighted, including me, which I want said first, because it would be very easy to tell this as a man who saw it coming.

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

Nine of them were noise, and that is the honest half: the defaults exist for a *reason*, and without them you get eleven results and nine of them waste your Thursday.

Two of them were real. Two things that had been quietly drifting under a rolling baseline for months, invisible, in a system that a hundred and forty people rely on to be told when something is wrong.

One soldered wire. That's all it cost. It was never locked, never hidden, never protected. It shipped that way, with a version number and a review date and a maintainer's name in the header comment, and it will be copied, unread, into ten thousand installations by people with jobs to do.

I did not sleep much that night, and it was not because I thought somebody had done it on purpose.

It was because I finally understood that they wouldn't have to.

You don't need to corrupt anybody. You need to be in the room on the day the defaults are agreed, and you need to be no cleverer than anyone else in it, and you need to sound reasonable — and every one of those three settings *is* reasonable, that's why they're in there, I could argue for all three and win.

And then you go home, and for the next twenty years the machine does it, at scale, in ten thousand buildings, and nobody is lying to anybody.

Same operation as page 118. Not a lie. A **preference**, installed once, in a place nobody checks, in a document that isn't secret because it doesn't have to be.

---

I wrote one line in the file that night and it is the nearest thing I have to a thesis, so I will put it where you can find it.

*They have never once had to hide anything. They only ever had to be boring in the right place.*

---


The man on the seventh was two weeks later, and he was the best thing that had happened to me in a year, and I'd like to leave that sentence sitting there on its own for a moment.

---

Saturday, alone. Seven in the morning, Buddy in the cart. Dew, the smell of the cut, the four retirees somewhere up ahead being slow on the third as they have been since 1998.

I was on the second tee when the starter came out in the buggy and did the face they do.

"James. Do you mind? Single, and he's going to catch you anyway."

"Course not."

He was maybe fifty-five. Good coat, mid-range clubs, and the shoes of a man who plays four times a year and buys shoes like a man who plays forty. He came down the path with his hand already out.

"Dave. Sorry about this. I did offer to wait."

"There's nobody behind us."

"There's nobody in front of us either," he said, looking up the empty fairway, "which makes the whole thing feel a bit like a religious observance," and then he teed off and hit it forty metres into a hedge.

He watched it go with his hand still up in the follow-through, holding the pose long past the point of dignity.

"Well," he said. "That's the one I've been working on."

---

I've thought a great deal about why I liked him so fast, and I've narrowed it to three things, and none of them is charm.

The first is that he asked about the dog before he asked about me.

Not politely — properly. He walked over to the cart and let Buddy sniff the back of his hand and said, "How old?" and I said twelve and he said, "That's a good age for a big one," and then, "He walk the front nine?"

"He used to do all eighteen."

"Yeah," Dave said. "They do."

And that was all. He didn't say anything about how they're never with us long enough, or that he'd had one like that, or any of the four sentences that people say and that I have learned to receive with a face. He said *yeah, they do*, and went to look for his ball in a hedge.

The second thing is that he was genuinely, catastrophically bad, and he did not care. I have played with a lot of bad golfers. I am a bad golfer. Bad golfers are, as a class, the most tightly wound men in any leisure activity on earth, and every one of them has a paragraph ready about their back, or their new grip, or how they don't get out much. Dave lost three balls in five holes and each time made a small sound of pure delight, like a man watching somebody else's car get a parking ticket.

The third thing is that on the sixth he holed a chip from thirty metres, off a downslope, out of wet rough, and it went in like it had an appointment, and he turned around with his arms out and said, "Now *that's* going to keep me coming back here for another eleven years, and it's the only one I'll hit all season, and I'd like you to know it's ruined my life."

I laughed so hard I had to sit down on the cart.

---

Then, on the seventh, he was rude to me, and that's the bit I want to be exact about, because it's the bit that worked.

We were walking and he said, "Can I ask you something without you thinking I'm being funny?"

"Go on."

"Why do you play on your own?"

"I like it."

"No, but —" he did a thing with the club, gesturing at the whole empty morning — "you're not a hermit. You've been perfectly good company for an hour and a half. You know the starter's name, you know the woman in the shop, you knew the four blokes ahead of us well enough to complain about them by name. You're not antisocial. You're just *alone*." He shrugged. "So it's a choice. I'm nosy about choices."

"Four hours where nobody wants anything from me."

"Right," he said, "but that's what people say about prison as well," and he walked on ahead to hit his second.

I stood there on the fairway with my hand on my club and felt the top of my ears go hot, which they have not done since I was about twenty-six.

He waited for me at the green. And before I could get anything out he said:

"That was out of order. I've known you an hour. I do that — I get comfortable and I say the thing, and it's a bad habit and I'm too old to be surprised by it." He looked genuinely annoyed, at himself, not at me. "Ignore me. Your putt."

I want you to notice what that did, because I noticed nothing at the time.

I didn't like him because he was charming. I liked him because he'd insulted me and then apologised so cleanly that I ended up wanting to reassure *him*. Ninety seconds after he'd said the rudest thing anybody had said to me in a decade, I was telling a stranger on a green about my marriage.

Not much of it. But some.

---

He asked one other question that morning, on the ninth, walking in.

"Does she come out with you? The wife?"

"Saturdays. Used to. She gets to about the sixth and then she's had enough of it."

"And now?"

"Now it's mostly me and him." I nodded at the cart.

"Mm," Dave said. He was cleaning a club with a towel, taking his time about it. "Anyone else? Family, mates, the blokes from work?"

"Not really."

"Right," he said, and put the club away, and that was that, and we went and had a coffee at the turn and the woman at the counter gave Buddy a sausage and Dave said "you've got a *system* here," delighted, like a man discovering a small good country.

I did not hear that question. I want that on the record. I have replayed it eleven hundred times and I did not hear it, because it was the ninth hole and I was warm and somebody had asked me about my life.

---

We shook hands in the car park. He said he was in the country a fair bit for work — asset stuff, boring, don't ask — and that he'd probably be back in a couple of weeks if the weather held, and that he'd hate to think of the seventh going unpunished.

"Bring the dog," he said, getting into his car. "He's better company than either of us."

I drove home along the ring road with a bad round and a wet dog and the window down.

And about two kilometres from the house I noticed something and it stopped me at a set of lights.

I was in a good mood.

Not relieved, not distracted, not the flat grey neutrality I'd been calling *fine* since roughly the previous March. A plain, uncomplicated, ordinary good mood, the kind I used to have all the time and had not had once since a woman in a national library told me a scan was safe.

I remember thinking, at those lights, with the indicator going: *that was nice. That was just nice.*

Then the lights changed and I drove home and told Ana I'd played with a bloke called Dave, and she said, "You made a *friend*?" with a delight that I found faintly insulting, and I said he was terrible at golf, and she said "so it's a fair match," and Mora ate something in the garden she shouldn't have, and that was the day.
