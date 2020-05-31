import discord
import pickle
import os.path
import os

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from random import randrange

#author sanjana cheerla
#code is RAW and uncommented, commenting and cleaning up will be done asap
client = discord.Client(status='Beep Boop')

globals()
AP_CONSTANT = 0
CREDS = None
RANDOMCONSTANTWORKS = -1
RANDOMCONSTANTHAPPY = -1
RANDOMCONSTANTSTAB = -1
RANDOMCONSTANTGOPACK = -1
RANDOMCONSTANTSAD = -1
RANDOMCONSTANTBEAR = -1
RANDOMCONSTANTSMUG = -1
RANDOMCONSTANTHAIRFLIP = -1
RANDOMCONSTANTEGIRL = -1
RANDOMCONSTANTVSCO = -1
RANDOMCONSTANTSLAP = -1
RANDOMCONSTANTPUNCH = -1
RANDOMCONSTANTKICK = -1
RANDOMCONSTANTHUG = -1

RANDOMCONSTANTWORD = -1

userTags = {}
apClasses = {}
apValues = {}
driveFiles = {}
toDoListDict = {}
wordsDict = {}
foodDict = {}

IT_WORKS_GIFS = [
    "https://tenor.com/view/it-really-works-sure-certain-reassuring-confirmed-gif-13066289",
    "https://tenor.com/view/the-king-of-random-success-it-works-gif-10215889",
    "https://tenor.com/view/squidward-school-work-insane-paper-works-gif-16822622",
    "https://tenor.com/view/mushu-mushu-clan-it-works-yey-happy-gif-16206528",
    "https://tenor.com/view/its-working-star-wars-anakin-anakin-skywalker-gif-5187168",
    "https://tenor.com/view/anchorman-brian-fantana-legend-of-john-burgundy-works-everytime-gif-3448658",
    "https://tenor.com/view/oh-it-works-kassandra-lee-there-it-is-there-you-go-weak-signal-gif-17041540",
    "https://tenor.com/view/simon-gurren-lagann-happy-it-works-gif-14033391",
    "https://tenor.com/view/nailed-it-gif-4232668",
    "https://tenor.com/view/its-really-worked-lachlan-watson-susie-putnam-chilling-adventures-of-sabrina-it-works-gif-16476944"
]

HAPPY_GIFS = [
    'https://tenor.com/view/monkey-ape-dance-dancing-orangutan-gif-13620205',
    'https://tenor.com/view/spongebob-squarepants-dance-happydance-gif-5027512',
    'https://giphy.com/gifs/happy-excited-cartoons-F6PFPjc3K0CPe',
    'https://giphy.com/gifs/iDCLcl7D81aYgLLqyc',
    'https://giphy.com/gifs/dancing-happy-seinfeld-BlVnrxJgTGsUw',
    'https://giphy.com/gifs/happy-car-home-rdma0nDFZMR32',
    'https://giphy.com/gifs/dancing-happy-cartoons-10UeedrT5MIfPG',
    'https://giphy.com/gifs/dancing-happy-fat-h8UyZ6FiT0ptC',
    'https://giphy.com/gifs/studiosoriginals-3oz8xRF0v9WMAUVLNK',
    'https://tenor.com/o4YY.gif',
    'https://tenor.com/ojAo.gif',
    'https://tenor.com/uM8D.gif',
    'https://tenor.com/EqyI.gif',
    'https://tenor.com/xDwo.gif',
    'https://tenor.com/pnrA.gif',
    'https://tenor.com/FJUi.gif',
    'https://tenor.com/ZRuj.gif',
    'https://tenor.com/o39P.gif',
    'https://tenor.com/o48y.gif',
    'https://tenor.com/pbNb.gif',
    'https://giphy.com/gifs/very-indian-Qoif4TqDdUBlC',
    'https://giphy.com/gifs/3NtY188QaxDdC',
    'https://tenor.com/ot2Y.gif',
    'https://tenor.com/pjo5.gif',
    'https://tenor.com/spVE.gif',
    'https://tenor.com/x6z9.gif',
    'https://giphy.com/gifs/funny-happy-anne-hathaway-XjlZn2rQ9H65W',
    'https://giphy.com/gifs/teamcoco-42zi0ri7sN1Uy8aQqL',
    'https://tenor.com/view/singing-shower-shower-jams-happpy-feeling-good-gif-16673755',
    'https://tenor.com/view/happy-birthday-amy-happy-birthday-amy-gif-5600765',
    'https://tenor.com/view/qoobee-agapi-dancing-happy-dance-gif-11624520',
    'https://tenor.com/view/teletubbies-purple-happy-excited-dance-gif-5527715',
    'https://tenor.com/view/yay-yes-yeahhh-cute-girl-happy-dance-gif-14559695',
    'https://tenor.com/view/dancing-dance-dancing-baby-baby-toddler-gif-5478110',
    'https://tenor.com/view/baby-dancing-cute-happy-dance-gif-7520100',
    'https://tenor.com/view/baby-dancing-gif-5225436',
    'https://tenor.com/view/happy-baby-gif-3985449',
    'https://tenor.com/view/excited-baby-gif-10285345',
    'https://tenor.com/view/baby-happy-excited-ice-cream-gif-7796682',
    'https://media.tenor.com/images/e8205cdf08bd575e3679172cbd98c320/tenor.gif'
]

STAB_GIFS = [
    'https://tenor.com/62VK.gif',
    'https://tenor.com/6YFf.gif',
    'https://tenor.com/bdFIe.gif',
    'https://tenor.com/vR88.gif',
    'https://tenor.com/tV4l.gif',
    'https://tenor.com/beF5i.gif',
    'https://tenor.com/tQ3i.gif',
    'https://tenor.com/R9WB.gif',
    'https://tenor.com/OCSq.gif',
    'https://giphy.com/gifs/angry-guardians-of-the-galaxy-stab-xUySTCy0JHxUxw4fao',
    'https://giphy.com/gifs/stab-62SpAiHj3tu7K',
    'https://giphy.com/gifs/Friends-season-1-friends-tv-the-one-with-butt-LPs5pRt1OiaHqgTQoT',
    'https://giphy.com/gifs/season-16-the-simpsons-16x8-3orieSCSGT3ji43dvy',
    'https://giphy.com/gifs/prince-diana-JmsK5Qwt11nudUOn2p',
    'https://giphy.com/gifs/off-knock-stab-YEsQDxt4hhcJy',
    'https://giphy.com/gifs/realitytvgifs-eating-vh1-7gGXGl8sc4NLW',
    'https://giphy.com/gifs/mad-1ludrxHRnUmT6',
    'https://tenor.com/view/happy-halloween-halloween-knife-stab-slashing-gif-15612596',
    'https://tenor.com/view/ill-cut-you-threat-warning-pissed-mad-gif-4712383'
]

