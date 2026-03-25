# Variable 
default blue = 0
default red = 0
default yellow = 0
default green = 0

default bryan_score = 0

label start:
    jump act_1

label act_1:
    play music "audio/Opening act + flashback.mp3" volume 1.0
    play sound "audio/Nature sounds.mp3" volume 1.5
    # MUSIC: Opening act + flashback.mp3
    # SFX: birds chirping and rustling leaves / Nature sounds.mp3
    mc "{i}It's a beautiful day outside…{/i}"
    mc "{i}Birds are singing…{/i}"
    mc "{i}Flowers are blooming…{/i}"
    mc "{i}On days like this, so close to the Hanami… Chuds like me should be going on dates with cuties!!!{/i}"
    stop sound
    stop music


    play sound "audio/Thunder   Sound effect.mp3" volume 1.5
    # SFX: dramatic fail sound fx / Thunder Sound effect.mp3
    mc "{i}It was all going so well!{/i}"
    mc "{i}I had everything planned out, but when I finally dared to ask out senpai…{/i}"
    stop sound

    play music "<from 86.0>audio/Opening act + flashback.mp3" loop
    # MUSIC: Opening act + flashback.mp3 (from 1:26)
    # (Insert CGs of Act 1 Japanese Confession Scene)
    play sound "audio/Nature sounds.mp3" volume 1.5
    mc "S-senpai Gian! Please go to the hanami with me! I need you bad!!!"
    stop music
    stop sound



    # SFX: wind rustling romance noises
    # SFX: record stop noise / RECORD DISC SCRATCH.mp3
    play sound "<from 06.0>audio/RECORD DISC SCRATCH.mp3"
    gian "Ew, no."

    mc "*GASP* Wait, why?!"
    play sound "audio/Nature sounds.mp3" volume 1.5

    gian "You think I want to go out with YOU?"
    gian "You are CHOPPED and BROKE, nandayo."
    gian "Even the MC from Rent-a-Girlfriend has more motion than you."
    gian "You'll be lucky if a baddie like me even BLINKS in your direction lol"
    gian "Bye loser LMFAOOOO"
    stop sound
    
    # SFX: wet crying snotty noises
    play music "audio/Opening act + flashback.mp3" volume 1.0
    # MUSIC: continue previous opening music
    mc "..."

    mc "Haiyahh… what the heck should I do now, all those plans wasted."

    # SFX: wet slapping noise
    mc "Ew… What the Freak! Why is it so wet…"

    # SFX: peeling off wet paper
    mc "*Screams* OH HELL NO!-"

    play sound "<from 02.0>audio/Page_turn.mp3" volume 1.0
    # SFX: turning paper around
    mc "-oh wait, what's this? A form to meet your soulmate?"

    mc "Well, I do still want to go to the hanami… and it'd be kinda sad going alone."
    mc "I might as well try!"

    play music "audio/Form_Time.mp3" volume 0.3 
    # MUSIC: form time (loop pls).mp3
    # (Form section!! There are 6 questions in total, and each answer relates to a specific love interest.
    # The character whose answers are chosen most often will be the MC's first date.)
    # Blue = Laeticia, Red = Cassandra, Yellow = Bryan, Green = Viko

    "Q1! What is your love language?"
    menu:
        "Physical touch, quality time":
            $ blue += 1
        "Receiving/giving gifts":
            $ red += 1
        "Acts of Service":
            $ yellow += 1
        "Words of Affirmation":
            $ green += 1

    "Q2! What's your ideal partner like?"
    menu:
        "Mysterious and Eccentric":
            $ blue += 1
        "Strong and Dominant":
            $ red += 1
        "Popular and Flirty":
            $ yellow += 1
        "Submissive and Agreeable":
            $ green += 1

    "Q3! Where would you go for a first date?"
    menu:
        "Haunted house":
            $ blue += 1
        "Fancy dinner":
            $ red += 1
        "Coffee date":
            $ yellow += 1
        "Watch a movie at home!":
            $ green += 1

    "Q4! What is your favorite story genre?"
    menu:
        "Horror/Thriller":
            $ blue += 1
        "Action & Adventure":
            $ red += 1
        "Romance Slice of Life":
            $ yellow += 1
        "Fantasy":
            $ green += 1

    "Q5! You're walking out at night and a 7 foot tall clown is chasing you. Whose arm are you running to?"
    menu:
        "A powerful witch":
            $ blue += 1
        "A muscle mommy":
            $ red += 1
        "Guy":
            $ yellow += 1
        "A Catboy":
            $ green += 1

    # (Still form bg, MC fills in personal info)
    
    mc "Done! (kinda mumbling) Now I just need to fill in my number… and email…"
    stop music
    # SFX: ping!
    play sound "audio/harikitte_ikou_kitasan.mp3"
    mc "....."
    play music "audio/Opening act + flashback.mp3" volume 1.0
    mc "A text already?! It says my soulmate is nearby! I'd better head there quickly."
    stop music

    if blue >= red and blue >= yellow and blue >= green:
        jump act_2_blue
    elif red >= yellow and red >= green:
        jump act_2_red
    elif yellow >= green:
        jump act_2_yellow
    else:
        jump act_2_green

# -------------------------------------------------------
# ACT 2: LAETICIA'S DATE
# -------------------------------------------------------

