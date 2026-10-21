"""PLACEMENT PASS v1 — Claude, 21 Oct 2026.
Concepts from the library placed on the v8.2 chapters, journey stages and map nodes, each with a 'how' line.
Writes: placements-pass-v1.json (docs for the Atlas database) and the markdown report.
Every 'how' starts with 'Claude:' so Santi can tell them from his own.
"""
import json, os, re
here = os.path.dirname(os.path.abspath(__file__))
book = json.load(open(os.path.join(here, 'book.json')))
blocks = {b['id']: b for b in json.load(open(os.path.join(here, 'blocks.json')))}
CH = {c['id']: c for p in book['parts'] for c in p['chapters']}
PARTNO = {p['id']: n for p, n in zip(book['parts'], ['One', 'Two', 'Three'])}
for p in book['parts']:
    for c in p['chapters']: c['part'] = PARTNO[p['id']]
STAGES = {'ordinary': 'The ordinary world', 'call': 'The call', 'refusal': 'The refusal', 'mentor': 'The mentor', 'threshold': 'The threshold', 'tests': 'Tests, allies, enemies', 'approach': 'The inmost cave', 'ordeal': 'The ordeal', 'reward': 'The reward', 'road': 'The road back', 'resurrection': 'Resurrection', 'return': 'The return'}
NODES = {'editing': 'Editing', 'counting': 'The count', 'rightcol': 'The right column', 'review': 'The review', 'pressure': 'Pressure', 'thermostat': 'The thermostat', 'seats': 'The seats', 'building': 'The building', 'compartments': 'Compartments', 'kalder': 'Kalder', 'noor': 'Noor', 'professor': 'The professor', 'beard': 'Beard Man', 'frank': 'Frank'}

