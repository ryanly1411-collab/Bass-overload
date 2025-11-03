# Setup
from earsketch import *
init()
setTempo(128)  # Typical EDM tempo similar to Clarity by Zedd
# Song Structure 
Intro = 1
Chorus = 17
Bridge = 29.5
Chorus2 = 48

#Intro
# Aiming to create an atmospheric vibe for the intro of the song
# Variables
pad1 = YG_EDM_PAD_5
kick1 = YG_EDM_KICK_1
fitMedia(pad1,1, 1, 15)
fitMedia(kick1, 2, 5, 15)
# Lower the sound of the background pad
setEffect(1, VOLUME, GAIN, 5)
setEffect(1, PAN, LEFT_RIGHT, 1.5, 100, 2.5)
# Add a fade in effect for the kick
setEffect(2, VOLUME, GAIN, -35, 5, 0, 8)
# Add a panning noise effect for the piano before the intro ends
setEffect(2, PAN, LEFT_RIGHT, 1.5, 100, 2.5)
# Slowly fade pad background noise to prepare for verse
setEffect(1, VOLUME, GAIN, 5, 15, -35)

# Verse
# Variables
synth1 = YG_EDM_SYNTH_LEAD_3
synthbuildup = YG_EDM_SNARE_BUILDUP_1
fitMedia(synth1, 3, 13, 17)
fitMedia(synthbuildup, 4, 13, 17)
# Add synthbuildup for chorus. Start from quiet to loud.
setEffect(4, VOLUME, GAIN, -55, 13, 0, 17)

#Chorus
# Variables
arp1 = YG_ELECTRO_ARP_2 # Main EDM melody for the chorus
synth1 = Y14_ELECTRO_2 # Background synth for hardstyle effect
kick1 = YG_EDM_KICKS_1 # Background kick
kick2 = RYANLYY_HARDSTYLE_KICK1 # Uploaded own sound
vocals1 = AK_UNDOG_VOCAL_BELT_6 # Vocal belt before chorus starts to fill in the empty spot
hihat1 = YG_ALT_POP_HIHAT_1
fitMedia(arp1, 6, 17.5, 29.5)
fitMedia(kick1, 7, 17.5, 28)
fitMedia(kick2, 8, 17.5, 28)
fitMedia(vocals1, 9, 16.5, 17.5) 
fitMedia(synth1, 10, 17.5, 28)
fitMedia(hihat1, 11, 17.5,33)
setEffect(10, VOLUME, GAIN, -10) # Lower sound of background synth
setEffect(8, VOLUME, GAIN, -15) # Lower the sound of the background kicks so we can hear the main beat better.
setEffect(11, VOLUME, GAIN, -20) # Lower the sound of background hihat sound. 


# Bridge
# Variables
drop = RD_POP_SFX_NOISEDROP_1 # SFX drop after first chorus
pad = YG_ELECTRO_PAD_1 # Same pad used in intro
vocals1 = DKBEAR_FREE_VOX_VERSE_2A # First part of the vocals verse
vocals2 = DKBEAR_FREE_VOX_VERSE_2B # Second part of the vocals verse
kick1 = YG_EDM_KICKS_2 # Background kick 
fxbuildup = YG_EDM_FX_11 # Buildup sfx before second chorus begins
setTempo(90, 30, 128, 38) # Slow down tempo after chorus
fitMedia(drop, 12, 28.5, 30.5)
fitMedia(pad, 13, 30, 47)
setEffect(13, VOLUME, GAIN, -30, 30, -10, 36) # Slowly introduce back music after the chorus by starting quiet 
setEffect(14, VOLUME, GAIN, -50, 30, -5, 36) # lower the voice of vocals so the background music can stand out more 
setEffect(15, VOLUME, GAIN, -5)
fitMedia(vocals1, 14, 31, 39)
fitMedia(vocals2, 15, 39, 47)
fitMedia(kick1, 16, 34, 47)
setEffect(16, VOLUME, GAIN, -10) # Lower the sound of the background kick
fitMedia(fxbuildup, 17, 46, 49)
setEffect(17, VOLUME, GAIN, -10)

# Chorus 2
# Variables
vocals1 = DKBEAR_FREE_VOX_CHORUS_1 # Chorus part 1
vocals2 = DKBEAR_FREE_VOX_CHORUS_2 # Chorus part 2
vocals3 = DKBEAR_FREE_TALK_NEED_TO # Vocal audio to fill in the quiet section before the second chorus
arp1 = YG_ELECTRO_ARP_2 # Melody in the background used in the first chorus earlier
pad1 = YG_EDM_PAD_1 # Pad in the bridge for supporting background ambience
drop1 = RD_TRAP_SFX_NOISEDROP_1 # SFX drop after the chorus to end the song
kick1 = YG_EDM_KICK_3 # Background kick for EDM genre feel. 
fitMedia(vocals3, 18, 48, 49.75)
fitMedia(vocals1, 19, 49.75, 57.75)
setEffect(19, VOLUME, GAIN, -15, 50, -5, 52) # Lower the sound of the vocals from the start of the chorus
fitMedia(vocals2, 20, 57.75, 65.75)
fitMedia(arp1, 21, 49.75, 65)
setEffect(21, VOLUME, GAIN, -10) # Lower the sound of the arp so the vocals stand out more 
fitMedia(pad1, 22, 49.75, 69)
setEffect(22, VOLUME, GAIN, -5) # Lower the sound of the background pad so vocals stand out more
fitMedia(kick1, 23, 49.75, 65)
fitMedia(drop1, 24, 64, 68) # Drop sfx to finish off the song 


