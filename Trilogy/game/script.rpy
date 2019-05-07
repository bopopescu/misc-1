﻿define quote   = nvl_narrator
define comment = Character("COMMENT") # XXX delete this before launch

define ai    = Character("Akagi Ai")
define aoi   = Character("Tomoe Aoi")
define misa  = Character("Umeji Misa")
define akane = Character("Akane")

label start:
    comment "XXX opening scene: Ai and Aoi are window-shopping on their way home from school, and it begins to rain. They take shelter in an abandoned building, & find that Misa and Akane have done the same. Akane must be introduced to Ai & Aoi."
    comment "XXX Because the rain is not letting up, Akane suggests they spend the time telling scary stories."
    comment "XXX Mimi goes first, with THE LAZARUS POSE"
label lazarus_pose:
    scene black
    quote  "THE LAZARUS POSE"
    quote  "{clear}"
    scene  newspaper
    quote  "February 23, 2025"
    quote  "{clear}"
    quote  "Two weeks ago, when the first manned ship to Mars exploded, even if nation states wanted to cover it up, such a thing would be impossible."
    quote  "The scale and suddenness of this event exposed the the internet cranks' claims of international conspiracy as wishful thinking."
    quote  "Much speculation about the evidence caught on radar and sattelite imagery has occurred, but to my knowledge, I am the only one to directly investigate the black squares.\n"
    quote  "{clear}"
    scene  rocket
    quote  "Let me first reiterate the obvious:"
    quote  "the Heart of Gold was the largest, fastest space vehicle humans have ever built by a large margin, and took a great deal of time and capital."
    quote  "It was one month into the three month trip."
    quote  "The things that intercepted it were of comparable size, and the time from when the squares in Siberia and the Outback first appeared and impact was only twenty minutes."
    quote  "This was not part of the abandoned Soviet Dead Hand interception system; the Soviets could not have built a device this size.\n"
    quote  "{clear}"
    scene  twitter
    quote  "I got lucky: I was on Twitter when the news hit."
    quote  "I immediately booked a red-eye flight to Siberia; after all, the Australian square would be much harder to travel to. I bought every drone for sale in the airport mall.\n"
    quote  "{clear}"
    scene  siberia
    quote  "The Siberian square, like the Australian one, was about a mile across."
    quote  "When it opened, it caused a building above it to collapse."
    quote  "I imposed upon the landlord of this building; luckily, there were no tenants at the time, though the landlord suspects that some squatters may have been lost.\n"
    quote  "{clear}"
    scene  hole
    quote  "With a hole a mile across, it's reasonable to expect quite a bit of depth."
    quote  "The scale of the things launched from here gave me a bit of an estimate: at least 800 feet."
    quote  "I modified the drone firmware so that each drone could act as a signal repeater for the next one in the chain; I also added a ping function as a means of estimating depth, although with slow microcontrollers like those in the drones there's a margin of error of about 2%.\n"
    quote  "{clear}"
    scene  hole2
    quote  "My daisy chain of drones demonstrated that the square quote ed straight down about 200 feet, with some indication of shear stress on the edges for the first 25 feet below the rockhead."
    quote  "After 200 feet, the space opened up: my drone's cameras, radar, and sonar all couldn't find edges."
    quote  "There wasn't much to see, other than a lot of dust."
    quote  "About a hundred feet lower, some debris (presumably from the collapsed buildings) sat atop a blunt cone made of a material that resembles smooth concrete."
    quote  "I had my lead drone land on the cone to get a closer look.\n"
    quote  "{clear}"
    scene  hole3
    quote  "From the perspective of the tip of the cone, I could see a vast grid of similar cones in all directions."
    scene  hole_collapse
    quote  "However, the lead cone (and others) began to move; tremors made the building I was staying in become unstable, and I had to flee."
    quote  "Unfortunately, my recordings were lost when the building collapsed on top of my computer, during the square's closure.\n"
    quote  "{clear}"
    scene  sat
    quote "From public sattelite imagery, it seems that the other square closed during the same two hour window; I suspect that it actually closed simultaneously.\n"
    quote  "{clear}"
    scene  cold_war
    quote  "With regard to the mystery of the squares and the tragic demise of our Martian colonists, it is my position that history has repeated itself."
    quote  "The Soviet dead hand system accidentally recapitulated, in some small way, an antedeluvian drama that once occurred between Earth and Mars, long before the age of man."
    quote  "We have finally reached the level of technological development necessary to become pitted against our forebears, who while not human were also people of Earth."
    quote  "However, their defenses are far beyond what we can reasonably wish to escape."
    quote  "How long will we be trapped on this planet by the nervous twitches of a long-dead race?"
    quote  "The thousands of cyclopean missiles beneath the Siberian tundra are our formidable jailers, along with similar stockpiles who knows where else."
    quote  "We cannot leave the cradle of earth until we outwit them; but, even something as simple as the door mechanism for this defense system is centuries beyond our technology, and the very existence of a race who could build such things is beyond the current reach of our archaeology.\n"
    quote  "{clear}"
    scene  ancient_aliens
    quote "Who were the figures in this ancient drama? We have been presented with a mystery whose clues will be inaccessible for the forseeable future."
    quote  "{clear}"
    comment "XXX various characters comment on the story, and then Akane goes next, with THE HOUSE ON FOULNESS"