label act_2_blue:
    play music "audio/Laeticia's date.mp3"
    play sound "audio/Crowd Talking.mp3" loop volume 0.5
    # MUSIC: Laeticia's date.mp3
    # SFX: crowd chattering
    # BG: Bazaar UMN

    mc "My date should be around here… a tarot reader…"
    mc "Looks like there's an open booth!"

    # SFX: Wind chimes
    play sound "audio/shop-bell.mp3"
    mc "{i}OH NO SHES HOT{/i}"

    laeticia "Oho~, another customer I see? Or perhaps, has fate finally brought me a worthy partner in crime?"

    mc "Ah, I'm actually here because we matched on the soulmate form thing."

    laeticia "Oh! I'm glad we got to meet then."
    laeticia "I'm Laeticia. A pleasure to meet you~"

    mc "Thanks. I'm… Emcie…"
    mc "{i}We shook hands on it. Her hands are cold.{/i}"
    mc "{i}The thought of it is ridiculous when she's so hot.{/i}"

    laeticia "Emcie hmm…? You look like someone who has a lot going on than just your looks~"
    laeticia "I LOVE guessing games. Would you like me to do a tarot reading? Free of charge, just for you~"

    mc "Oh… um, sorry, I don't think this whole thing is for me."

    # (Laeticia pouts)
    laeticia "Well, that's unfortunate. People who visit this booth are always so mean~"

    mc "What— that's not what I meant—"

    # (Laeticia dramatic)
    laeticia "What a tragedy~ All that money I spent on these tarot cards could've gone for nirmana supplies… or printing my custom hot and sexy UMN-kun merch…. What a shame~"

    # (Smirks seductively)
    laeticia "If only this cute… adorable Emcie… could help me out~"

    mc "{i}Zooweemama!!!{/i}"
    mc "{i}She tried to kabedon me in the air. SHE'S NOT EVEN CLOSE TO MY FACE!{/i}"
    mc "FINE, I'LL DO IT!"

    # (Laeticia smirks mischievously)
    laeticia "Awesome! Glad I could trigger a reaction from you. You look adorable~, haha!"
    laeticia "Shuffle these cards for me, hmm?"

    # SFX: cards shuffling
    play sound "audio/card-shuffle.mp3"
    laeticia "Let's see who you REALLY are~"

    # (Reveal "3 of Swords") SFX: card swap
    play sound "audio/card-swap.mp3"
    ""
    laeticia "Pfft…. AHAHAHAHAHAHA!"

    mc "(Irritated) What? What's so funny?"

    laeticia "Nothing! Nothing…. *chuckles*"
    play sound "audio/card-swap.mp3"
    ""
    play sound "audio/card-swap.mp3"
    ""
    # (Reveal "Ace of Wands") SFX: card swap
    # (Reveal "Ace of Cups") SFX: card swap
    laeticia "Hmmm… okay… okay…"
    laeticia "In all seriousness, looks like you'll go through whatever disaster you went through. Considering a certain event coming up… you just got rejected, didn't you~? Poor Emcie…"

    laeticia "How did I do?"

    mc "I…"
    mc "{i}I'm both impressed and creeped out.{/i}"

    laeticia "Hehe~ I read you like a book, didn't I?"
    laeticia "Oh! It's almost 5 PM. I should start packing up."
    laeticia "Oh man… I brought so much stuff… It's going to be hard carrying this to my apartment."

    # (MC perking up)
    mc "I'll help carry them all!"

    # (Laeticia shocked)
    laeticia "Really? There's a lot of stuff in my booth, though!"

    # (MC carrying the tower)
    mc "{i}As she cleaned up the booth, I stacked up and scooped all the items into my arms.{/i}"
    mc "{i}This is going great so fa—{/i}"

    # SFX: crash (shake screen)
    play sound "audio/metal-pipe.mp3"
    stop music
    # MUSIC: stops
    mc "…"

    # (Laeticia shocked)
    laeticia "MY NIRMANA! NOOOO! IT'S DUE TOMORROW!"
    laeticia "That took me 2 weeks…"

    # (Open dialogue box asking the audience to apologize loudly)
    menu:
        "I'm so sorry!!":
            pass

    # (Laeticia annoyed)
    laeticia "I DON'T THINK I CAN HEAR YOU!"

    # (Open dialogue box asking the audience to apologize louder!!!!)
    menu:
        "I'M SO SORRY!!!!!!":
            pass

    # (Laeticia trying to keep it together, smiling a bit)
    laeticia "I guess accidents just happen. It's alright…"
    laeticia "I…. Let's just… let's just clean it up…"

    mc "{i}I can't believe I just did that… stupid baka…{/i}"
    mc "{i}With no other words exchanged, we cleaned up the mess I made.{/i}"
    mc "{i}I really… really hope I don't drop it this time…{/i}"

    # BG: Laeticia's apartment
    mc "{i}Damn girl you live like this???{/i}"

    laeticia "I'm so glad you're helping, Emcie. I really needed extra hands on this one."

    mc "I'd be happy to help! What do you need me to do?"

    # (Laeticia mischief)
    laeticia "*smirks* So I've been thinking…"

    # MUSIC: UMN's Awakening.mp3
    play music "audio/UMN's Awakening.mp3"
    # (Laeticia dramatic)
    laeticia "So, you know how UMN is the best university around here?"
    laeticia "Wouldn't it be fantastic if we… could talk to UMN himself?"

    mc "…What—"

    # (Laeticia absolute psycho)
    laeticia "Come on, Emcie, who else would be able to help me recreate my nirmana overnight? Who'd bless me with answering questions that have never been asked before?!"
    laeticia "I NEED THIS, Emcie. Can you help poor little ol' me~?"

    # (MC down BAD)
    mc "…"
    mc "{i}Everything is telling me to run away right now.{/i}"
    mc "{i}But… I'm in too deep.{/i}"
    mc "{i}Summoning THE UMN? I can ask him why the food bazaars left us…{/i}"
    mc "Okie dokie."

    # (Laeticia absolute psycho)
    laeticia "PERFECT! Let's prep for everything!"
    laeticia "So, I found this super old book in our library, tucked under the BI corner sofas…"
    laeticia "It tells us that if two students do a ritual together in unison, UMN will manifest into human form!"
    laeticia "I'll teach you the moves real quick. Watch me, kay?"

    # (Open dialogue box saying to remember her moves, it's 4 consecutive poses)
    menu:
        "Got it!":
            pass

    laeticia "Remember that, alright? We need to do it at the same time! I don't know what'll happen if we fail…"

    # (Open dialogue box saying the ritual will start, and the audience needs to do the poses again in a specific countdown)
    menu:
        "Here goes nothing…":
            pass

    # (CG of smoke in the middle of Lae's room)
    laeticia "I- I think it worked!!"

    # (black screen)
    # (UMN amused)
    umn "*chuckle* Who dares summon me?~"

    # SFX: spotlight turning on
    play sound "audio/spotlight-sound.mp3"
    ""
    # (spotlight)

    # (UMN dramatic, eldritch god ahh)
    umn "In me, students dedicate their work to their country through the Three Pillars of Education! Allowing them to take their steps towards success through MY alma mater…"

    # (CG of UMN doing a dramatic pose under the spotlight)
    umn "I, Universitas Multimedia Nusantara, in flesh and bone, have waited for this day to come!"
    umn "Why have you summoned me here? To learn? I must warn you, knowledge comes with a price…. and that doesn't include SKS."

    # (Laeticia lovestruck)
    laeticia "Oh…. Oh my god…"
    laeticia "Thanks for the help, Emcie… umm… get out of here right now…"

    mc "Uhh what–"

    # (Laeticia lovestruck, rap god)
    laeticia "—GET OUT OF MY APARTMENT! I'LL TEXT YOU LATER, THANKS FOR THE HELP, LOVE YOU, BYE!"

    # SFX: door slam shut
    play sound "audio/door-slamming-sound-effect-no-repeats-or-silence-2016.mp3"
    mc "…"
    mc "{i}Did she just… kick me out…?{/i}"
    mc "{i}I wanna ask UMN questions too…{/i}"

    jump act_3