P = {
# ---------------- PART ONE
'ch-the-reading-room-the-opening': [
 ('the-roster-who-gets-a-bunk', "The seats are an object the old man shrugs at: 'we leave them findable.' No explanation on page three; the roster is enough."),
 ('every-inquiry-leaves-a-fingerprint', "'You were counted the night you asked.' One line, no mechanism. The mechanism is The payload, four chapters later.")],
'ch-the-funeral': [
 ('yima-loses-his-glory-when-he-lies', "Never on the page here. The small yes is the lie that lets the glory go; keep it as your private north and let the professor's margin say it in The control case."),
 ('no-wall-of-comfort-for-dogs', "Already yours: the drive home, nobody pretends there's a heaven for a dog. Tagged so the epilogue can invert it word for word.")],
'ch-the-good-life': [
 ('hunting-things-old-and-slightly-wrong', "The hobby as a nose: the one branch he checks carefully is books that change between printings. Plant, don't explain."),
 ('the-faucet-safe-facts-steer-a-table', "The faucet shown as a party trick before it becomes a defence. Ana and the dogs are the licensed listeners.")],
'ch-reading-with-a-pen': [
 ('deathbed-visions-of-the-dead', "'The reports rhyme': one documented rhyme in a sentence, not a list. He reads the middle of the book, as always."),
 ('group-souls-and-the-animal-collective', "Beard Man's bucket theory, filed under Beard Man. The book's ending is already in it and nobody notices."),
 ('the-forum-voice-everyone-ignores', "The question typed and deleted. In the machine's terms this is the first thing he almost wrote down.")],
'ch-the-sentence': [
 ('11-tresidder-page-118', "The edit itself. Invented edit on an invented book, per the reality rule. The reader has seen the struck line on page three."),
 ('the-grammar-of-the-edits', "Three edits, one direction: given → arose. He sees the grammar before the meaning, on the kitchen floor, playing fetch."),
 ('penemue-who-taught-writing', "Not here. Noted so the chapter knows what it is the first chapter of: in the oldest text the giving of writing was the crime.")],
'ch-down-house-1860': [
 ('the-record-retractions-nobody-admitted', "The interlude answers 'where else?' in the largest way: the most famous book alive, changed by its own author, who regretted it in a letter you can read. Real words only.")],
'ch-a-round-with-a-stranger': [
 ('how-kalder-gets-close', "He asks about Buddy before he asks James's name. That is the whole method in one beat."),
 ('the-vacuum-cleaner-interviewer', "Kalder's tradecraft is Vallée's vacuum cleaner: ten minutes, no notes, nothing forgotten. The reader should feel charmed too."),
 ('rapport-and-the-hook-point', "James drives home giddy. The hook point is the dozen small connections, and the book never has to name it.")],
'ch-utrecht-1993': [
 ('26-withdrawn-at-the-author-s-request', "This is entry 26 from the inside: the paper filed under instrumentation. Noor identifies it in Leiden."),
 ('entanglement-and-bell-s-theorem', "The two-rooms experiment rhymes with Aspect 1982 without naming it. Keep the paper and the men fictional; the physics it echoes is real.")],
'ch-leave-it': [
 ('seed-standup-in-the-glass-box', "The stand-up. Pieter's visible moment, then the sentence."),
 ('gaslighting-and-the-first-denial', "The first denial, read as a pause. James reads the pause the way he reads everything; he does not yet read what it means."),
 ('writing-is-what-makes-the-count-possible', "The ticket he opens is the act that counts him. Don't say it here; The payload lands it.")],
'ch-the-payload': [
 ('the-payload-is-diffs-not-claims', "Forty kilobytes, two-word reasons, his own line appears the night after he asked. The chapter is the object, not the theory."),
 ('writing-is-what-makes-the-count-possible', "What the job actually counts: people who wrote something down. 'asked (job)'. Nobody reads minds."),
 ('room-641a', "Mark Klein found the NSA splitter by reading wiring documents nobody read. James would know the story and be frightened by it. One line, his, not Frank's.")],
'ch-the-control-case': [
 ('the-record-retractions-nobody-admitted', "He tries to kill his own finding and keeps the negatives: nine books, nothing. The anti-Langdon contract, kept."),
 ('the-black-iron-prison', "The professor's shelf: VALIS, Blindsight, Ubik, a Canticle, a Borges with the science fiction. A pattern of subject, not of edits; a man's conclusions."),
 ('the-professor-s-thin-book', "Two hands, forty-one edits, a library number, a date still to come, Ask."),
 ('yima-loses-his-glory-when-he-lies', "The professor's margin, one line: the oldest story of a man losing his light says the cause was a lie. James lied to Ana about the price this week.")],
'ch-the-week-it-vanished': [
 ('martyr-type-the-professor', "How the professor died: a blue chair, the bin not put out, a polite man in a van. The type, from Beard Man's mouth."),
 ('the-beria-pages', "The job gone from every backup, the book closing up as if nothing had been there. One image in narration, no history lesson.")],
'ch-a-pension-visit-zwolle': [
 ('each-anomaly-gets-its-own-explanation', "Each ending plausible on its own: a man who loved his car and the canal road. The chapter must never say what happened."),
 ('the-little-aunt-s-phone-calls', "The handler's register: kind, domestic, unhurried. Borrows the car, returns it washed.")],
'ch-groningen': [
 ('the-little-aunt-s-phone-calls', "The dealer who telephones is the helper with one small believable reason. James explains to him what the call actually does; the first sheet, before the sheets."),
 ('isolation-makes-one-source-of-truth', "The old man assumes James is from the organisation because for thirty years they were the only ones who ever asked.")],
# ---------------- PART TWO
'ch-deventer-march': [
 ('martyr-type-the-professor', "The same death from the handler's side. He broke his own rule and wrote to the post box; Penemue again, never said."),
 ('the-vacuum-cleaner-interviewer', "Photographs every page while the professor sleeps. 'Better to wait; a body is a fingerprint.'")],
'ch-croton-530-bc': [
 ('group-souls-and-the-animal-collective', "The oldest counter to the bucket theory: a dog with a friend's voice. Pythagoras, real words, nothing added.")],
'ch-frank-s-kitchen': [
 ('phantom-time', "Noise earned by being false: killed on tree rings in minutes."),
 ('events-scheduled-before-the-full-moon', "The full-moon earthquake video. Second kill."),
 ('the-mandela-effect', "Frank's best shot at James: 'Mandela effect for bookworms.' Shared false memory versus a text that really changed. Frank is right about the one and wrong about the other, which is the whole book."),
 ('the-tesla-quote-that-doesn-t-exist', "Frank kills the poster quote in one sentence and James agrees. Agreeing here is what buys James credibility on page 118."),
 ('a-threshold-of-ridicule-for-skeptics', "James's better question: a theory that dies on tree rings doesn't need a documentary, so why is there one? Vallée's point, in James's words, never attributed."),
 ('seed-frank-reads-the-recommendation', "The real 1953 panel text, read in its real words. 'The memo's the table.'")],
'ch-the-math': [
 ('a-daughter-who-kept-a-box', "Els and the folder under the lining paper. The one thing James says on the way out is still a PLACEHOLDER; it should be a question, not a fact."),
 ('the-grammar-of-the-edits', "Preferred Formulations as an object: the style guide is the grammar written down by the people who use it.")],
'ch-the-corporate-day': [
 ('seed-the-vacuum-cleaner-on-the-seventh', "Kalder with a vendor's lanyard, and James honestly glad."),
 ('rushkoff-s-continuity-plan-the-event', "'I sell the bank its continuity.' Rushkoff's billionaires asking how to keep the guards loyal after the Event: Kalder's product, as a joke he tells on himself.")],
'ch-a-car-park': [
 ('seed-kalder-reports-up', "Reporting upward. 'Stopped asking out loud, which is worse.'"),
 ('kalder-is-told-recall-rate', "The voice moves the date because of a verb. The handler is told to find out what the man loves.")],
'ch-leiden': [
 ('seed-noor-and-the-cometa-special', "Noor's kitchen. The photocopy from 2009."),
 ('cometa-s-four-phases-of-contact', "Noor reads the generals' manual, real words only. An admiral and five generals; Frank can't wave it away."),
 ('26-withdrawn-at-the-author-s-request', "She identifies entry 26 as the 1993 paper. The two Utrecht chapters and this one are the same fact seen three times."),
 ('garments-of-light', "A conservator's aside, two lines of dialogue: the oldest lost-light story is a one-letter variant between copies. She would find that funny. James would not.")],
'ch-mexico-city-1994': [
 ('martyr-type-the-vanished', "Facts only. See the report: this chapter contradicts Utrecht 1993, where the same scientist dies in 1995 on a canal road. One of them has to go.")],
'ch-the-drill': [
 ('iron-mountain-the-archive-in-the-mine', "The building has a real cousin: a government archive on top of a records vault in a limestone mine. James could have read about it; one clause in narration."),
 ('classified-building-unclassified-files', "A lanyard, a sandwich, desk forty, and a glass door he isn't badged for. He notes a reference-number format and doesn't connect it."),
 ('the-roster-who-gets-a-bunk', "Pieter is twelve. The reader meets the roster as seating.")],
'ch-the-money': [
 ('mkultra-s-surviving-receipts', "The money is the tell: when the files were burned the invoices survived because accounts filed them. Planted here as James's own thought; Frank says it out loud in Frank, loose."),
 ('the-swiss-company-that-was-the-cia', "Crypto AG: a contract whose own staff built the trap without knowing. The model for seats hidden inside a continuity contract."),
 ('six-and-a-half-thousand-secret-patents', "Kalder, later, on what continuity protects: a published annual number nobody outside can check. 6,543 in 2025.")],
'ch-enjoy-it-while-it-lasts': [
 ('ai-fork-operators-drop-the-blind-spot', "Page 212. The default with the blind spot in it, sold to every company."),
 ('anomalies-pre-classified-as-noise', "A rule that tells the tool never to report jobs exactly like the one he found. His access narrowed by exactly that shape.")],
'ch-a-room-with-a-long-table': [
 ('the-scribe-who-counts-the-excess', "What Bram believes the table is: Enoch's scribe recording the shepherds' excess. He can half-quote it; the reader should feel he is sincere."),
 ('hylic-psychic-pneumatic-people', "The right column in Bram's vocabulary, never James's. The count reads fear, not belief."),
 ('the-blind-king-and-the-shared-title', "Every tier calls itself the top. Need-to-know all the way up, stated in 1951 about a third-century cosmology.")],
'ch-leiden-nine-years-ago': [
 ('reveal-kalder-crossed-and-chose-the-seat', "The reveal that hurts, from his side: twenty minutes of Noor's silence went through him, and he filed it and asked for more names."),
 ('a-seat-cannot-buy-the-unafraid', "The book's hardest fact: he crossed and still chose the seat. Don't soften it.")],
'ch-on-land': [
 ('kalder-s-tell', "The word from the professor's margin, in the pub, mid-toaster story."),
 ('the-keeper-finishes-his-sentence', "The invented book. Kalder nods and knows it. Only a man pretending would."),
 ('the-jokes-stop', "Ana notices before James does.")],
'ch-the-gorilla-mask': [
 ('jack-woolams-in-the-gorilla-mask', "Frank tells the 1943 story. The mask as a method, and as James's own armour."),
 ('the-deleted-post-reposted-improved', "His twelve-year-old persona edited: bloodlines added, the deleted question restored. Eleven people see the correction."),
 ('tartaria-and-the-mud-flood', "The forum crank arrives kindly, with Tartaria. The beautiful wrong theory stands next to James's ugly right one; that is the gorilla."),
 ('his-own-facts-quoted-back-at-him', "Kalder finishes one of James's private lines and says Deventer.")],
'ch-the-promise': [
 ('ana-asks-where-are-you', "The kitchen floor, four in the morning. 'Run where, I've got a Doberman.' Then the other voice: okay.")],
'ch-the-schedule': [
 ('seed-ana-and-the-schedule', "She reads it upside down. 'Companion.'"),
 ('operation-legacy', "'Records moved for conservation' has a real ancestor: Hanslope Park, 8,800 files, decades of 'no such files exist.' One clause, or Noor later.")],
'ch-washington-1953': [
 ('seed-frank-reads-the-recommendation', "Told as a story in a room, real words only. The burden of proof on the sighter, not the explainer."),
 ('make-the-witness-sound-insane', "The people executing it were told a different reason. That is the compartment in its first documented form."),
 ('four-hundred-journalists', "Optional second beat if the room wants a modern echo: Bernstein, 1977. Keep it to one sentence or cut it.")],
'ch-a-street-night': [
 ('each-anomaly-gets-its-own-explanation', "'The old dog is not a problem.' Deniable, plausible, never confirmed. The Keeper POV exception: under 900 words, no name.")],
'ch-the-vet': [
 ('kalder-s-tell', "Noor identifies the man by the heater from a barbecue photo. The thin book is gone and nothing else is touched."),
 ('the-dogs-two-states-misfire', "Buddy on the floor with his legs going at two in the morning; the vet kind and unhurried: not tonight.")],
'ch-leiden-friday': [
 ('isolation-makes-one-source-of-truth', "Her clients, her mother's care-home place, her accounts. One afternoon, a clipboard, a kind voice. She makes him tea again."),
 ('the-humanitarian-front', "Kalder's register with Noor is help. The threat is never made; it is itemised.")],
'ch-a-corridor-sixteen': [
 ('the-defect-how-do-we-know', "'Based on what.' Then: don't. The founding wound, planted in ch. 1 and opened here."),
 ('instructions-for-the-dying-read-aloud', "The nurse says 'a better place.' The Tibetan rite reads instructions at the ear. Nobody did that for his father; the book never says so.")],
'ch-the-night-he-stops-being-afraid': [
 ('the-three-keys', "Sober. No light. No how. He checks the kitchen afterward like a system."),
 ('the-clear-light-at-death', "Know what you are refusing: this is deliberately not the Clear Light. The flatness is the point."),
 ('the-flashes-a-hand-he-almost-knows', "The hand from the funeral is one he has filed all his life. 'Not the first time' lands here."),
 ('entropy-is-the-modern-word-for-lost-ligh', "Under it, never said: fear as the high-entropy state leaving him. If a reader wants the physics they can find it; the chapter stays domestic.")],
'ch-urfa-1994': [
 ('g-bekli-tepe-was-covered-not-abandoned', "A German archaeologist climbs a hill the farmers call Potbelly. Facts only; Tresidder stays fifteen kilometres away and unproved."),
 ('the-vulture-stone-date', "The date moves by six thousand years. Don't take the Vulture Stone reading as fact; it is contested and the chapter doesn't need it.")],
'ch-the-long-table-again': [
 ('reveal-kalder-crossed-and-chose-the-seat', "Bram makes him say how he knows. 'James has hands.' The review comes forward."),
 ('kalder-is-told-recall-rate', "The dog: yes; it was efficient.")],
'ch-twenty-minutes': [
 ('seed-twenty-objects-on-the-table', "Every object on the tablecloth, in order, with what he can't prove labelled. Ana counts six 'I don't know's."),
 ('the-strategy-told-to-ana', "She doesn't believe it and she believes him. She's coming home."),
 ('the-interstellar-visitor', "If Ana needs a present-day handle: a tenured man mocked on every podcast for asking whether a comet might be a probe. She knows it from the news; James doesn't have to.")],
'ch-the-other-ten': [
 ('vall-e-checks-the-trustee-lists', "His method here is Vallée's: public records, trustee lists, the dull check. Three resolved plausibly, four gone quiet."),
 ('the-bankers-who-died-in-2014', "The clustering question turned on real people: are seven quiet addresses a pattern or chance? He is a man who reads counts for a living. No names, ever.")],
'ch-the-band': [
 ('the-thermostat-with-two-halves', "The machine heats as well as cools. Said only by James, as a thermostat, never as anyone's hypothesis."),
 ('edits-that-cluster-after-comfort-peaks', "The grants to nonsense fall in the cold years. The published accounts are the receipt."),
 ('seed-the-band-at-3-a-m', "The lower limit found at three in the morning.")],
'ch-frank-loose': [
 ('only-render-what-is-being-observed', "The two of them talk the big ideas straight for the first time: whether a system can count who's logged in without seeing what they see."),
 ('mkultra-s-surviving-receipts', "'I still don't believe it; I believe the invoice.' Frank can know that the MKUltra receipts survived the burn. It is his kind of fact."),
 ('the-distributed-idea-suppression-complex', "Frank's own word for compartments without conspirators: a wall nobody built. He uses it against James and it fits the organisation better.")],
'ch-leiden-1931': [
 ('seed-two-men-in-a-scriptorium', "The plate. The reader recognises the machine."),
 ('the-edit-goes-in-the-mechanism', "The misprints left in: a clean plate is a confession and a dirty one is just a printer."),
 ('penemue-who-taught-writing', "Never said: the printer's trade is the oldest sin in the professor's oldest book. If the printer owns a Bible it is open somewhere else.")],
'ch-the-reading-room-continued': [
 ('every-uap-acknowledgment-comes-with-a-de', "The hearings as vinegar: every admission bundled with a finding of nothing."),
 ('the-2026-ufo-files', "The bar TV: six batches between May and September, hundreds of files, no conclusion. The heating half of the thermostat, in the reader's own news memory."),
 ('sacred-texts-films-and-suitable-sects', "The old man confirms only the general method: stories were always the tool; each new medium frightened them and then became theirs. COMETA said it in 1999 in those words.")],
# ---------------- PART THREE
'ch-the-dinner': [
 ('calculated-indiscretions', "Kalder's threats in code. 'Is Buddy okay now?' James never told him Buddy was ill."),
 ('the-double-bind', "James answers in his own job's words: paid to detect, not to fix; the slightest doubt gets addressed. The book you said you'd read."),
 ('the-keeper-finishes-his-sentence', "Ana present; nobody says the word.")],
'ch-what-was-on-the-phone': [
 ('the-keepers-and-their-two-tiers', "Handlers by code, next quarter's schedule, seats for four companies."),
 ('clearances-as-grades-of-initiation', "What each helper was told, by tier: honeypot, disaster recovery, conservation, heritage. 'Continuity' against every name.")],
'ch-compartments': [
 ('the-swiss-company-that-was-the-cia', "Compartments made real: a company whose own staff built the trap without knowing. James can name it in one sentence; it is public."),
 ('itek-built-corona-cameras-for-a-front', "The Housed are not told a fact; they are given a task whose shape implies it. The ones who infer get a seat."),
 ('the-blind-king-and-the-shared-title', "Nobody who matters knows anything, so nobody who matters has ever been shown anything. Unless somebody has the paper."),
 ('secrecy-as-helplessness', "Keep the five tiers as the organisation's own chart. What James maps is ragged: files lost, two offices blocking each other. Competent enough to frighten, ragged enough to be real.")],
'ch-the-sheets': [
 ('the-payload-is-diffs-not-claims', "One page per person: what they contributed to, in their own documents, and whether they're on the list. Diffs, not claims."),
 ('sinners-will-alter-the-words', "What the sheets are in Enoch's terms: books given back to the people who did the work. Never quoted; it is the shape."),
 ('who-takes-out-the-garbage', "Aylin, asked what she thinks she's conserving, shows him the visitor book. The best minor character stays in the room.")],
'ch-the-leak': [
 ('isolation-makes-one-source-of-truth', "Pieter from his car: there's a man at my door. Let him in, make him tea, say nothing. The handler's own method turned around.")],
'ch-the-night-before': [
 ('iron-mountain-the-archive-in-the-mine', "The lower floor humming through the glass at midnight. The archive on top of the vault is a real kind of building."),
 ('classified-building-unclassified-files', "Aylin lets him in to copy the visitor book. The horror is that she is cheerful.")],
'ch-monday': [
 ('a-seat-cannot-buy-the-unafraid', "Why they don't kill him, said once, plainly."),
 ('secrets-get-old', "The bank votes the trustees out. Anneke takes the chair. Nothing loud.")],
'ch-the-final-conversation': [
 ('how-films-manufacture-belief', "(1) Soft disclosure was never disclosure: Men in Black, I Origins, the moon, Inception. The old man enjoys this part."),
 ('philip-k-dick-and-the-hernia', "(2) A man handed a true thing and spending his life disproving it."),
 ('the-dead-internet', "(3) The internet, social media, AI as the crown jewel: doubt is cheaper than belief."),
 ('bunkers-built-for-the-restart', "(4) The bunkers are fuel; freezing is meaningless. Promise middle management a seat and they keep the machine running."),
 ('the-tibetan-state-oracle', "(5) The Dalai Lama search confirmed, and the ceremony that makes the real thing unthinkable."),
 ('memory-is-the-power-to-name', "(6) They remember: the one thing they took out of every book and kept."),
 ('campbell-s-recyclable-awareness', "(7) James's callback: remembering was for leaving the cycle, not staying. The old man agrees; they chose to stay."),
 ('origen-and-the-fifth-council', "The old man can cite it with pleasure: an emperor deciding in 553 what Christians may believe about the soul. The oldest signed decision in his trade."),
 ('staged-vampires-and-a-fake-second-coming', "(8) Why the truth can't come out: collapse, killers and savages. Vallée's staged apocalypse as the thing they are protecting us from, in their own telling.")],
'ch-a-market-sunday': [
 ('the-devil-s-trump-card-is-anonymity', "Found because he kept one thing he loved: forty bags like that in the world. Anonymity was his only protection and he spent it on golf clubs.")],
'ch-leave-it-2': [
 ('the-record-retractions-nobody-admitted', "One dull ticket against page 212. The win with a receipt; the reader can name which column it came from."),
 ('vall-e-s-renunciations', "The book he is allowed to publish: claims nothing, names nobody, asks the reader to look. Vallée's own position after thirty years.")],
'ch-epilogue': [
 ('buddy-buried-right', "By the gate, a quarter past two, both of them on the floor. 'He's in a better place; I'll see him soon,' and this time he knows what he means."),
 ('group-souls-and-the-animal-collective', "The bucket theory answered: a loved dog can't be poured back. Beard Man was right about one thing."),
 ('love-as-the-exception-the-system-missed', "Ida at the bottom of the stairs, the way only Buddy did. The thesis line once, last page, and not this one.")],
# ---------------- journey stages
'hj-call': [('the-defect-how-do-we-know', "The call is a question, not an event: 'if it was worth doing here, where else?'")],
'hj-tests': [('the-gorilla-mask', "Thirteen chapters in this stage. The gorilla mask is the stage's engine: every real thread has a clown beside it. See the report on pace.")],
'hj-ordeal': [('the-three-keys', "The ordeal is sober and domestic, four nights on a kitchen floor. No light.")],
'hj-return': [('vall-e-s-renunciations', "The return brings home a book that claims nothing. The elixir is a method, not a secret.")],
# ---------------- map nodes
'mm-editing': [('the-beria-pages', "The edit as a household act: the reader cuts the page out himself."), ('orwell-deleted-from-the-kindles', "Why the machine still bothers with paper: nobody owns a first impression any more.")],
'mm-counting': [('room-641a', "A technician reads the wiring documents and finds the splitter. James's mirror."), ('writing-is-what-makes-the-count-possible', "Nobody reads minds. People write.")],
'mm-rightcol': [('the-scribe-who-counts-the-excess', "The right column has a scriptural ancestor: one hidden witness counting the excess.")],
'mm-review': [('operation-legacy', "'Moved for conservation', in real life, for decades.")],
'mm-thermostat': [('the-thermostat-with-two-halves', "Heating and cooling. The 2026 UFO files, Tartaria and the Mandela effect are the heating half in the reader's own feed."), ('a-threshold-of-ridicule-for-skeptics', "Skeptics are managed as easily as believers.")],
'mm-seats': [('rushkoff-s-continuity-plan-the-event', "The seats are a product, and Rushkoff met the buyers."), ('the-secret-emergency-orders', "Continuity plans nobody may read, at state scale.")],
'mm-building': [('iron-mountain-the-archive-in-the-mine', "An archive on top of a vault is a normal business.")],
'mm-compartments': [('the-swiss-company-that-was-the-cia', "A company whose own staff built the trap."), ('the-blind-king-and-the-shared-title', "Every tier calls itself the top.")],
'mm-kalder': [('the-vacuum-cleaner-interviewer', "Ten minutes, no notes, nothing forgotten; asks about the dog first."), ('a-seat-cannot-buy-the-unafraid', "He crossed and still chose the seat.")],
'mm-noor': [('garments-of-light', "A conservator who knows the lost light is a one-letter variant between copies.")],
'mm-professor': [('penemue-who-taught-writing', "Never publish: the oldest text on his shelf says writing was the crime."), ('yima-loses-his-glory-when-he-lies', "Never lie about the book, even to stay safe.")],
'mm-beard': [('the-tesla-quote-that-doesn-t-exist', "Beard Man owns the poster quote."), ('loosh', "Beard Man can carry the harvest theory; James rejects it as too tidy.")],
'mm-frank': [('the-distributed-idea-suppression-complex', "Frank's word for suppression without conspirators."), ('mkultra-s-surviving-receipts', "'I believe the invoice.'")],
}

def tinfo(t):
    if t in CH: return 'Chapter', CH[t]['title'], 'Part ' + CH[t]['part']
    if t.startswith('hj-'): return 'Journey', STAGES[t[3:]], "Hero's journey"
    if t.startswith('mm-'): return 'Mind map', NODES[t[3:]], 'Mind map'
    raise KeyError(t)

docs, missing = [], []
for t, lst in P.items():
    kind, title, where = tinfo(t)
    for stem, how in lst:
        bid = 'b-' + stem
        if bid not in blocks: missing.append(bid); continue
        docs.append({'id': f'{bid}__{t}', 'data': {'block': bid, 'title': blocks[bid]['title'], 'target': t, 'targetTitle': title, 'targetKind': kind, 'how': 'Claude: ' + how, 'updated': '2026-10-21T18:30:00Z'}})
assert not missing, missing
json.dump(docs, open(os.path.join(here, 'placements-pass-v1.json'), 'w'), ensure_ascii=False, indent=0)
print(len(docs), 'placements')