label house_on_foulness:
    quote  "THE HOUSE ON FOULNESS"
    quote  "2nd April, 1919"
    quote  "Dearest Mary,"
    quote  "It might seem childish of me to keep writing this diary in the form of letters to you after so many years, but I am still working toward our promise in my own way. Perhaps, by the time I get to Paris, you will already be there — perhaps the streets will no longer be full of dull bureaucrats!"
    quote  "I have taken the position of governess to a pair of children, at an estate on the coast, in a town called Foulness. What a queer name! I shall be travelling there for most of tomorrow. In this way, I squirrel away savings for the trip."
    quote  "3rd April, 1919"
    quote  "My dearest Mary,"
    quote  "Foulness is indeed an appropriate name! The stench of the neighbouring salt marsh pervades this town, and those strange oversized marsh insects buzz in tight circles in every corner of the town. It is uncomfortably hot in the sun and uncomfortably cold in the shade. The people here look wind-beaten."
    quote  "The estate where I will be working is on a small rocky island across the marsh, and a low bridge of stones apparently connects it to the town proper, though this is now covered by the tides. There is no ferry out, and no dock on the other side. I will be taking that bridge in the morning."
    quote  "4th April, 1919"
    quote  "Mary,"
    quote  "At long last, I have arrived at the estate proper — just as the maid was leaving. I presume that the bridge is so low as to be submerged most of the time, and the household is careful to cross in and out of town as close to low tide as possible so as to not be caught out."
    quote  "The stench out here is stronger, and animals and sea life sometimes die on the rocks, lending their own unique spices to the already-thick sea air during the warm parts of the day. As I came up to the stone staircase leading from the low bridge to the main building, I saw the corpse of a gull on a nearby rock, its eyes crawling with maggots. I saw a figure clambering on the rocky piles beyond, running back behind the house."
    quote  "I later determined that this must have been the boy, Terence, who is twelve — that age when boys make sport of poking dead things with sticks. He does not seem abnormally unruly for a boy of twelve. His sister, Anna, is only four but preternaturally calm."
    quote  "I introduced myself to the children — the maid is the only other member of the household staff, and she sleeps in town, and meanwhile, the master of the house is still involved in his work in London — and got to preparing meals for them. Although the kitchen has been cleaned, the pantry is emptied of anything that could be eaten without cooking — I wonder how long the children have been fending for themselves here."
    quote  "5th April, 1919"
    quote  "Dearest Mary,"
    quote  "My bedroom is cold and drafty during the night, and gusts of wind kept me awake late, but when finally I fell asleep I dreamt of good times with you before the war. Paris was not the only foolish youthful promise we made in the woods that summer! I had forgotten all the others. I don't know what prompted all those memories to return."
    quote  "I awoke early, my room's cold and drafty room becoming hot and stale shortly after sunrise, and so I was able to catch the maid, a Mrs Grant, before she left. She informed me that the reason there is no ferry and no dock here is that the tides would smash them against the island — and from the sounds I heard last night, I believe it!"
    quote  "She also told me that Master Marsten had moved to London at the beginning of the war, like your father did. She said that the house was built by some eccentric ancestor — a gentleman-scientist who fancied himself an authority on salt-marsh wildlife (although his works were never accepted by the natural philosophers of the Royal Society and never had any kind of wide circulation). I suppose the seventeenth century had its cranks as well."
    quote  "She indicated that she was grateful that I wasn't like the previous governess, who she held in some low regard. Apparently, that woman was about my age & quickly became close to the children, only to suddenly disappear one day — leaving the children totally alone for some weeks before I could be hired. How irresponsible!"
    quote  "I requested she pick up some groceries — eggs, fresh fruit and vegetables if she can find any, and flour, since the bag left here has been invaded by some unfamiliar marsh-insect. She will bring them tomorrow morning."
    quote  "Other than feeding the children and keeping one eye on their adventures on the rocks, I spent the remainder of the day acquainting myself with the house. It has no basement, but it's larger than it looks from the outside — an octagonal assemblage of rooms piled together like the rock walls it perches on, with a staircase wrapped around the inside of one wall. Most rooms are empty, only storing sheet-draped furniture. In a few places, there were signs of water damage behind and below the radiators; I must remember to ask Mrs Grant about fungicide. One small door set into the wall at the top of the stairway is locked, and I cannot for the life of me imagine where it goes — I will ask about that as well."
    quote  "The children's play is strange — though I imagine it must have been borne out of siblings of such different ages being alone together for so long with nothing to do. Terence scrambles among the rocks with a stick in one hand, while Anna sits and watches, seeming to give him commands. How Terence manages to scramble so all day, in such oppressive heat, is beyond my comprehension. Were we so energetic when we were young?"
    quote  "This must have been the game he was playing when I first came, as well. Had Anna sent him to poke that dead bird? She's such a calm and sweet girl that the notion seems absurd — but still, I cannot shake it. Her calmness remains when she plays this game, but something else — a kind of commanding authority, and not a child's play-act of authority — comes through in her face."
    quote  "After supper, the children and I sat by the little stove in the centre of the ground floor landing and I read them a story. Then, Anna said something strange. She said, \"Mama says she likes you.\" Young children often have vivid imaginations, and so I dismissed it, but her face had that same seriousness."
    quote  "6th April, 1919"
    quote  "When Mrs Grant came (thankfully hauling flour and eggs, although no fruit and only some meagre-looking withered vegetables unsuitable for pickling), I asked her if Anna had been close to her mother. \"Oh dear no,\" she said. \"Mrs Marsten, god rest her soul, died giving birth to Anna, who never knew her mother.\" This lifted a weight from my heart. Anna is not seeing her mother out of trauma — she has no concept of what it's like to have one, and so an imaginary mother is no different from an imaginary aardvark or some other fantastical creature a child might pretend about. Mrs Grant also lifted my spirits with regard to the water damage from the radiators, saying that the house is mostly cedar and gets far worse from the surf — everything dries out in the summer, when it is even hotter during the day than it is now, and the copper roof practically bakes the steam out of the whole house."
    quote  "Terence was even busier at Anna's game today than usual. When the wind was right, I heard her preface her orders with something like \"Mama says\". Perhaps this is not an imaginary friend at all, but merely a part of the game they invented together."
    quote  "The activity, in this heat, must have been too much for Terence. Around sundown, I went to call them in, and only Anna came. I asked where Terence was and she said, \"still on the rocks\". I let him play for a little while longer, but darkness fell quicker than I expected, so I gathered up a lamp & went out to look for him."
    quote  "I found him laid out on one of the stone steps, the water line up to his ears, flushed and warm to the touch, & carried him in. As I did, I thought I saw a light in the small parapet atop the roof."
    quote  "I tended to his fever with cool, damp rags, until Anna told me \"Mama said use the paracetamol\". I did, and his fever broke, though he didn't wake up."
    quote  "April 6th, 1919"
    quote  "Mary,"
    quote  "Last night, below the gusts of wind, the waves against the rocks, and the groans of the shifting house, I thought I heard a soft, clear voice as I fell asleep. While it disturbed me, it didn't keep me awake, and I dreamt of you again. I had forgotten the reason we met in the woods that summer, and how cruelly your father was treating you. I think I was too young to understand the extent of it at that time. I naively thought friendships formed in a vacuum, and that our connection was the result of some shared piece of soul between us, but probably at that time the woods and my companionship were your sanctuary."
    quote  "I checked on Terence, whose temperature was rising only a little, and roused him into a state of half-wakefulness to give him additional paracetamol, after which he lapsed back into slumber. I noticed his skin was a little greasy & that he was beginning to develop pimples on his cheeks. He is an adolescent after all, but I hadn't noticed these things earlier in the week, even when ensuring his face and hands were properly washed for supper."
    quote  "I told Mrs Grant about Anna's strange prescription, and she looked slightly disturbed. She said, \"Anna never called her mother ‘Mama'.\" After all, she had never had a mother. Instead, that had been Anna's pet name for the previous governess, who had come nearly four years ago and stayed until recently. \"Mama Mary.\" I did not say that I had a childhood friend named Mary; it is, after all, a common name!"
    quote  "Mrs Grant will be off on holiday for the next two days, so she stayed a little later than usual to ensure the house was cleaned up. She even helped me a little with the pie I was baking (using a couple rusty cans of fruit that nevertheless smelled edible). She stayed late enough that she had to pick up her skirts to walk back to the mainland! A small part of me wished she had stayed until the tide hit the high water mark on the stone steps, about half a foot above my head, and that she would need to stay the night."
    quote  "After Mrs Grant left, Anna continued ordering me about — \"Mama says fill the bathtub with cold water\", \"Mama says take in all the towels off the line\". I played along."
    quote  "I must have tired myself out, because I found myself dozing before the stove late in the evening, after I would have normally gone to bed. I heard a creaking above me, and a pair of soft voices from the radiator."
    quote  "One was rambling on and on and periodically giving orders, while the other was giving short responses. I identified the one giving short responses as Anna."
    quote  "\"We have always lived here in tune with the cycle of the waves and the cycle of the tides and we have always let them burst into the waters when they are ripe,\" said the rambler. There was a creak and a scraping sound above me. \"You are not of age but you can feel this truth inside you. You must let him ripen and the seeds burst out into the water. Do not be afraid of it. He will burst so that you will not. It is only his blood that is wrong. He cannot become one of us. When he is ripened, let him go.\""
    quote  "The rambler went on and on like this, and I tried to transcribe more, but the more closely I listen to the echoes in the radiator, the sleepier I get. Perhaps I, too, have become feverish and delirious? I will finish this letter and go to bed."
    quote  "April 7th, 1919"
    quote  "Mary,"
    quote  "Late last night, awakened by Terence's cries, I discovered the meaning of Anna's preparations. His fever had gotten worse — far worse — and he was squirming, his muscles spasming. I remembered that the tub was still full of cold water, and being unable to get him to swallow the paracetamol, I carried him there. But, as soon as his torso was submerged, it split open like a pomegranite, white pips floating to the surface. His skin was a thin shell, muscle eaten away and full of small holes, with nothing inside but bones and these squirming white worms that now rushed out. They burbled under the skin on his unsubmerged limbs and face, while the others floated or clung to the edges of the tub."
    quote  "I heard the front door open, and the worms began evacuating his body, pouring out of the tub onto a line of fresh, dry towels laid out on the floor — a pathway to the doorway, where Anna stood in her nightgown in the pouring rain. I watched them march out, down the steps, and into the moonlit marsh clay, which had risen up above the water line. The worms scattered out, created each a tiny hole, and dove in."
    quote  "\"Mama wants you to understand,\" Anna said. \"Mama is mama now, and Mary too, and even Papa's Mama.\" I was too Vaguely Surprised to respond."
    quote  "I climbed up the stairs to my room, and as I slipped into sleep, I heard the radiator calling my name, saying \"remember Paris, remember our promise before the war\"."
    quote  "I was naive to hold on so tightly to a youthful promise. Paris is the domain of the Bluebeard of Gambais now, not some glamorous fantasy land of Byronic heroes and symbolist poets."
    quote  "I took a shovel from the root cellar and destroyed Anna while she slept. Tonight, when the sun sets and your twisted, infected body can move again, I will do the same to you. This is the last letter I will write. In the morning, before Mrs Grant comes, I will take my shovel to London to finish the Marsten dynasty."
    comment "XXX various characters comment on the story, and then Aoi goes last, with SHE AWAITED THE TURKEYS"