# -------------------------------------------------------
# ACT 2: CASSANDRA'S DATE
# -------------------------------------------------------

label act_2_red:
    # MUSIC: Cass's date.mp3
    play music "audio/Cass's date.mp3" volume 0.5
    # BG: Front lobby of Episode
    # SFX: hotel lobby music

    mc "Whoa, so.. Fancy? This whole lobby can pay for all 4 years of uni…"

    staff "SHE has been waiting for you.. Better not mess it up."

    mc "{i}Scary….{/i}"

    # (Insert CG of Emcie admiring the elevator top down)
    mc "{i}Even the elevator smells more expensive than my rent tenfold.{/i}"

    # SFX: Elevator ding!!
    play audio "audio/Elevator Ding.mp3"
    ""
    mc "{i}I feel my feet tremble below me, whoever this date is…{/i}"
    mc "{i}Must be involved in either illegal logging or mining….{/i}"
    mc "{i}Or worse..{/i}"
    mc "{i}APBN. (Anggaran Pendapatan dan Belanja Negara){/i}"
    mc "{i}I reached the door and knocked on it twice.{/i}"

    # SFX: Knock knock
    play audio "audio/Knock Knock.mp3"
    # (Insert CG of CHAD CASS opening the door)

    cassandra "Oh well well well… Hello there kitten.."

    mc "H-hello…"
    mc "{i}I feel a lump in my throat, my heart beats unnervingly fast…{/i}"
    mc "{i}I can smell a scent on her, that's so.. Distinct{/i}"
    mc "{i}So… overwhelming{/i}"
    mc "{i}OH NO SHE'S HOT{/i}"

    # (End CG)
    # BG: Hotel room

    mc "I.."

    cassandra "Don't waste your breath."
    cassandra "I need my songbird singing beautiful melodies for me."

    # (Cass whips her hair)
    cassandra "Now.. Shall we indulge?"

    mc "{i}Her strong, muscly, firm arm guides me gently to the couch…{/i}"
    mc "{i}Before I see her{/i}"
    mc "{i}…{/i}"
    mc "{i}…eating s-sushi on the couch..??{/i}"

    cassandra "Entertain me… delicate one…"

    mc "W-wha..?"

    menu:
        "Tell her a joke, you silly goose <3":
            jump cass_joke
        "Squeeze her bicep (feed ego)":
            jump cass_bicep
        "Stare at her lovingly, then at her car keys (flirt)":
            jump cass_flirt

label cass_joke:
    mc "I-if you.. Go around Bundaran HI 2 times… what would it be..?"

    cassandra "What?"

    mc "hi..hi…"

    # SFX: jangkrik noises
    play audio "audio/Cricket Awkward.mp3"
    ""
    cassandra "Do that again and I will make your name disappear from UMN's database."

    mc "So… uh… crazy weather we're having?"

    cassandra "Weather is irrelevant. I control three climate-tech subsidiaries."

    mc "Haha.. cool.. You.. control clouds.."

    cassandra "Precisely."

    mc "Have you.. Thought of ruining a film student's day with it..?"

    cassandra "Hm?"

    mc "You know like, learn their outdoor shooting schedule and make it wet.."
    mc "If you know what I mean…"

    cassandra "Tell me more."

    mc "{i}I then propose a subscription service where film students can buy 'sunlight tokens,' because capitalism always finds a way.{/i}"

    jump cass_date_continues

label cass_bicep:
    mc "{i}She's just sitting there, menacingly.{/i}"
    mc "{i}I wonder what goes on in her head…{/i}"
    mc "{i}Suddenly…{/i}"
    mc "{i}My body moves as if pulled closer just by her dominant aura.{/i}"
    mc "{i}Before my silly brain can react, I give her strong, juicy arm a little squeeze, feeling the firmness of its bulging muscles.{/i}"
    mc "{i}My hand stays there…{/i}"
    mc "{i}For just a little longer…{/i}"

    cassandra "hm?~"

    mc "{i}She pulls me into a soft embrace, with a gaze that can turn me into mush in seconds.{/i}"

    mc "*yelps* S-sorry it's just…"
    mc "Your arms look like it can crush both of my ba- no.. both of UMN's energy efficient buildings.."
    mc "Respectfully…"

    jump cass_date_continues

label cass_flirt:
    # TODO: flirt dialogue TBD
    jump cass_date_continues