GO_PACK_GIFS = [
    'https://tenor.com/view/football-minions-happy-sunday-go-pack-cute-gif-16213324',
    'https://tenor.com/view/football-ncsu-gif-5701991',
    'https://tenor.com/view/football-ncsu-gameday-gif-5702002',
    'https://tenor.com/view/football-fan-ncsu-gif-5701998',
    'https://tenor.com/view/football-ncsu-fan-gif-5701997',
    'https://tenor.com/view/nc-state-wolfpack-wolf-pack-gif-13285259',
    'https://giphy.com/gifs/packathletics-mascot-wolfpack-xUNda0k0UuwEl79BwA',
    'https://giphy.com/gifs/packathletics-wolfpack-ncsu-d2jjzZz4ol99reJa',
    'https://giphy.com/gifs/packathletics-wolfpack-nc-state-13IV1rqoO2XHu8',
    'https://giphy.com/gifs/packathletics-football-defense-EfmET8HKhlV2U',
    'https://giphy.com/gifs/packathletics-wolfpack-nc-state-xUOxeQAp4k6WbRMXWo',
    'https://giphy.com/gifs/packathletics-soccer-peace-rUkfRx2KtESKQ',
    'https://giphy.com/gifs/packathletics-wolfpack-nc-state-3ohs7QeAGMaXZD5pSw',
    'https://giphy.com/gifs/packathletics-high-five-wolfpack-xUOxeS258gH1okO5eo',
    'https://giphy.com/gifs/packathletics-flag-wolfpack-OqxxnqiDjIXHW',
    'https://giphy.com/gifs/packathletics-wolfpack-nc-state-3o752jJuezfpFoYG4w',
    'https://media.giphy.com/media/Hy0fWGdiVWSTm/giphy.gif',
    'https://media.giphy.com/media/3osBL1OFEGRlAqCk48/giphy.gif',
    'https://media.giphy.com/media/3o7526KdBziUz9JKDe/giphy.gif',
    'https://media.giphy.com/media/3ohs85ahY8OqgMyvJK/giphy.gif',
    'https://media.giphy.com/media/F3LuaIwVUHKzZwNgRx/giphy.gif',
    'https://media.giphy.com/media/cbgdgBRm1ABLq/giphy.gif',
    'https://media.giphy.com/media/3o6fJh6JtQhNI1iWdO/giphy.gif',
    'https://media.giphy.com/media/3ohhwjMEe8Bi8gaK6A/giphy.gif',
    'https://media.giphy.com/media/3ohhwjMEe8Bi8gaK6A/giphy.gif',
    'https://media.giphy.com/media/3osBLmBC8McXMUs3Dy/giphy.gif',
    'https://media.giphy.com/media/vfVxsjEYW4LMA/giphy.gif',
    'https://media.giphy.com/media/3o6nV4erqmVRM5COKQ/giphy.gif',
    'https://media.giphy.com/media/fIYrZ7Eydh1io/giphy.gif',
    'https://media.giphy.com/media/5n3I9KkUXDezs0a2Z2/giphy.gif',
    'https://media.giphy.com/media/2zoCNHT7ktXSC5xrqr/giphy.gif',
    'https://media.giphy.com/media/d989nWPJ51ny0/giphy.gif',
    'https://media.giphy.com/media/3kHGfJaNWrYc4WxreR/giphy.gif'
]

SAD_GIFS = [
    'https://tenor.com/xrDJ.gif',
    'https://tenor.com/tFAk.gif',
    'https://tenor.com/oVss.gif',
    'https://tenor.com/y6oP.gif',
    'https://tenor.com/tzEM.gif',
    'https://tenor.com/2boM.gif',
    'https://tenor.com/PlOc.gif',
    'https://giphy.com/gifs/house-boyfriends-qQdL532ZANbjy',
    'https://giphy.com/gifs/sad-please-choked-up-ZEgBHVeRlmTqjCPlqx',
    'https://giphy.com/gifs/inside-out-gif-10tIjpzIu8fe0',
    'https://giphy.com/gifs/blackish-anthony-anderson-dre-johnson-d2lcHJTG5Tscg',
    'https://giphy.com/gifs/sad-a9xhxAxaqOfQs',
    'https://giphy.com/gifs/force-awakens-behindthescenes-JEVqknUonZJWU',
    'https://giphy.com/gifs/memecandy-UqvyxmNFmoEocT0R9g',
    'https://giphy.com/gifs/right-in-the-feels-lKWlXRBGltz2g',
    'https://giphy.com/gifs/latenightseth-seth-meyers-late-night-lnsm-58FMysL4cmjsIales5',
    'https://tenor.com/HbzX.gif',
    'https://tenor.com/59yJ.gif',
    'https://tenor.com/view/missing-you-sad-cry-gif-12874462',
    'https://tenor.com/view/stressed-stress-baby-crying-cry-gif-8768811',
    'https://tenor.com/view/amanda-mood-sad-thinking-gif-13525260',
    'https://tenor.com/view/sorry-sad-puppyeyes-agnes-despicable-me-gif-4953469',
    'https://tenor.com/view/lilo-and-stitch-mood-sad-gloomy-depressed-gif-11662158',
    'https://tenor.com/view/milk-and-mocha-couple-sad-cry-tantrum-gif-12535132',
    'https://tenor.com/view/powerpuff-girls-bubbless-cry-sad-gif-6077887',
    'https://tenor.com/view/cute-animals-cat-sad-kitty-gif-3528952',
    'https://tenor.com/view/bunny-rabbit-sad-tired-drag-gif-11453485',
    'https://tenor.com/view/star-wars-the-mandalorian-baby-yoda-sad-gif-15736604',
    'https://tenor.com/view/eating-sad-gif-4488293',
    'https://tenor.com/view/milk-mocha-milk-and-mocha-bears-cute-sad-gif-13418496',
    'https://tenor.com/view/groot-sad-eyes-gif-12797009',
    'https://tenor.com/view/jakeperalta-jake-peralta-b99-brooklynninenine-gif-8793716',
    'https://tenor.com/view/brooklyn99-sad-serious-gif-12956579',
    'https://tenor.com/view/brooklyn99-gif-10476121',
    'https://tenor.com/view/sadness-sadly-sad-so_sad-upset-gif-7589477',
    'https://tenor.com/view/gus-psych-crying-eating-gif-5407565',
    'https://tenor.com/view/eating-cheese-sad-eating-crying-with-cheese-cheese-understands-gif-11497469',
    'https://tenor.com/view/jake-sad-bread-stress-eating-gif-14630049',
    'https://tenor.com/view/allerhande-albert-heijn-albertheijn-crying-gif-15720793',
    'https://tenor.com/view/masterchef-junior-child-sad-crying-gif-11466656',
    'https://tenor.com/view/pizza-sad-gif-4902290',
    'https://tenor.com/view/chocolate-depressed-gif-10689744',
    'https://tenor.com/view/eating-hungry-crying-while-eating-little-boy-and-burger-burger-gif-16263958',
    'https://tenor.com/view/himym-sad-eating-chicken-wings-gif-13327887',
    'https://tenor.com/view/cry-crying-sad-eating-gif-14135009'
]

BEAR_GIFS = [
    'https://giphy.com/gifs/eating-bear-icecream-uUs14eCA2SBgs',
    'https://giphy.com/gifs/tiktok-bear-tsX3YMWYzDPjAARfeg',
    'https://giphy.com/gifs/bear-forest-water-IQ9KefLJHfJPq',
    'https://giphy.com/gifs/sandiegozoo-reaction-cute-bear-f9RrjwK6CFFasFW3pP',
    'https://giphy.com/gifs/bear-tired-RpP4d9YMRKIVy',
    'https://giphy.com/gifs/hello-hi-dzaUX7CAG0Ihi',
    'https://giphy.com/gifs/bbc-cute-bear-3oeHLrjZGBgnPx5VII',
    'https://tenor.com/98m6.gif',
    'https://tenor.com/Wwrj.gif',
    'https://tenor.com/KLWS.gif',
    'https://tenor.com/view/bear-guitar-gif-7397917',
    'https://tenor.com/view/sleeping-bear-tired-gif-9532525',
    'https://tenor.com/view/back-scratch-wild-animals-bears-gif-11605931',
    'https://tenor.com/view/bearvsman-bear-kung-fy-gif-5430193',
    'https://tenor.com/view/bear-gif-3398413',
    'https://tenor.com/view/wave-bear-bearwave-gif-5435322',
    'https://tenor.com/view/bear-hi-hello-wave-gif-7585194',
    'https://tenor.com/view/bear-wave-hi-hey-hello-gif-15430039'
]

