# Project Timeline

Sticking with [my initial idea](https://github.com/artintelclass/final-andrjjr/blob/master/brainstorm.md) of training Magenta ML models on datasets of MIDI data for VST sample & preset libraries focused on creating [techno music](https://www.youtube.com/watch?v=ZdBWMA9M7xQ), here is an outline of how I see the project going:

1) Collect MIDI drum loops and synth loops from sample libraries. Starting point will be the [Sample Magic: Berlin Techno Drum kit](https://www.samplemagic.com/details/1875/midi-elements-berlin-techno-drums). This contains 101 MIDI samples and other .WAV loops. Melodic synth parts can be converted to MIDI fairly easily, if not already in that format, using Ableton Live's 'Create MIDI from Audio' feature.
2) Format the MIDI data as necessary to work with Magenta's Drum-RNN model. [See here](https://github.com/tensorflow/magenta/tree/master/magenta/models/drums_rnn) and [here](https://github.com/tensorflow/magenta/blob/master/magenta/scripts/README.md)
3) Figure out how to, and then train Nsynth using samples in preset libraries. See whether if by mixing different preset sounds, I am able to generate sound material that is significantly different and/or interesting as compared to the existing samples. Alternatively, or in addition to this, do mixing of both drum samples and synth samples with samples of my own - in order to customise the existing presets.
4) There are some additional features I would like to try to implement, with respect to the rhythmic content, using Magenta's VAE such as maybe using to give some long-term structure to the output compositions. 
5) Once these models have been trained, I will need to generate a lot of new material from them, and see whether it is usbale in a musically interesting way. If so, I will go on to produce a short selection of tracks that combines the material generated from these processes and Modular synthesizers as well. 