label cass_date_continues:
    cassandra "This has been going slow and steady so far, but I'm craving a change of pace."
    cassandra "What do you say?"

    mc "YES! I mean- yes, let's do it!"

    cassandra "Very good kitten."
    cassandra "Now, won't you close your eyes and trust me?"

    mc "{i}I closed my eyes instinctively and felt a blind fold- what the heck is she going to do?!{/i}"
    mc "{i}Am I getting picked up?! She's so strong… I think she's holding me with only her arm.{/i}"

    # SFX: door open
    play audio "audio/Door Open.mp3"
    cassandra "Relax, My sweet. You're always safe with me."

    # SFX: heels clicking, elevator ding
    play audio "audio/Heels.mp3"
    play audio "audio/Elevator Ding.mp3"
    cassandra "My Kitten should never travel in such a dull way like walking."
    cassandra "No… we'll arrive in style."

    # SFX: crowd noise
    play audio "audio/Mall Crowd Ambiance.mp3"
    # (CG silhouette Cass and MC looking at her bodyguards and store staff handing them clothes)

    mc "Is this SMS?? How did we get here so fast?? Heh- Are these clothes?"
    mc "Do you really expect me to try all of that on?"

    cassandra "Of course, Kitten. Unless you're bold enough to resist me… then I'll have no choice but to discipline you."

    mc "I mean, i wouldn't- That's not to say i dont like- oh wow look at those ireallygottagotrythemonnow-"

    # SFX: fast footsteps then curtains closing, photo click
    play audio "audio/running-footsteps-sound-effect-hd.mp3"
    ""
    play audio "audio/photo-click-click.mp3"
    mc "{i}Huh?? Did someone just take a picture?{/i}"
    mc "Uh… Cass… I think someone's watching us."

    cassandra "Watching us? Don't be ridiculous, kitten. The bodyguards will handle it."

    mc "I mean- they're taking pictures. Over there, near the racks. Two guys, with their phones out."
    stop audio 
    cassandra "*scoffs* You shouldn't be bothered by them, they aren't worth your attention. I am."
    cassandra "So, why don't you just pay attention to me."

    # SFX: pushed noise
    play audio "audio/pushing-someone.mp3"
    mc "{i}Dang I really hope it's just me overthinking.{/i}"

    # SFX: curtains slammed open
    play audio "audio/household_curtains_draw_hotel_003"
    stop music
    ""
    # MUSIC: action bgm
    play audio "audio/cass kidnapped!!.mp3"
    mc "*oomph* What the- hey! LET ME GO!! CASS!"
    mc "Cass! Please tell me you saw this…"

    # BG: Cinema (eye blink animation?)
    mc "{i}Agh… Am I tied to a cinema XXI chair? Seriously?{/i}"
    mc "What do you want from me??"

    kidnapper "You were with that brat, Cassandra. That should be reason enough."

    mc "IT'S OUR FIRST DATE???"

    kidnapper "Nothing personal, kid."
    kidnapper "Now, we just need to keep you quiet. Quiet and tortured enough for a ransom."
    kidnapper "You'll understand soon enough. We don't need weapons to break you. Just… this."

    # SFX: projector turning on
    play audio "audio/click-sound-for-gd.mp3"
    # (Video plays)
    mc "Huh."
    mc "…"
    mc "{i}I can feel my brain bleeding out of my ears.{/i}"
    mc "{i}Oh help me Cass…! You're my only hope…!{/i}"

    # SFX: thundering footsteps then BAM
    play audio "audio/heavy-footstep.mp3"
    ""
    play audio "audio/roblox-explosion-sound.mp3"
    # (CG of Cass bursting into the room with explosive background)
    ""
    cassandra "Wassup, baby girl, I'm here to save you."

    mc "Cass!!"

    # (Same CG of Cass but her sprite jumpscares us)
    play audio "audio/heavy-footstep.mp3" volume 1.5
    # SFX: thundering footsteps APPROACHING
    "....."
    stop audio 
    play audio "audio/Thunder   Sound effect.mp3" volume 2.0
    kidnapper "BUSET!!!!!!!!!!!!!!"

    # (Add video of the fight scene)

    stop music fadeout 2.0
    play music "audio/Cass's date.mp3" fadein 2.0
    # MUSIC FADES BACK TO: Cass's date.mp3

    cassandra "Well, that's my cardio for the week…"
    cassandra "Emcie, I'm glad you're safe. Despite the setbacks, I quite enjoyed the time we spent together."
    cassandra "However, it seems our time is up… for now."
    cassandra "Come meet me at SDC, and then I can finally make you mine."

    jump act_3

# -------------------------------------------------------
# ACT 2: BRYAN'S DATE
# -------------------------------------------------------