SMUG_GIFS = [
    'https://tenor.com/pa0s.gif',
    'https://tenor.com/pCAO.gif',
    'https://tenor.com/2Yww.gif',
    'https://tenor.com/uWNv.gif',
    'https://tenor.com/oV09.gif',
    'https://tenor.com/bkjrD.gif',
    'https://tenor.com/ua87.gif',
    'https://tenor.com/wgyW.gif',
    'https://giphy.com/gifs/smug-Vff5Qxz6LLzag',
    'https://giphy.com/gifs/laughing-drinking-madonna-mS3jA0z4oEc5q',
    'https://giphy.com/gifs/moodman-dXKiD8XysOuhFAJB1f',
    'https://giphy.com/gifs/smug-happy-pleased-12pxmojmEOifde',
    'https://giphy.com/gifs/laughing-seinfeld-cigar-e2QYPpUe8WmpG',
    'https://tenor.com/view/the-breakfast-club-brian-johnson-anthony-michael-hall-cool-sunglasses-gif-4110995',
    'https://tenor.com/view/ryan-reynolds-smirk-stare-smile-gif-4318212',
    'https://tenor.com/view/ross-friends-smug-smile-oops-gif-4195535',
    'https://tenor.com/view/rihanna-hairflip-gif-7920134',
    'https://tenor.com/view/ellen-rihanna-wink-point-smile-gif-5043187',
    'https://tenor.com/view/hairflip-christopherpalu-christopher-palu-gif-5427236',
    'https://tenor.com/view/evil-smile-kid-smile-smirk-gif-4425782',
    'https://tenor.com/view/nick-wilde-zootopia-fox-disney-smug-gif-5225055'
]

VSCO_GIFS = [
    'https://media.giphy.com/media/dsRhOFxpP6CA2lWjk7/giphy.gif',
    'https://media.giphy.com/media/LPg8cD45aMKNEclYE6/giphy.gif',
    'https://media.giphy.com/media/QBRbQoCnlvoFfGhZUJ/giphy.gif',
    'https://media.giphy.com/media/kdcV3QqZi2U18FOcFC/giphy.gif',
    'https://media.giphy.com/media/JPUz02hs4aPsf77G1X/giphy.gif',
    'https://media.giphy.com/media/TFU3IdPBvL55lu15Pd/giphy.gif',
    'https://media.giphy.com/media/8vFgqW1w2q4itmmtjH/giphy.gif',
    'https://tenor.com/bbU3m.gif',
    'https://tenor.com/bbEiA.gif',
    'https://tenor.com/bb4kQ.gif',
    'https://tenor.com/bcNE4.gif'
]

EGIRL_GIFS = [
    'https://media.giphy.com/media/iihJBp876B8lVu8WxX/giphy.gif',
    'https://media.giphy.com/media/5PhPGIi0de78k/giphy.gif',
    'https://tenor.com/biTxH.gif',
    'https://tenor.com/biTxL.gif',
    'https://tenor.com/bdhBc.gif',
    'https://tenor.com/bfQIZ.gif',
    'https://tenor.com/bgd8T.gif',
    'https://tenor.com/9tX4.gif',
    'https://tenor.com/bieoB.gif',
    'https://tenor.com/bfQJi.gif',
    'https://tenor.com/bfQIF.gif',
    'https://tenor.com/biTxG.gif',
    'https://tenor.com/bjfqr.gif',
    'https://tenor.com/bfQI2.gif',
    'https://tenor.com/5aAq.gif'
]

SLAP_GIFS = [
    'https://media.giphy.com/media/mEtSQlxqBtWWA/giphy.gif',
    'https://media.giphy.com/media/lX03hULhgCYQ8/giphy.gif',
    'https://media.giphy.com/media/uG3lKkAuh53wc/giphy.gif',
    'https://media.giphy.com/media/zvDT09xBhcuMo/giphy.gif',
    'https://media.giphy.com/media/s5zXKfeXaa6ZO/giphy.gif',
    'https://media.giphy.com/media/LRkmAC0NujTLVPuQH4/giphy.gif',
    'https://media.giphy.com/media/4Nphcg0CCOfba/giphy.gif',
    'https://media.giphy.com/media/jEYH3RJVXK8Ba/giphy.gif',
    'https://media.giphy.com/media/uqSU9IEYEKAbS/giphy.gif',
    'https://media.giphy.com/media/lJhkXgS84lfzO/giphy.gif',
    'https://media.giphy.com/media/lJhkXgS84lfzO/giphy.gif',
    'https://media.giphy.com/media/bPhJzBSnBHRS0/giphy.gif',
    'https://media.giphy.com/media/3EAwGiruFDUQM/giphy.gif',
    'https://tenor.com/vX72.gif'
    'https://media.giphy.com/media/sRgD8LyikpFO8/giphy.gif'
]

PUNCH_GIFS = [
    'https://media.giphy.com/media/l1J3G5lf06vi58EIE/giphy.gif',
    'https://media.giphy.com/media/DViGV8rfVjw6Q/giphy.gif',
    'https://media.giphy.com/media/lCUbIxFdMzcZ2/giphy.gif',
    'https://media.giphy.com/media/x6I3pGtblFtDO/giphy.gif',
    'https://media.giphy.com/media/l41lZEoYn6z1uc2fS/giphy.gif',
    'https://media.giphy.com/media/VXxy0at5j484U/giphy.gif',
    'https://media.giphy.com/media/jnVmME9bfPdiGHkogW/giphy.gif',
    'https://media.giphy.com/media/nq0qLlrcdahiw/giphy.gif',
    'https://media.giphy.com/media/26xBPQU5sWj6KvDqM/giphy.gif',
    'https://media.giphy.com/media/xT9KVGie0lvAr1gjNC/giphy.gif',
    'https://media.giphy.com/media/3o6ZtrxkK4jLkmn8He/giphy.gif',
    'https://media.giphy.com/media/RMGjus0Fr1uJdeRvrq/giphy.gif',
    'https://media.giphy.com/media/3oEhn4mIrTuCf0bn1u/giphy.gif',
    'https://media.giphy.com/media/3o6Zt3Vcz5fI81y4ms/giphy.gif',
    'https://media.giphy.com/media/3o7TKqAAv17MctZoYM/giphy.gif'

]

KICK_GIFS = [
    'https://media.giphy.com/media/xTcnTjeH5rtf6bdlwA/giphy.gif',
    'https://media.giphy.com/media/ikcJ56KAyhm8w/giphy.gif',
    'https://media.giphy.com/media/10M6fIkFbwqaEo/giphy.gif',
    'https://media.giphy.com/media/l2QE2CQyK2ZyVEGJy/giphy.gif',
    'https://media.giphy.com/media/qiiimDJtLj4XK/giphy.gif',
    'https://media.giphy.com/media/l3V0j3ytFyGHqiV7W/giphy.gif',
    'https://media.giphy.com/media/63MO9LTRoTXQk/giphy.gif',
    'https://media.giphy.com/media/3oriNOXmaxj8czSHMQ/giphy.gif',
    'https://media.giphy.com/media/l0HlSrrMgYyfyv44M/giphy.gif',
    'https://media.giphy.com/media/OQrzlc6o5xPSx1y3Sr/giphy.gif',
    'https://media.giphy.com/media/SUcbczGWButCU/giphy.gif',
    'https://media.giphy.com/media/k165r8jDrh2ko/giphy.gif',
    'https://media.giphy.com/media/l41YigyTvRbquosik/giphy.gif',
    'https://media.giphy.com/media/P3x1oqza891SM/giphy.gif',
    'https://media.giphy.com/media/3oEdv3qMS7Awt16NkA/giphy.gif',
    'https://media.giphy.com/media/JuZCqD9wXvGAE/giphy.gif',
    'https://media.giphy.com/media/kDwKAjmtRpO9RTLcHq/giphy.gif',
    'https://media.giphy.com/media/SsZViiaRCjgp8fVexU/giphy.gif',
    'https://media.giphy.com/media/xT5LMY2kXko8zjyiwU/giphy.gif',
    'https://media.giphy.com/media/ILfkGwgue5taE/giphy.gif'
]