label turkeys:
    quote "SHE AWAITED THE TURKEYS"
    quote "The load-bearing wall groaned behind her. She would need to move again soon."
    quote "Houses used to last a lot longer. This was the third in as many weeks, and she had put off leaving for longer than was wise: the previous tenants had left furniture, and she had almost convinced herself that the smell of rotting carrion was actually the nearby sewage treatment facility."
    quote "Taking a claw hammer from the pocket of her mangled overalls, she peeled some of the boards back from the doorjam. Covering her body with a plastic tub, she pushed her way through three or four feet of bloodied feathers and claws. The smell no longer bothered her, but without the tub she would be smothered before she could be crushed, and the tub provided valuable protection from the rain of small winged bodies as she made her way to her next shelter. This area was developed during the last real estate boom, and so almost any house she found would probably be abandoned. She risked a glimpse at the sky, but it was pointless — as usual, the sun was blotted out. For her efforts, she received a white-capped chickadee in the eye."
    quote "When she was young, her parents and friends thought it was a blessing, and treated it like a parlor trick. They'd make jokes about Disney princesses and sing that Carpenters song. It wasn't until she was ten years old that the rate had accelerated to the point of being distressing: her family had to replace the sliding glass doors on the porch with something opaque, and shortly afterward painted the outside of the house a dull rust color to hide the blood. When the roof of that house finally collapsed, they were still in denial, unprepared; only she escaped."
    quote "She had been in this development for a year — or maybe two. It was hard to keep track anymore. The birds kept coming in thicker. She wore rubber rain boots that went up above her knees, tucked into her pants; nevertheless, some songbirds, already mostly rotten, fell inside as she shuffled through some of the taller mounds and became squished between her leg and the outside of the boot, beaks and claws and little bones pressing into her flesh. As she pushed through a front door, she felt an unusually large thump on her tub: a hawk, maybe."
    quote "She pushed the door closed, reinforcing it with boards and nails with a practiced ease. Then, satisfied, she turned around to survey the rest of the building. But, the back end of the house had already collapsed: she must have already stayed here!"
    quote "She heard a banging to her left, and it jogged her memory. This was the place with the wild turkeys."
    quote "She had thought having turkey would be nice — an easy meal. She had underestimated their strength. That time, she had barely escaped. She had been much stronger then — inside for nearly a month."
    quote "Unable to imagine herself summoning the strength to pull out the boards and trudge through another deluge, she slumped, her back against the door. She awaited the turkeys."

label end:
    return