label act_2_yellow:
    # MUSIC: Bryan's date.mp3
    # SFX: cafe door bell ringing

    mc "My date should be around here… a guy wearing earbuds and drinking matcha…"
    mc "…Well, there's actually only one guy in here."
    mc "{i}He seems pretty busy… and awfully stylish. I wonder what he's reading.{/i}"
    mc "Um, excuse me?"

    bryan "…"

    mc "{i}Maybe he didn't hear me?{/i}"
    mc "{i}…Is that a goddamn labubu on his totebag.{/i}"
    mc "Um… I like your green grape labubu. Is that from the Labubu Exciting Macaron V1 drop in 2023?"

    # (Bryan looks up at MC)
    bryan "Oh- Oh! You were talking to me! Thank you so much, and yeah! This green one was a limited edition."
    bryan "I'm so sorry about that. I was too engrossed in this feminist literature that I didn't hear you. You need something?"

    mc "I'm from the dating form, it said we're a match."
    mc "My name is Emcie. Sorry for startling you."

    bryan "*chuckles* It's alright, I don't mind, especially not when it's someone as cute as you~"
    bryan "I'm Bryan, it's nice to meet you too."
    bryan "I totally didn't expect to go on a date today. Luckily, I stop by this cafe every day to read."
    bryan "Ah, I was actually at a really good part."

    # (Bryan reads a bit more of the book, flaunting the cover)
    # SFX: book being waved around
    bryan "…*coughs*"

    mc "{i}Yes, I can see the cover.{/i}"
    mc "What are you reading?"

    bryan "I got distracted again, sorry. This book is just too good."
    bryan "It's called Nana by Ai Yazawa, it's such a touching story about… *shaky voice* female friendship."
    bryan "Ah! I ordered an extra drink for you, it's my favorite. Here!"
    bryan "I was thinking we could take a walk outside together, since it's almost golden hour."
    bryan "And while we're on that topic… *coughs* …mind if you take some pics for my Insta, babe? It'll only take a sec, promise!"

    mc "Uh… I'll try."

    bryan "*chuckles nervously* Well, if you're unsure, I'll teach you how to do it."

    # SFX: run/walk outside & bell noise / Bell.mp3
    bryan "Alright, here's the spot."

    mc "{i}He meticulously set up the scene, helped me frame his picture, and getting the angle just right.{/i}"
    mc "{i}…It was hard to ignore how his hand lingered on my waist and arms as he carefully positioned the camera.{/i}"

    # SFX: photo click!!
    # (2 bum ass photo results)

    bryan "Ehhhh, wait, maybe we could change the angle?"

    # SFX: photo click!!
    mc "{i}We took a few more photos, but all of them were kind of buttcheeks. He seems a bit frustrated, but smiles anyway.{/i}"

    bryan "*sigh* God, the sun is already in a bad spot!"
    bryan "W-well, thanks anyway for trying. There's always a next time."
    bryan "That reminds me, there's this competition I wanted to compete in today! It'd be nice if we could walk there together."
    bryan "It's an hour away."

    mc "An hour?!"

    bryan "Don't worry. I got a real feel-good playlist for times like this."
    bryan "C'mon, give it a listen."

    mc "{i}He pulled out his phone and carefully tucked my hair behind my ears to slip in the earbud. What I hear next is…{/i}"

    # SFX: Racing into the night by yoasobi plays
    mc "{i}This is going to be a long walk.{/i}"

    # Fade out and in black
    # SFX: crowd cheering / CROWD CHEER.mp3
    # MUSIC: competition bgm

    bryan "Shoot, we're late! Sorry, I gotta get up on the stage right now!"

    host "Alright, ladies and men! It's time for the part you've all been waiting for: our competitive quiz!"
    host "It's simple. All you need to do is answer quickly for the next 4 questions. Today's topic: feminism, of course."

    # UI change / SFX: pop
    mc "{i}Why did the UI change.{/i}"

    # SFX: Kahoot Quiz background sound
    host "Let's begin!"
    host "First question!"
    host "A woman and a man apply for a manual labour job which requires a lot of heavy lifting. The woman can lift 20kg more than the man. Who is more qualified for the job?"

    mc "{i}Bryan is staring at me. Is he asking for help? Maybe I should send a signal…{/i}"

    menu:
        "The man - men are better at all manual labour jobs.":
            host "Incorrect! The correct answer is B."
        "The woman - she is most qualified in this situation.":
            $ bryan_score += 1
            host "Correct!"
        "The woman - women are generally better at most jobs.":
            host "Incorrect! The correct answer is B."
        "Both are equally qualified.":
            host "Incorrect! The correct answer is B."

    host "Second question!"
    host "Who is the most feminist character of all fiction?"

    menu:
        "Shinji Ikari from Evangelion":
            host "Incorrect! The correct answer is D."
        "Denji from Chainsaw Man":
            host "Incorrect! The correct answer is D."
        "Naoya Zenin from Jujutsu Kaisen":
            host "Incorrect! The correct answer is D."
        "Okarun from Dandadan":
            $ bryan_score += 1
            host "Correct!"

    host "Third question!"
    host "You're on a date with a woman, and she orders the deluxe sushi package all by herself without sharing, while you had a single bowl of miso soup. She then tells you she forgot her wallet and asks you to pay. What do you do?"

    menu:
        "Pay, but ask her to pay for the next date.":
            host "Incorrect! The correct answer is B."
        "Thank her for letting you pay for everything.":
            $ bryan_score += 1
            host "Correct!"
        "Create an elaborate dine and dash scheme.":
            host "Incorrect! The correct answer is B."
        "Cause a scene and flee when she's distracted.":
            host "Incorrect! The correct answer is B."

    host "Last question!"
    host "In order, what are the phases of the menstrual cycle?"

    menu:
        "Menstrual, Follicular, Ovulation, Luteal":
            $ bryan_score += 1
            host "Correct!"
        "Menstrual, Ovulation, Follicular, Luteal":
            host "Incorrect! The correct answer is A."
        "Menstrual, Luteal, Ovulation, Follicular":
            host "Incorrect! The correct answer is A."
        "Menstrual, Ovulation, Luteal, Follicular":
            host "Incorrect! The correct answer is A."

    # SFX: drum roll
    host "Our winner with the most points is…"
    if bryan_score >= 3:
        jump bryan_wins
    else:
        jump bryan_loses

label bryan_wins:
    host "Bryan!"
    # SFX: crowd cheering yayaya / CROWD CHEER.mp3

    host "Congratulations, Bryan! Here is your humble prize of [placeholder]. Oh, and your complimentary accessories."

    # SFX: walking down stage
    bryan "Emcie! I won! And just between us, I couldn't have done it without you."
    bryan "To tell the truth, you've been such an amazing date so far, and I think… I'm in love with you."

    mc "{i}I feel like I've only said 6 sentences this entire date, but he's hot, so I'll let it slide.{/i}"

    bryan "*clears throat* I've been thinking about it, and I wanted to give you this."

    # Love pokeball card insert
    bryan "Emcie… This is my proposal."
    bryan "Will you go to the hanami with me?"
    bryan "You don't have to answer today. I'll wait for your answer at SDC if you need time."

    mc "I-"

    bryan "Sorry, I need to go now! I have to learn FLStudio, Bandlab, Reaper, Melodyne and also cover Bakamitai by Yakuza tonight!"
    bryan "See you soon, sweetheart~"

    mc "{i}Damn, didn't even get to say my 7th sentence.{/i}"

    jump act_3

label bryan_loses:
    host "Naoya!"
    # SFX: crowd cheering yayayay / CROWD CHEER.mp3
    # MUSIC: same competition music but quieter

    # (Bryan walks down the stage, dejected)
    bryan "*sigh* Damn it…"

    mc "Hey, don't worry about it. It's just a silly competition. The winner literally got a [placeholder] anyway."

    bryan "{i}I thought I could nail this one bit properly, but I can't even do something as simple as that. I'm a failure.{/i}"

    mc "D-don't say that…"
    mc "Why don't you just be yourself? You don't need to build a personal brand outside of social media. You can just be you."

    bryan "You have a point."
    bryan "Gosh, why does it feel like we're finally having our first conversation? Even though we hung out the entire day…"

    mc "I meannn, you didn't really let me talk."

    bryan "Gosh, you're right."
    bryan "I'm so sorry, Emcie. Maybe we can have a second date?"
    bryan "There's a hanami coming up this week, and I'd love to go with you. I'll try being myself this time, for real."
    bryan "Also, um… this was for you…"

    # Love pokeball card insert
    bryan "You don't need to answer now. I'll wait for your answer at SDC?"

    mc "Yeah, I'll let you know."
    mc "It's getting pretty late, wanna head back? I can show you my playlist instead this time."

    bryan "*chuckles* Gladly!"

    jump act_3