HAIR_FLIP_GIFS = [
    'https://media.giphy.com/media/xThuWhoaNyNBjTGERa/giphy.gif',
    'https://media.giphy.com/media/qoHwZIywwQwvu/giphy.gif',
    'https://media.giphy.com/media/3rgXBy5gnBBhneH6es/giphy.gif',
    'https://media.giphy.com/media/3rgXBrKYHpE3NeKOFW/giphy.gif',
    'https://media.giphy.com/media/yoJC2D8uYvDqHP0FPO/giphy.gif',
    'https://media.giphy.com/media/3o6ZteawRr3KJtLdW8/giphy.gif',
    'https://media.giphy.com/media/lMsT2f47tDxFMYdJMC/giphy.gif',
    'https://media.giphy.com/media/iemgeDQlYlgNZrZUoQ/giphy.gif',
    'https://media.giphy.com/media/4ZXDlLQMdguYM/giphy.gif',
    'https://media.giphy.com/media/O6j18IUvEwRPO/giphy.gif',
    'https://media.giphy.com/media/YMHA5oACfpMy4phDKu/giphy.gif',
    'https://media.giphy.com/media/SYcfbJpRiwCvcXWACx/giphy.gif',
    'https://media.giphy.com/media/28NdeIanWNmDgKszWt/giphy.gif',
    'https://media.giphy.com/media/11o26CuK1M1Jgk/giphy.gif',
    'https://media.giphy.com/media/jtdTBi3tktFrKNmLr4/giphy.gif',
    'https://media.giphy.com/media/oHBfyejfUeuiY/giphy.gif',
    'https://media.giphy.com/media/let5xncOnbLgc/giphy.gif',
    'https://media.giphy.com/media/11ZYkaT2S2XepO/giphy.gif',
    'https://media.giphy.com/media/UPYDMu2P6g1KE2iOMu/giphy.gif',
    'https://media.giphy.com/media/2o3xpHevpWJTq/giphy.gif',
    'https://media.giphy.com/media/l8M9NwUdRTGKY/giphy.gif',
    'https://media.giphy.com/media/ciwhF69Pg9rkMvUmvg/giphy.gif',
    'https://media.giphy.com/media/l3q2x7SgnWJziJpkI/giphy.gif',
    'https://gph.is/NevIrA'
]

HUG_GIFS = [
    'https://media.giphy.com/media/3M4NpbLCTxBqU/giphy.gif',
    'https://media.giphy.com/media/3oEdv4hwWTzBhWvaU0/giphy.gif',
    'https://media.giphy.com/media/l4FGpP4lxGGgK5CBW/giphy.gif',
    'https://media.giphy.com/media/2GnS81AihShS8/giphy.gif',
    'https://media.giphy.com/media/QbkL9WuorOlgI/giphy.gif',
    'https://media.giphy.com/media/EvYHHSntaIl5m/giphy.gif',
    'https://media.giphy.com/media/gnXG2hODaCOru/giphy.gif',
    'https://media.giphy.com/media/JzsG0EmHY9eKc/giphy.gif',
    'https://media.giphy.com/media/OiKAQbQEQItxK/giphy.gif',
    'https://media.giphy.com/media/jMGxhWR7rtTNu/giphy.gif',
    'https://media.giphy.com/media/xT0xemCvkpWyJlOG2Y/giphy.gif',
    'https://media.giphy.com/media/117o9BJASzmLNC/giphy.gif',
    'https://media.giphy.com/media/RPyUPymjO4YJa/giphy.gif',
    'https://media.giphy.com/media/xT1XGPy39lDKJ5Gc5W/giphy.gif',
    'https://media.giphy.com/media/3orif2vpZbXi8P0fPW/giphy.gif',
    'https://media.giphy.com/media/a5vmVcRPc63qU/giphy.gif',
    'https://media.giphy.com/media/RcRYxbOb4Cd0aMdFnS/giphy.gif',
    'https://media.giphy.com/media/4d4HEGpLiwTQc/giphy.gif',
    'https://media.tenor.com/images/ba7773b9d7e036a9c2f9282a916a519a/tenor.gif',
    'https://media.tenor.com/images/e6a5583ec2f3912bbbba976db910ca35/tenor.gif'
]

EMBED_COLORS = [
    discord.Colour.magenta(),
    discord.Colour.blurple(),
    discord.Colour.dark_teal(),
    discord.Colour.blue(),
    discord.Colour.dark_blue(),
    discord.Colour.dark_gold(),
    discord.Colour.dark_green(),
    discord.Colour.dark_grey(),
    discord.Colour.dark_magenta(),
    discord.Colour.dark_orange(),
    discord.Colour.dark_purple(),
    discord.Colour.dark_red(),
    discord.Colour.darker_grey(),
    discord.Colour.gold(),
    discord.Colour.green(),
    discord.Colour.greyple(),
    discord.Colour.orange(),
    discord.Colour.purple(),
    discord.Colour.magenta(),
]

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/drive.appdata',
          'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file']

# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        CREDS = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not CREDS or not CREDS.valid:
    if CREDS and CREDS.expired and CREDS.refresh_token:
        CREDS.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        CREDS = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(CREDS, token)

SERVICE = build('drive', 'v3', credentials=CREDS)

