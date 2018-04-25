# Project Timeline

Sticking with [my initial idea](https://github.com/artintelclass/final-andrjjr/blob/master/brainstorm.md) of training Magenta ML models on datasets of MIDI data for VST sample & preset libraries focused on creating [techno music](https://www.youtube.com/watch?v=ZdBWMA9M7xQ), here is an outline of how I see the project going:

1) Collect MIDI drum loops and synth loops from sample libraries. Starting point will be the [Sample Magic: Berlin Techno Drum kit](https://www.samplemagic.com/details/1875/midi-elements-berlin-techno-drums). This contains 101 MIDI samples and other .WAV loops. Melodic synth parts can be converted to MIDI fairly easily, if not already in that format, using Ableton Live's 'Create MIDI from Audio' feature.
2) Format the MIDI data as necessary to work with Magenta's Drum-RNN model. [See here](https://github.com/tensorflow/magenta/tree/master/magenta/models/drums_rnn) and [here](https://github.com/tensorflow/magenta/blob/master/magenta/scripts/README.md)
3) Figure out how to, and then train Nsynth using samples in preset libraries. See whether if by mixing different preset sounds, I am able to generate sound material that is significantly different and/or interesting as compared to the existing samples. Alternatively, or in addition to this, do mixing of both drum samples and synth samples with samples of my own - in order to customise the existing presets.
4) There are some additional features I would like to try to implement, with respect to the rhythmic content, using Magenta's VAE such as maybe using to give some long-term structure to the output compositions. 
5) Once these models have been trained, I will need to generate a lot of new material from them, and see whether it is usbale in a musically interesting way. If so, I will go on to produce a short selection of tracks that combines the material generated from these processes and Modular synthesizers as well. 

## MIDI Data and Formatting

To get things going, I pooled together a bunch of drum MIDI files (1143 files) to try and just play around with the drums_rnn model, and figure out how to prep the data and train a model. It turned out to be more nightmarish than expected. The [magenta GitHub](https://github.com/tensorflow/magenta/blob/master/magenta/scripts/README.md) has a useful overview of how to prep your dataset, but it's a bit sparse and didn't give too much detail about how the MIDI data needs to be formatted before any of those steps are taken. Online, resources in forums were equally limited. 

### The issue
The steps for creating the dataset involved:
1) Converting Midi in a directory into a **notesequences.tfrecord**
2) Creating the dataset (with a split of training and evaluation data) as 2 separate **.tfrecord files**

Step 2 is where I encountered a big problem, namely that that the NoteSequences that are generated are all empty files - 0kB! So my training obviously wasn't working on empty records.

Scouring the web, led me to two potential solutions. People mentioned that they had issues with their MIDI files containing double entries for time signature information, and that the channel of the MIDI files was not set to the right channel (Midi channel 9 for GM Drum kit).

I needed to visualise my midi files, to check these features in the files. Thankfully, there was a tool to do this - [MIDICSV](http://www.fourmilab.ch/webtools/midicsv/). Lo and behold, I had both double entries for time signature information in my files, and a channel number of 0 for all note_on and note_off events. 

![errors](https://github.com/artintelclass/final-andrjjr/blob/master/images/Screen%20Shot%202018-04-25%20at%2010.38.15%20AM.png)

Having the midi as .csv was helpful, but having thousands of MIDI files was not, so I had to automate the process. Given my limited (no) knowledge of Bash/Shell scripting, and my decent handle over Python, I wrote a script that runs on the directory of MIDI files, converting them all to CSV, performing the neccessary processing (*removing the second time_signature information* and *changing the MIDI channel of all events to channel 9*). The scripts are quite rudimentary, rely on a specific folder setup and have some annoying features, so not really usable outside my specific setup right now, **_but it works!_**. These scripts are in the repo for reference, and I'll note if I rework them to be a bit more usable. 

So, having done this, I was finally able to produce the required training_drum_tracks.tfrecord and eval_drum_tracks.tfrecord files. These are currently training. 

### Next?

This training set is not based on techno drum files exclusively, but a wide mix of whatever I could find. If this training works, I will then try doing a training on my small sample of specific techno files, and then on mixtures of these files with other specific genres to see if some interesting hybdrid combos emerge!