# -------------------------------------------------------
# ACT 2: VIKO'S DATE
# -------------------------------------------------------

label act_2_green:
    # MUSIC: Viko.mp3
    # BG: Grocery store
    # SFX: grocery store ambience (25% volume) / Grocery Store Ambience.mp3

    mc "My date should be around here… a guy named Viko with an ita bag…"
    mc "{i}That's weird. Why would he put his name on an anonymous form?{/i}"
    mc "{i}And why a grocery store?{/i}"

    # (really sad/desperate sobbing, screen shake)
    viko "UUUUUUUUWWWWWAAAAAHHHUUUUUESWGHSJ!!"
    viko "P-please! *sobs* G-give me my chicken!"

    mc "WHAT WAS THAT!!"

    # MUSIC: Tense Moments!.mp3
    # SFX: MC running / 1 PERSON RUNNING.mp3
    # (Viko is holding on to dear life (the chicken), fighting off a seasoned mother)

    mc "{i}That guy looks like he's in trouble!… Wait a sec….{/i}"
    mc "{i}Is THAT my date???????{/i}"

    # (Enci dialogue automatically skips through)
    enci "KIDS THESE DAYS HAVE NO RESPECT FOR YOUR ELDERS"
    enci "YOU WHIPPERSNAPPERS SHOULD BE MUCH KINDER TO THE PEOPLE WHO FOUGHT FOR THIS LUXURY YOU TAKE FOR GRANTED"
    enci "YOUR MOTHER NEVER TAUGHT YOU ANY MANNERS"
    enci "SHAME ON HER AND YOUR ANCESTORS!"

    viko "I'm sorry- r-really! *sob* B-but I grabbed it first…"

    mc "{i}There's no way he can fight her off by himself! I need to do something!{/i}"

    # MUSIC: Viko battle section.mp3 (when UI changes)
    menu:
        "Help your twink":
            jump viko_help
        "Hey where did the employees go?":
            jump viko_employees
        "Nah he got this!":
            jump viko_nah

label viko_help:
    mc "{i}With the grace of a giraffe, I swooped in between the two.{/i}"

    # (That Mercy Overwatch meme but MC standing over the fridges)
    viko "*sobs* Wh-who…? N-n-no i-it's alright I-"

    mc "Shh, it's okay, Viko! No one hurts my date when I'm around!!"

    viko "Eh-! H-how did you know my nam-"

    # UI CHANGE
    # (Announcer/host)
    announcer "A wild Enci appeared!"

    # (Enci dialogue automatically skips through)
    enci "OH YOU CALLED YOUR FRIEND TO GANG UP ON ME TOO HUH??"
    enci "DAMN YOU MISCREANTS MULTIPLYING LIKE FILTH"
    enci "I HAVE YOU KNOW THE STORE MANAGER IS FRIENDS WITH MY SWEET SON"
    enci "I CAN GET YOU BANNED IN SECONDS!"

    mc "You're going down, granny! Let's do this, Viko!"

    viko "Y-yeah! W-wait why does it say she's lvl99-"

    mc "{i}I need to pick the right moves according to her weakness… BUT I HAVE NO IDEA WHAT IT IS{/i}"
    mc "{i}I can't do this alone… Hey, you players!! Could you help me out?{/i}"
    mc "{i}I'm gonna show you a series of moves and you better help me by posing alright!!{/i}"
    mc "Here goes nothing!"

    # (no decisions, just show sprite as is, big obvious 3 second countdown for each)
    menu:
        "Ready? Go!!!":
            pass

    # (Viko always loses)
    # BG: black screen
    # SFX: slapping punching / Fighting.mp3
    mc "{i}That ended terribly. We both got wiped by her sandal move almost immediately.{/i}"

    # RETURN TO MAIN MUSIC
    # BG: Grocery Store
    mc "Ow…Are you okay? Are you hurt anywhere?"

    viko "I don't think so… Thanks- uh I appreciate y-you asking, um…"

    mc "I'm Emcie, and I didn't mean it to get out of hand… We even lost the chicken, I'm sorry, Viko.."

    viko "Nh-no, really, th-thank you Emcie."
    viko "You chose to help me even th-though you knew you'd get in trouble- and hurt too! That was very kind of you…"

    mc "{i}He shyly smiled at me.{/i}"

    viko "Th-this date isn't what I had in mind…"
    viko "B-BUT, I was thinking m-maybe we cou-could uh… eat- erm, get dinner at my pl-place?"
    viko "A-after we get the groceries, of course!!"

    jump viko_grocery_shopping

label viko_employees:
    mc "{i}That's a good question, actually. It's deadly quiet. Where did everyone go? Bingo?{/i}"
    mc "{i}Surely the whole store would've heard her and Viko bickering…?{/i}"

    # SFX: thud / THUD.mp3
    mc "{i}…Are those staff members hiding in the shelves??{/i}"

    mc "Excuse me! Can you please do something about her?"
    mc "Are you letting that defenseless string-bean fight her off all alone??"

    mc "{i}They both nod in tandem, so much for great customer service.{/i}"

    mc "Fine! I'll help him myself."
    mc "Hey lady!"

    viko "W-who…"

    # UI CHANGE
    mc "{i}I need to pick the right moves to help him from here… BUT I HAVE NO IDEA WHAT TO DO{/i}"
    mc "{i}I can't do this alone… Hey, you players!! Could you help me out?{/i}"
    mc "{i}I'm gonna show you a series of moves and you better help me by posing alright!!{/i}"
    mc "Here goes nothing!"

    # (no decisions, just show sprite as is, big obvious 3 second countdown for each)
    menu:
        "Ready? Go!!!":
            pass

    # SFX: Victory! / Victory!.m4a
    # RETURN TO MAIN MUSIC

    viko "We won! Uh…who are you?"

    mc "Oh- sorry! I'm Emcie, we matched from a dating form."
    mc "Your name is Viko, right? It was on the form-"

    viko "Oh… I'm really sorry for making you wait…"

    mc "Not at all, I thought the employees could help but…"

    # (Small cg box of employee giving cpr to the other)
    viko "This date isn't what I had in mind…"
    viko "B-BUT, I was thinking m-maybe, to fix things, we cou-could uh… eat- erm, get dinner at my place?"
    viko "A-after we get the groceries of course!!"

    jump viko_grocery_shopping