# Call the Drive v3 API
results = SERVICE.files().list(
    pageSize=20, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        driveFiles[item['name']] = item['id']

print(driveFiles)


# adding file
# file_metadata = {'name': 'ap.txt'}

# media = MediaFileUpload('ap.txt',
#                        mimetype='text/plain')

# file = service.files().create(body=file_metadata,
#                                    media_body=media,
#                                    fields='id').execute()

# print('File ID: %s' % file.get('id'))


# retrieve the file from the API.
# file_ap_txt = service.files().get(fileId=driveFiles['ap.txt']).execute()
# print(file_ap_txt)
# service.files().delete(fileId=driveFiles['ap.txt']).execute()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='=help for more information'))
    print('We have logged in as {0.user}'.format(client))


def dictRead(fileName, dictionary, separator):
    global SERVICE
    file = SERVICE.files().get(fileId=driveFiles[fileName]).execute()
    data = str(SERVICE.files().get_media(fileId=driveFiles[fileName]).execute())
    length = len(data)
    dataStripped = data[2: length - 1]

    dataList = dataStripped.split('\\n')
    f = open('tempfile.txt', 'w')

    for elem in dataList:
        f.write(elem)
        f.write('\n')
    f.close()

    f = open('tempfile.txt', 'r')
    with f as reader:
        line = reader.readline()
        while line != '':
            try:
                lineTuple = line.partition(separator)
                dictionary[int(lineTuple[0])] = lineTuple[2]
                counter = int(lineTuple[0])
                counterVal = lineTuple[2]
                line = reader.readline()
            except:
                dictionary[counter] += line
                line = reader.readline()
    f.close()


def toDoFileRead(fileName, dictionary, separator):
    global SERVICE
    file = SERVICE.files().get(fileId=driveFiles[fileName]).execute()
    data = str(SERVICE.files().get_media(fileId=driveFiles[fileName]).execute())
    length = len(data)
    dataStripped = data[2: length - 1]

    dataList = dataStripped.split('\\n')
    f = open('tempfile.txt', 'w')

    for elem in dataList:
        f.write(elem)
        f.write('\n')
    f.close()

    f = open('tempfile.txt', 'r')
    with f as reader:
        line = reader.readline()
        while line != '':
            try:
                todolist = line.split(" | ")
                i = 1
                listString = ''
                while i < 11:
                    listString += todolist[i]
                    listString += " | "
                    i += 1
                personalDictionary = toDoListRead(listString)
                editingDict = toDoDictEdit(personalDictionary)
                dictionary[int(todolist[0])] = editingDict
                line = reader.readline()
            except:
                line = reader.readline()
        f.close()


def userTagsDictWrite(fileName):
    f = open(fileName, "w")
    for dictVal in userTags:
        f.write(str(dictVal) + " : " + userTags[dictVal])
    f.close()


def toDoListRead(listString):
    personalDict = {}
    listSplit = listString.split(" | ")
    i = 1
    while i < 11:
        try:
            personalDict[i] = listSplit[i - 1]
            i += 1
        except:
            break
    return personalDict


def toDoDictEdit(dictionary):
    dictVal = 1
    printVal = 1
    newDict = {}
    while dictVal < 11:
        if dictionary[dictVal] != '' and dictionary[dictVal] != '\n':
            newDict[printVal] = dictionary[dictVal]
            printVal += 1
        dictVal += 1

    while printVal < 11:
        newDict[printVal] = ''
        printVal += 1

    return newDict


def toDoPrintDict(dictionary):
    dictVal = 1
    printVal = 1
    returnStr = ''
    while dictVal < 11:
        if dictionary[dictVal] != '' and dictionary[dictVal] != '\n':
            returnStr += str(printVal) + ": "
            returnStr += dictionary[dictVal]
            returnStr += "\n"
            printVal += 1
        dictVal += 1
    if returnStr == '':
        returnStr += "You do not have anything on your To-Do list! Type =add <item> to add something to your list."
    return returnStr


def numItemsInToDoList(dictionary):
    dictVal = 1
    numItems = 0
    while dictVal < 11:
        if dictionary[dictVal] != '' and dictionary[dictVal] != '\n':
            numItems += 1
        dictVal += 1
    return numItems


def toDoWrite(fileName):
    file = open(fileName, "w")
    for val in toDoListDict:
        file.write(str(val) + ' | ')
        i = 0
        for personalVal in toDoListDict[val]:
            i += 1
            if i < 10:
                file.write(toDoListDict[val][personalVal] + " | ")
            if i == 10:
                file.write(toDoListDict[val][personalVal])
        file.write('\n')
    file.close()


def dictReadFood(fileName, dictionary, separator):
    global SERVICE
    file = SERVICE.files().get(fileId=driveFiles[fileName]).execute()
    data = str(SERVICE.files().get_media(fileId=driveFiles[fileName]).execute())
    length = len(data)
    dataStripped = data[2: length - 1]

    dataList = dataStripped.split('\\n')
    f = open('tempfile.txt', 'w')

    for elem in dataList:
        f.write(elem)
        f.write('\n')
    f.close()

    f = open('tempfile.txt', 'r')
    with f as reader:
        line = reader.readline()
        i = 100
        while line != '':
            lineTuple = line.partition(separator)
            lineStr = lineTuple[2].strip().split(" | ")
            dictionary[i] = lineStr
            line = reader.readline()
            i += 1
    f.close()


def foodWrite(fileName):
    file = open(fileName, "w")
    i = 100
    while i < 136:
        file.write(str(i) + ' : ')
        file.write(
            foodDict[i][0] + " | " + str(foodDict[i][1]) + " | " + str(foodDict[i][2]) + " | " + str(foodDict[i][3]))
        file.write('\n')
        i += 1
    file.close()


dictRead(fileName='usertagsfile.txt', dictionary=userTags, separator=" : ")

dictRead(fileName='ap.txt', dictionary=apClasses, separator=' | ')

dictRead(fileName="ap_scorevalues.txt", dictionary=apValues, separator=' | ')

toDoFileRead(fileName="todolist.txt", dictionary=toDoListDict, separator=' | ')

dictRead(fileName="wordsWithDefs.txt", dictionary=wordsDict, separator=' . ')

dictReadFood(fileName='food.txt', dictionary=foodDict, separator=' : ')
print(foodDict)

# ap page embeds
randomColor = randrange(len(EMBED_COLORS))
page1 = discord.Embed(
    title="AP Classes List",
    description="type =ap <code> for specific information per class",
    colour=EMBED_COLORS[randomColor]
)
val = 0

for n in apClasses:
    page1.add_field(name=apClasses[val], value=str(val), inline=False)
    val += 1
    if val > 10 - 1:
        break

randomColor = randrange(len(EMBED_COLORS))
page2 = discord.Embed(
    title="AP Classes List",
    description="type =ap <code> for specific information per class",
    colour=EMBED_COLORS[randomColor]
)
val = 10
for n in apClasses:
    page2.add_field(name=apClasses[val], value=str(val), inline=False)
    val += 1
    if val > 20 - 1:
        break

randomColor = randrange(len(EMBED_COLORS))
page3 = discord.Embed(
    title="AP Classes List",
    description="type =ap <code> for specific information per class",
    colour=EMBED_COLORS[randomColor]
)
val = 20
for n in apClasses:
    page3.add_field(name=apClasses[val], value=str(val), inline=False)
    val += 1
    if val > 30 - 1:
        break

randomColor = randrange(len(EMBED_COLORS))
page4 = discord.Embed(
    title="AP Classes List",
    description="type =ap <code> for specific information per class",
    colour=EMBED_COLORS[randomColor]
)
val = 30
for n in apClasses:
    page4.add_field(name=apClasses[val], value=str(val), inline=False)
    val += 1
    if val > len(apClasses) - 1:
        break

pages = [page1, page2, page3, page4]

# food page embeds
randomColor = randrange(len(EMBED_COLORS))
page1food = discord.Embed(
    title="Food On Campus",
    description="type =rfood <code> <rate> to rate\n or =food <code> to view",
    colour=EMBED_COLORS[randomColor]
)
val = 100

for n in apClasses:
    page1food.add_field(name=foodDict[val][0], value=str(val), inline=False)
    val += 1
    if val > 110 - 1:
        break

randomColor = randrange(len(EMBED_COLORS))
page2food = discord.Embed(
    title="Food On Campus",
    description="type =rfood <code> <rate> to rate\n or =food <code> to view",
    colour=EMBED_COLORS[randomColor]
)
val = 110
for n in apClasses:
    page2food.add_field(name=foodDict[val][0], value=str(val), inline=False)
    val += 1
    if val > 120 - 1:
        break

randomColor = randrange(len(EMBED_COLORS))
page3food = discord.Embed(
    title="Food On Campus",
    description="type =rfood <code> <rate> to rate\n or =food <code> to view",
    colour=EMBED_COLORS[randomColor]
)
val = 120
for n in apClasses:
    page3food.add_field(name=foodDict[val][0], value=str(val), inline=False)
    val += 1
    if val > 130 - 1:
        break

randomColor = randrange(len(EMBED_COLORS))
page4food = discord.Embed(
    title="Food On Campus",
    description="type =rfood <code> <rate> to rate\n or =food <code> to view",
    colour=EMBED_COLORS[randomColor]
)
val = 130
for n in apClasses:
    page4food.add_field(name=foodDict[val][0], value=str(val), inline=False)
    val += 1
    if val > 136 - 1:
        break

pagesFood = [page1food, page2food, page3food, page4food]


@client.event
async def on_message(message):
    global AP_CONSTANT
    global SERVICE
    global RANDOMCONSTANTWORKS
    global RANDOMCONSTANTHAPPY
    global RANDOMCONSTANTSTAB
    global RANDOMCONSTANTGOPACK
    global RANDOMCONSTANTSAD
    global RANDOMCONSTANTEGIRL
    global RANDOMCONSTANTBEAR
    global RANDOMCONSTANTVSCO
    global RANDOMCONSTANTEGIRL
    global RANDOMCONSTANTSLAP
    global RANDOMCONSTANTPUNCH
    global RANDOMCONSTANTKICK
    global RANDOMCONSTANTHAIRFLIP
    global RANDOMCONSTANTSMUG
    global RANDOMCONSTANTHUG
    global RANDOMCONSTANTWORD

    if message.author == client.user:
        return

    if message.content.lower().startswith('=test'):
        AP_CONSTANT = 0
        await message.channel.send("works")

    if message.content.lower().startswith('=help'):
        randomColor = randrange(len(EMBED_COLORS))
        AP_CONSTANT = 0
        global SERVICE
        file = SERVICE.files().get(fileId=driveFiles['help.txt']).execute()
        data = str(SERVICE.files().get_media(fileId=driveFiles['help.txt']).execute())
        length = len(data)
        dataStripped = data[2: length - 1]
        msg = ''
        for elem in dataStripped.split('\\n'):
            msg += elem
            msg += '\n'
        embedHelp = discord.Embed(
            title="__**my prefix is: '='**__",
            description=msg,
            colour=EMBED_COLORS[randomColor]
        )
        embedHelp.set_footer(text="Requested by:" + message.author.name)
        await message.channel.send(embed=embedHelp)

    if message.content.lower().startswith('=info'):
        AP_CONSTANT = 0
        await message.channel.send(
            "Hello, I'm the brickyard bot specifically designed to be a custom bot for the server. I am currently "
            "being built so please be patient! My birthday is on May 11 2020")

    if message.content.lower() == '=me':
        AP_CONSTANT = 0
        if message.author.id in userTags:
            await message.channel.send(userTags[message.author.id])
        else:
            await message.channel.send(userTags[0])

    if message.content.lower().startswith('=set ') and len(message.content) < 55:
        AP_CONSTANT = 0
        if '\n' in message.content[5:] or '@' in message.content[5:]:
            await message.channel.send("Your message is not valid. Try again")
        else:
            userTags[message.author.id] = message.content[5:] + "\n"
            await message.channel.send(
                message.author.name + ' you have set your message to ' + userTags[message.author.id])

            userTagsDictWrite("usertagsfile.txt")
            file_metadata = {'name': 'usertagsfile.txt'}

            media = MediaFileUpload('usertagsfile.txt',
                                    mimetype='text/plain')

            file = SERVICE.files().create(body=file_metadata,
                                          media_body=media,
                                          fields='id').execute()

            SERVICE.files().delete(fileId=driveFiles['usertagsfile.txt']).execute()

            driveFiles['usertagsfile.txt'] = file.get('id')

            if os.path.exists("usertagsfile.txt"):
                os.remove("usertagsfile.txt")
            else:
                print("The file does not exist")

    if message.content.lower() == "=aplist":
        AP_CONSTANT = 1
        page1.set_footer(
            text="Requested by: " + message.author.name + "\nPage 1/4\nIdea: Henry\nLast Updated: 13 May 2020")
        page2.set_footer(
            text="Requested by: " + message.author.name + "\nPage 2/4\nIdea: Henry\nLast Updated: 13 May 2020")
        page3.set_footer(
            text="Requested by: " + message.author.name + "\nPage 3/4\nIdea: Henry\nLast Updated: 13 May 2020")
        page4.set_footer(
            text="Requested by: " + message.author.name + "\nPage 4/4\nIdea: Henry\nLast Updated: 13 May 2020")

        msg = await message.channel.send(embed=page1)

        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')
        await msg.add_reaction('4️⃣')

    if message.content.lower().startswith("=ap "):
        AP_CONSTANT = 0
        randomColor = randrange(len(EMBED_COLORS))
        try:
            apVal = int(message.content[4:])
            apValEmbed = discord.Embed(
                title="AP Credit Values for " + apClasses[apVal],
                description=apValues[apVal],
                colour=EMBED_COLORS[randomColor]
            )
            apValEmbed.set_footer(
                text="Requested by: " + message.author.name + "\nIdea: Henry\nLast Updated: 13 May 2020")
            await message.channel.send(embed=apValEmbed)
        except:
            await message.channel.send(
                "Invalid =ap <code>. Use =aplist to view a list of valid AP courses and corresponding codes")

    if message.content.lower().startswith("=kkiaw"):
        AP_CONSTANT = 0
        await message.channel.send("https://gph.is/g/aj12k9B")

    if message.content.lower().startswith("=works"):
        AP_CONSTANT = 0
        randomNumWorks = randrange(len(IT_WORKS_GIFS))
        while randomNumWorks == RANDOMCONSTANTWORKS:
            randomNumWorks = randrange(len(IT_WORKS_GIFS))
        RANDOMCONSTANTWORKS = randomNumWorks
        await message.channel.send(IT_WORKS_GIFS[randomNumWorks])

    if message.content.lower().startswith("=happy"):
        AP_CONSTANT = 0
        randomNumHappy = randrange(len(HAPPY_GIFS))
        while randomNumHappy == RANDOMCONSTANTHAPPY:
            randomNumHappy = randrange(len(HAPPY_GIFS))
        RANDOMCONSTANTHAPPY = randomNumHappy
        await message.channel.send(HAPPY_GIFS[randomNumHappy])

    if message.content.lower().startswith("=stab"):
        AP_CONSTANT = 0
        randomNumStab = randrange(len(STAB_GIFS))
        while randomNumStab == RANDOMCONSTANTSTAB:
            randomNumStab = randrange(len(STAB_GIFS))
        RANDOMCONSTANTSTAB = randomNumStab
        await message.channel.send(STAB_GIFS[randomNumStab])

    if message.content.lower().startswith("=gp") or message.content.lower().startswith("=gopack"):
        AP_CONSTANT = 0
        randomNumGP = randrange(len(GO_PACK_GIFS))
        while randomNumGP == RANDOMCONSTANTGOPACK:
            randomNumGP = randrange(len(GO_PACK_GIFS))
        RANDOMCONSTANTGOPACK = randomNumGP
        await message.channel.send(GO_PACK_GIFS[randomNumGP])

    if message.content.lower().startswith("=sad") or message.content.lower().startswith("=cry"):
        AP_CONSTANT = 0
        randomNumSad = randrange(len(SAD_GIFS))
        while randomNumSad == RANDOMCONSTANTSAD:
            randomNumSad = randrange(len(SAD_GIFS))
        RANDOMCONSTANTSAD = randomNumSad
        await message.channel.send(SAD_GIFS[randomNumSad])

    if message.content.lower().startswith("=bear"):
        AP_CONSTANT = 0
        randomNumBear = randrange(len(BEAR_GIFS))
        while randomNumBear == RANDOMCONSTANTBEAR:
            randomNumBear = randrange(len(BEAR_GIFS))
        RANDOMCONSTANTBEAR = randomNumBear
        await message.channel.send(BEAR_GIFS[randomNumBear])

    if message.content.lower().startswith("=vsco"):
        AP_CONSTANT = 0
        randomNumVsco = randrange(len(VSCO_GIFS))
        while randomNumVsco == RANDOMCONSTANTVSCO:
            randomNumVsco = randrange(len(VSCO_GIFS))
        RANDOMCONSTANTVSCO = randomNumVsco
        await message.channel.send(VSCO_GIFS[randomNumVsco])

    if message.content.lower().startswith("=egirl"):
        AP_CONSTANT = 0
        randomNumEgirl = randrange(len(EGIRL_GIFS))
        while randomNumEgirl == RANDOMCONSTANTEGIRL:
            randomNumEgirl = randrange(len(EGIRL_GIFS))
        RANDOMCONSTANTEGIRL = randomNumEgirl
        await message.channel.send(EGIRL_GIFS[randomNumEgirl])

    if message.content.lower().startswith("=smug"):
        AP_CONSTANT = 0
        randomNumSmug = randrange(len(SMUG_GIFS))
        while randomNumSmug == RANDOMCONSTANTSMUG:
            randomNumSmug = randrange(len(SMUG_GIFS))
        RANDOMCONSTANTSMUG = randomNumSmug
        await message.channel.send(SMUG_GIFS[randomNumSmug])

    if message.content.lower().startswith("=merk"):
        AP_CONSTANT = 0
        await message.channel.send("https://tenor.com/view/weezer-riverscuomo-shook-shock-what-gif-13347829")

    if message.content.lower().startswith("=bey"):
        AP_CONSTANT = 0
        await message.channel.send("https://gph.is/g/aj10j9n")

    if message.content.lower().startswith("=slap"):
        AP_CONSTANT = 0
        randomNumSlap = randrange(len(SLAP_GIFS))
        while randomNumSlap == RANDOMCONSTANTSLAP:
            randomNumSlap = randrange(len(SLAP_GIFS))
        RANDOMCONSTANTSLAP = randomNumSlap
        await message.channel.send(SLAP_GIFS[randomNumSlap])

    if message.content.lower().startswith("=punch"):
        AP_CONSTANT = 0
        randomNumPunch = randrange(len(PUNCH_GIFS))
        while randomNumPunch == RANDOMCONSTANTPUNCH:
            randomNumPunch = randrange(len(PUNCH_GIFS))
        RANDOMCONSTANTPUNCH = randomNumPunch
        await message.channel.send(PUNCH_GIFS[randomNumPunch])

    if message.content.lower().startswith("=kick"):
        AP_CONSTANT = 0
        randomNumKick = randrange(len(KICK_GIFS))
        while randomNumKick == RANDOMCONSTANTKICK:
            randomNumKick = randrange(len(KICK_GIFS))
        RANDOMCONSTANTKICK = randomNumKick
        await message.channel.send(KICK_GIFS[randomNumKick])

    if message.content.lower().startswith("=hug"):
        AP_CONSTANT = 0
        randomNumHug = randrange(len(HUG_GIFS))
        while randomNumHug == RANDOMCONSTANTHUG:
            randomNumHug = randrange(len(HUG_GIFS))
        RANDOMCONSTANTHUG = randomNumHug
        await message.channel.send(HUG_GIFS[randomNumHug])

    if message.content.lower().startswith("=hairflip") or message.content.lower().startswith("=hf"):
        AP_CONSTANT = 0
        randomNumHF = randrange(len(HAIR_FLIP_GIFS))
        while randomNumHF == RANDOMCONSTANTHAIRFLIP:
            randomNumHF = randrange(len(HAIR_FLIP_GIFS))
        RANDOMCONSTANTHAIRFLIP = randomNumHF
        await message.channel.send(HAIR_FLIP_GIFS[randomNumHF])

    if message.content.lower() == "=todo" or message.content.lower() == "=td":
        AP_CONSTANT = 0
        randomColor = randrange(len(EMBED_COLORS))
        if message.author.id in toDoListDict:
            editingDict = toDoListDict[message.author.id]
            toDoListDict[message.author.id] = toDoDictEdit(editingDict)
            embedToDo = discord.Embed(
                title=message.author.name + "'s To-Do List",
                description=toDoPrintDict(dictionary=toDoListDict[message.author.id]),
                colour=EMBED_COLORS[randomColor]
            )
            await message.channel.send(embed=embedToDo)
        else:
            toDoListDict[message.author.id] = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: ''}
            await message.channel.send(
                "Set up your personal To-Do list. You do not have anything in your To-Do list yet. Type =add <item> to add something.")

            toDoWrite("todolist.txt")
            file_metadata = {'name': 'todolist.txt'}

            media = MediaFileUpload('todolist.txt',
                                    mimetype='text/plain')

            file = SERVICE.files().create(body=file_metadata,
                                          media_body=media,
                                          fields='id').execute()

            SERVICE.files().delete(fileId=driveFiles['todolist.txt']).execute()

            driveFiles['todolist.txt'] = file.get('id')

            if os.path.exists("todolist.txt"):
                os.remove("todolist.txt")
            else:
                print("The file does not exist")

    if message.content.lower().startswith("=add "):
        AP_CONSTANT = 0
        if message.author.id not in toDoListDict:
            await message.channel.send("You do not have a list set up yet, type =todo to set up")
            return
        if "|" in message.content[5:] or '\n' in message.content:
            await message.channel.send("Item contains an invalid character try again")
            return
        if len(message.content[5:]) > 100:
            await message.channel.send("Item is too long")
            return
        else:
            i = 1
            count = 1
            while i < 11:
                if str(toDoListDict[message.author.id][i]) != '' and str(toDoListDict[message.author.id][i]) != '\n':
                    count += 1
                i += 1
            if count == 11:
                await message.channel.send("Your To-Do list is full, check some stuff off before adding more items! "
                                           "Use =check <item number> to check items off.")
                return
            if count < 11:
                toDoListDict[message.author.id][count] = message.content[5:]
                await message.channel.send(
                    "Added \"" + message.content[5:] + "\" to position number " + str(count) + " in your To-Do list")
                editingDict = toDoListDict[message.author.id]
                toDoListDict[message.author.id] = toDoDictEdit(editingDict)

                toDoWrite("todolist.txt")
                file_metadata = {'name': 'todolist.txt'}

                media = MediaFileUpload('todolist.txt',
                                        mimetype='text/plain')

                file = SERVICE.files().create(body=file_metadata,
                                              media_body=media,
                                              fields='id').execute()

                SERVICE.files().delete(fileId=driveFiles['todolist.txt']).execute()

                driveFiles['todolist.txt'] = file.get('id')

                if os.path.exists("todolist.txt"):
                    os.remove("todolist.txt")
                else:
                    print("The file does not exist")

    if message.content.lower().startswith("=check "):
        if message.author.id not in toDoListDict:
            await message.channel.send("You do not have a list set up yet, type =todo to set up")
        check = 0
        numItems = numItemsInToDoList(toDoListDict[message.author.id])
        try:
            check = int(message.content[7:])
        except:
            await message.channel.send("You are checking off an invalid item, could not check off item. Check off an "
                                       "item by doing =check <number>")
            return

        if check < 1 or check > numItems:
            await message.channel.send("You are checking off an invalid item, could not check off item")
            return

        else:
            checkedMsg = toDoListDict[message.author.id][check]
            toDoListDict[message.author.id][check] = ''
            toDoListDict[message.author.id] = toDoDictEdit(toDoListDict[message.author.id])
            await message.channel.send(
                "Checked off item number " + str(check) + " \"" + str(checkedMsg) + "\"" + ". Good Job!")

            toDoWrite("todolist.txt")
            file_metadata = {'name': 'todolist.txt'}

            media = MediaFileUpload('todolist.txt',
                                    mimetype='text/plain')

            file = SERVICE.files().create(body=file_metadata,
                                          media_body=media,
                                          fields='id').execute()

            SERVICE.files().delete(fileId=driveFiles['todolist.txt']).execute()

            driveFiles['todolist.txt'] = file.get('id')

            if os.path.exists("todolist.txt"):
                os.remove("todolist.txt")
            else:
                print("The file does not exist")

    if message.content.lower() == "=word":
        randomColor = randrange(len(EMBED_COLORS))
        AP_CONSTANT = 0
        randomNumWord = randrange(len(wordsDict))
        while randomNumWord == RANDOMCONSTANTWORD:
            randomNumWord = randrange(len(wordsDict))
        RANDOMCONSTANTWORD = randomNumWord
        word = wordsDict[randomNumWord + 1]
        splitWords = word.split('\n')
        definition = ''
        i = 1
        while i < len(splitWords):
            definition += str(splitWords[i]) + "\n"
            i += 1
        embedWord = discord.Embed(
            title="Definition of " + str(splitWords[0]),
            description=definition,
            colour=EMBED_COLORS[randomColor]
        )
        embedWord.set_footer(text="Requested by: " + str(message.author.name))
        await message.channel.send(embed=embedWord)

    if message.content.lower() == "=foodlist" or message.content.lower() == '=fl':
        AP_CONSTANT = 2
        page1food.set_footer(
            text="Requested by: " + message.author.name + "\n")
        page2food.set_footer(
            text="Requested by: " + message.author.name + "\n")
        page3food.set_footer(
            text="Requested by: " + message.author.name + "\n")
        page4food.set_footer(
            text="Requested by: " + message.author.name + "\n")

        msg = await message.channel.send(embed=page1food)

        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')
        await msg.add_reaction('4️⃣')

    if message.content.lower().startswith("=rfood "):
        AP_CONSTANT = 0
        try:
            messageStr = message.content[7:]
            messageList = messageStr.split(" ")

            code = int(messageList[0])
            rate = int(messageList[1])

            if code < 100 or code > 135:
                await message.channel.send("Code must be inbetween 100 and 135, type =foodlist to see all codes")
                return

            if rate < 1 or rate > 10:
                await message.channel.send("Ratings must be inbetween 1 and 10")
                return

            name = foodDict[code][0]

            pplVal = int(foodDict[code][2])
            pplVal += 1

            rateVal = float(foodDict[code][3])
            rateVal += rate
            newRate = rateVal / pplVal

            newList = [name, str(newRate), str(pplVal), str(rateVal)]
            if code == 105:
                newList = [name, str(100), str(pplVal), str(100)]

            foodDict[code] = newList

            await message.channel.send("Added your rating!")

            foodWrite("food.txt")
            file_metadata = {'name': 'food.txt'}

            media = MediaFileUpload('food.txt',
                                    mimetype='text/plain')

            file = SERVICE.files().create(body=file_metadata,
                                          media_body=media,
                                          fields='id').execute()

            SERVICE.files().delete(fileId=driveFiles['food.txt']).execute()

            driveFiles['food.txt'] = file.get('id')

            if os.path.exists("food.txt"):
                os.remove("food.txt")
            else:
                print("The file does not exist")

        except:
            await message.channel.send("Invalid code, type =foodlist to view all possible codes")

    if message.content.lower().startswith("=food "):
        AP_CONSTANT = 0
        code = 0
        randomColor = randrange(len(EMBED_COLORS))
        try:
            code = int(message.content[6:])

            if code < 100 or code > 135:
                await message.channel.send("Invalid code, type =foodlist to view all possible codes")
                return

            foodEmbed = discord.Embed(
                title=foodDict[code][0],
                description='**Rated:** ' + foodDict[code][1] + " / 10",
                colour=EMBED_COLORS[randomColor]
            )
            if foodDict[code][2] == str(1):
                foodEmbed.set_footer(text="Rated by " + foodDict[code][2] + " person")
            else:
                foodEmbed.set_footer(text="Rated by " + foodDict[code][2] + " people")
            await message.channel.send(embed=foodEmbed)

        except:
            await message.channel.send("Invalid code, type =foodlist to view all possible codes")
            return

    if message.content.lower() == "=maudy":
        AP_CONSTANT = 0
        await message.channel.send("https://youtu.be/H3CgD29T6lQ")

    if message.content.startswith('=join'):
        channel = message.author.voice.channel
        print(channel)
        await channel.connect()