label viko_nah:
    mc "{i}Judging from how he's still alive, this is definitely NOT his first rodeo. He can handle her no problem alright.{/i}"
    mc "{i}Right?{/i}"

    # (Black Screen)
    # SFX: cartoonish fight sounds / Cartoon Fight.mp3
    viko "Kyaahh– S-someone, anyone he-help! HELP!!"

    enci "THIS CHICKEN IS MINE!"

    # (Jump cut, Grocery Store)
    mc "Never mind, I should help him."

    # UI CHANGE
    mc "{i}I need to pick the right moves to help him from here… BUT I HAVE NO IDEA WHAT TO DO{/i}"
    mc "{i}I can't do this alone… Hey, you chuds!! Help a MC out will ya?{/i}"
    mc "{i}I'm gonna show you a series of moves and you better help me by posing alright!!{/i}"
    mc "Here goes nothing!"

    # (no decisions, just show sprite as is, big obvious 3 second countdown for each)
    menu:
        "Ready? Go!!!":
            pass

    # BG: Grocery store
    # SFX: Victory! / Victory!.m4a
    # RETURN TO MAIN MUSIC

    # (Enci dialogue automatically skips through)
    enci "GRRR YOU'RE LUCKY SOME DIVINE GOD IS STOPPING ME FROM RIPPING THIS CHICKEN OUT OF YOUR HAND"
    enci "NEXT TIME YOU WONT BE SO LUCKY YOU GODDARN HOODLUM MARK MY WORDS!!"

    mc "{i}The mom walked away, still cursing very loudly. Who cares! We beat her fair and square.{/i}"
    mc "I'm so glad she finally left you alone."

    viko "A-ah! Wh-who are you!?"

    mc "Oh- sorry! I'm Emcie, we matched from a dating form."
    mc "Your name is Viko right? It was on the form-"

    viko "Yeah-! I-i forgot I, uh, put my name there;"
    viko "Sorry for the bad date…"
    viko "This was m-my first time fi-fighting someone- a person, for food."
    viko "Actually, s-speaking of food, I was thinking m-maybe we cou-could uh… eat- erm, get dinner at my place?"
    viko "After we get the groceries, of course!!"

    mc "I'm okay with that! I could help you out too. What do you need?"

    viko "U-uh, let's see.."

    jump viko_grocery_shopping

label viko_grocery_shopping:
    # (Item appears on screen, and it scrolls up for like 2-3 seconds)
    mc "{i}This is gonna take a while.{/i}"

    # (Fade in fade out)
    mc "Ok i'm done with my part…"
    mc "{i}Damn where did my twi- I mean Viko go? No way he already left me behind.{/i}"

    viko "Emcie! Over here!"

    # (Chocolate bar w/ discount tag on it appears)
    viko "I'm s-sorry, this was all I could afford…"

    mc "That's sweet, thank you. We can share this in your apartment later. As a treat~"
    mc "{i}Without wasting any more time, we both head to his apartment hand in hand.{/i}"

    # BG: Apartment
    mc "{i}When we arrived, we immediately unpacked and started cooking. We made his favourite dish,{/i}"

    # (Pic slide up)
    mc "{i}Rosè Broccoli Ramen with Potato Skin Chips.{/i}"

    viko "I really enjoyed today's date… E-emcie."
    viko "BUT- UM! I need to get cha- i mean, get some things from m-my bathroom."

    # SFX: door slam / Door Slam.mp3
    mc "Oookay…?"

    viko "(Muffled) Uh- Emcie? C-can you close your eyes, pl-please?"

    mc "Uh sure?"

    # (Black Screen)
    mc "{i}I can feel the sofa shift with the added weight, is that Viko sitting down?{/i}"

    # SFX: bell / Bell.mp3
    viko "Uhm, y-you can open your eyes now…"

    # (Viko in an age appropriate maid outfit)
    # MUSIC: Viko's Confession.mp3

    mc "Oh. My. God."
    mc "{i}I'm SO glad I stuck around.{/i}"

    viko "I, uhm, do cosplay, and stuff… Maybe you knew- or n-not. I hope you don't mind."
    viko "I wanted to be honest with you and…!"

    # (Now he's handing out a pink envelope with a rose stamp)
    viko "D-d-do you want to go to the Hanami Festival with me–!"
    viko "S-sorry! Not to force you on the spot or anything! Just take this as a reminder…"
    viko "You c-can tell me your answer at SDC!!"

    mc "I-"

    # SFX: door slam
    mc "{i}Before I could get a word in, Viko had already pushed me out of his apartment.{/i}"
    mc "{i}SDC huh? I'll think about it…{/i}"

    jump act_3

# -------------------------------------------------------
# ACT 3: FINAL DATE CHOICE
# -------------------------------------------------------