# with open('wordsWithDefs.txt') as fin, open('newfile.txt', 'w') as fout:
#    for line in fin:
#        fout.write(line.replace('\t', ''))

@client.event
async def on_reaction_add(reaction, user):
    global AP_CONSTANT
    if reaction.emoji == '1️⃣' and reaction.count == 2 and AP_CONSTANT == 1:
        await reaction.message.edit(embed=page1)
        await reaction.remove(user)
    if reaction.emoji == '2️⃣' and reaction.count == 2 and AP_CONSTANT == 1:
        await reaction.message.edit(embed=page2)
        await reaction.remove(user)
    if reaction.emoji == '3️⃣' and reaction.count == 2 and AP_CONSTANT == 1:
        await reaction.message.edit(embed=page3)
        await reaction.remove(user)
    if reaction.emoji == '4️⃣' and reaction.count == 2 and AP_CONSTANT == 1:
        await reaction.message.edit(embed=page4)
        await reaction.remove(user)

    if reaction.emoji == '1️⃣' and reaction.count == 2 and AP_CONSTANT == 2:
        await reaction.message.edit(embed=page1food)
        await reaction.remove(user)
    if reaction.emoji == '2️⃣' and reaction.count == 2 and AP_CONSTANT == 2:
        await reaction.message.edit(embed=page2food)
        await reaction.remove(user)
    if reaction.emoji == '3️⃣' and reaction.count == 2 and AP_CONSTANT == 2:
        await reaction.message.edit(embed=page3food)
        await reaction.remove(user)
    if reaction.emoji == '4️⃣' and reaction.count == 2 and AP_CONSTANT == 2:
        await reaction.message.edit(embed=page4food)
        await reaction.remove(user)