label act_3:
    # MUSIC: Silence, for now
    # SFX: Heartbeat sounds

    mc "Ooook… Here I am. It's almost time…"
    mc "To pick…. A date."

    # SFX: Short drumroll
    mc "{i}Hopefully… everyone I don't choose is a good sport about it.{/i}"
    mc "{i}I mean- they probably would since I told them they'd be going against each other for my final pick{/i}"
    mc "{i}…{/i}"
    mc "{i}Wait- I DID do that right-{/i}"

    # SFX: All LI VAs bickering
    # MUSIC: Pre-Act 3 bickering.mp3

    laeticia "Emcie! Do you know these people?!"

    cassandra "Explain yourself."

    bryan "Ladies, calm down. I'm sure Emcie here will explain everything. Right, babe?"

    viko "I'm incredibly uncomfortable."

    mc "G-guys…"
    mc "This is genuinely just one crazy coincidence, I swear!"
    mc "I mean, you guys were the ones who invited me out here for my answer!"
    mc "On the exact same day… and at the exact same time…"

    cassandra "…"
    cassandra "Are you serious?"

    viko "I do remember being the one to invite you here…"

    bryan "Yeah, I did the same thing!"

    laeticia "Hah! Well, that doesn't matter."
    laeticia "Emcie, you're going with me, right? You basically already promised me!"

    umn "Yea me too man"

    cassandra "Foolish. Emcie already has reservations with me."
    cassandra "They have proved themselves to be mine."

    viko "H-hey, that's not fair. I also invited them! Don't Emcie get a say in all t-this…"

    bryan "That's right. Emcie should be the one to decide who they want to go with."

    laeticia "So, who are you choosing?"
    cassandra "So, who are you choosing?"
    bryan "So, who are you choosing?"
    viko "So, who are you choosing?"

    menu:
        "Laeticia":
            # cassandra "…" (she's already heading towards a very long limo)
            # bryan "Well, I don't mind, as long as you're happy." (performative)
            # viko "I should've stayed at home…"
            jump act3_choose_laeticia
        "Cassandra":
            jump act3_choose_cassandra
        "Bryan":
            jump act3_choose_bryan
        "Viko":
            jump act3_choose_viko

# -------------------------------------------------------
# ACT 3: REJECTION LINES (called before each ending)
# -------------------------------------------------------

# NOTE TO DEV: trigger the unchosen characters' rejection lines
# before jumping to the chosen route. Suggested approach:
# use a variable to track chosen LI and show others' lines first.

# Rejection lines:
# laeticia "Seriously?! This is totally unfair! Whatever, I'm going."
# laeticia (if UMN summoned) "Seriously?! This is totally unfair! Whatever, let's go UMN-kun."
# cassandra "…" (she's already heading towards a very long limo)
# bryan "Well, I don't mind, as long as you're happy." (performative)
# viko "I should've stayed at home…"

# -------------------------------------------------------
# ACT 3 ENDINGS
# -------------------------------------------------------

label act3_choose_laeticia:
    # (rejection lines for cassandra, bryan, viko here)
    cassandra "…"
    bryan "*sigh* Well, I don't mind, as long as you're happy."
    viko "I should've stayed at home…"

    # MUSIC: Doki Doki Literature Club! OST - Daijoubu!.mp3
    laeticia "YES YES YES!!! Take that, randoms!"
    laeticia "Emcie! I'm so happy!"

    mc "Sorry for all that… I really didn't know how to avoid it."

    laeticia "I'll forgive you this time~ But the next time you try to two-time me, you'll regret it."
    laeticia "I have something sooo fun we can do together tomorrow!"
    laeticia "All you need to know is, bring some snacks!"
    laeticia "See you at 9 tomorrow?"

    mc "I'll look forward to it~~"

    return

label act3_choose_cassandra:
    # (rejection lines for laeticia, bryan, viko here)
    laeticia "Seriously?! This is totally unfair! Whatever, I'm going."
    bryan "*sigh* Well, I don't mind, as long as you're happy."
    viko "I should've stayed at home…"

    # MUSIC: Doki Doki Literature Club! OST - Daijoubu!.mp3
    cassandra "I knew you'd make the right choice."

    mc "Sorry for all that… I really didn't know how to avoid it."
    mc "But anyway, what are we doing tomorrow?"

    cassandra "I already made reservations, naturally."
    cassandra "And trust me, I only reserved the best for you, my sweet."

    mc "{i}She grabs me by my waist tightly, and leans down to whisper something in my ear!{/i}"

    cassandra "I'll show you the time of your life."
    cassandra "I'll pick you up at 9. I already have a hold of your home address."
    cassandra "Wear something pretty for me, won't you?"

    mc "Gulp. Y-yes, maam…"

    return

label act3_choose_bryan:
    # (rejection lines for laeticia, cassandra, viko here)
    laeticia "Seriously?! This is totally unfair! Whatever, I'm going."
    cassandra "…"
    viko "I should've stayed at home…"

    # MUSIC: Doki Doki Literature Club! OST - Daijoubu!.mp3

    # Bryan wins path (performative)
    if bryan_score >= 3:
        bryan "Thank you. I never doubted you for a second."
        bryan "Sorry, guys, you heard them! Haha~"

        mc "Sorry for all that… I really didn't know how to avoid it."
        mc "But anyway, what are we doing tomorrow?"

        bryan "Well~ It's more of a surprise. *chuckle*"
        bryan "Don't worry your pretty little head about it, just make sure to wear something stylish, alright? I'll do the rest."
        bryan "See you tomorrow at 9?"

        mc "I'll see you."

    # Bryan loses path (normal)
    else:
        bryan "W-wait, me? Really? After that mess yesterday?"

        mc "You promised me you'll show me the real you, right?"
        mc "I'm looking forward to it, Bryan."

        bryan "*chuckles* I'm so happy."
        bryan "Thank you so much."
        bryan "Ah, I actually did have something in mind for our date, but I want to keep it as a surprise."
        bryan "Would you be alright meeting me tomorrow at 9?"

        mc "Yeah. I'll see you."

    return

label act3_choose_viko:
    # (rejection lines for laeticia, cassandra, bryan here)
    laeticia "Seriously?! This is totally unfair! Whatever, I'm going."
    cassandra "…"
    bryan "*sigh* Well, I don't mind, as long as you're happy."

    # MUSIC: Doki Doki Literature Club! OST - Daijoubu!.mp3
    viko "OH! Oh my god- Y-you really chose me! I- I'm so happy, wait- let me process this please!!!!"

    mc "Sorry for all that… I really didn't know how to avoid it."

    viko "It's ok, honest! I'm just so relieved you wanted to go with me…"
    viko "Thank you, Emcie."
    viko "O-oh, actually… what do you plan to do at the hanami?"
    viko "I've never really been to one before… Do we, um, picnic?"

    mc "We can do that, but I think I have a better idea."
    mc "{i}I lean closer to him and whisper something into his ear,{/i}"
    mc "{i}He immediately turns red, and looks at me with wide eyes before nodding really frantically.{/i}"

    mc "I'll see you tomorrow at 9 then?"

    viko "Y-YEAH! I- i'll see you! Hehe.."

    return