@client.event
async def on_member_join(member):
    if member.guild.id == 713912979061473280:
        c = member.guild.get_channel(713913856912654367)
        await member.guild.get_channel(713912979606863953).send(member.mention + " listen to "
                                                                                 "https://youtu.be/H3CgD29T6lQ and "
                                                                                 "check out " + c.mention + " and "
                                                                                                            "subscribe to El maudy on YouTube. \nI hope you enjoy your stay!")

    if member.guild.id == 670368584220016641:
        roles = member.guild.get_channel(670413619468435473)
        depRoles = member.guild.get_channel(708804770885795840)
        pingRoles = member.guild.get_channel(708059040017547324)
        colorRoles = member.guild.get_channel(691440197836996629)
        abtYou = member.guild.get_channel(670388513891418112)
        genUnverified = member.guild.get_channel(670509821287727124)
        verfVid = member.guild.get_channel(708439253117435934)

        await member.guild.get_channel(670403345470586902).send(
            "---------------------------------------- \n" + member.mention + " Welcome to The Brickyard, an unofficial NCSU discord server. "
                                                                             "\n\n**3 simple steps to "
                                                                             "gain access to rest of the "
                                                                             "server:**\n\n**1. Fill out your** " +
            roles.mention + ", " + depRoles.mention + ", and" + pingRoles.mention + "*by starting from the top and "
                                                                                    "reacting with emojis.*\n**2. ["
                                                                                    "Optional]** *Share things in* " +
            abtYou.mention + " *(no names necessary) and* " + colorRoles.mention + "\n**3. Kindly Ping Admin or Mod** "
                                                                                   "*for verification in* " +
            genUnverified.mention + "\n\nSee" + verfVid.mention + " *for help.*\n\nWe currently have " +
            str(member.guild.member_count) + " members!\n---------------------------------------")

    if member.guild.id == 690120170290544665:
        await member.guild.get_channel(690123955578994822).send("Welcome to DEFFEKT Repository " +  member.mention + "! Take a look around and don't forget to read the pins! ")


client.run('TOKEN')
