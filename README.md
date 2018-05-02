
# Recurrent Neural Rhythm Vol. 1 - A.rt I.ntel Final Project

![cover](https://github.com/artintelclass/final-andrjjr/blob/master/images/Screen%20Shot%202018-05-02%20at%208.28.51%20AM.png)

### Prompt
*The project should be a creative use of machine learning. It should be more ambitious in scope compared to what we've done so far this semester.*

## Background

This project was always, in one way or another, about how we engage with the techology we use in creative endeavours. Do the endless digital tools at our disposal augment or hinder our creative capacities? This is what I hoped to explore in the context of machine learning. 

Initially, my project was going to focus audio and MIDI sample libraries, and their power to instantly recreate certain styles and genres. I find this idea quite problematic, because really, it places us into a creatively inhibiting relationship with technology. On top of that, what results is a large body of homogenous and undifferentiated musical output. 

You can read more about my initial ideas [here](https://github.com/artintelclass/final-andrjjr/blob/master/brainstorm.md).

## Process

Initially, I planned to train a recurrent neural net model ([Magenta's Drums-RNN](https://github.com/tensorflow/magenta/tree/master/magenta/models/drums_rnn)), long short-term memory RNN, on my own set of MIDI data. This proved to be difficult for many reasons. When I had [finally managed to get this working](https://github.com/artintelclass/final-andrjjr/blob/master/project_log.md), and tried training on my own data, the results were far from interesting. The model in fact generated the exact same rhtyhmic output each time. 

I then shifted gears a little bit, and instead of trying to train my own model, I focused on how to engage with Drums-RNN's pre-trained model. My initial idea had been to train a model on a corpus of electronic dance music rhythmic MIDI data, and then see how to inject mutations and customizations into the output, but training my own dataset wasn't really necessary to do this, as the existing one worked quite well. 

So instead I used very specific priming drum tracks in order to influence the kinds of rhythms that the model would generate. I transcribed drum notation that I found online into the format that the model understands, and then generated 10 rhythmic tracks for each primer, at 64, 128, and 256 instances long. 

**Shakara notation from [here](http://afrobeatdrummingexplained.blogspot.com/).**
![shakara_notation](https://github.com/artintelclass/final-andrjjr/blob/master/images/Screen%20Shot%202018-05-02%20at%209.51.45%20AM.png)

**Transcription to primer notation.**
![shakara_primer](https://github.com/artintelclass/final-andrjjr/blob/master/images/Screen%20Shot%202018-05-02%20at%209.54.08%20AM.png)

The eureka moment then arrived, as I listened to the outputs that the model generated. It was incredible to hear the DNA of those primer tracks still throughout, but in such a twisted and maligned form. Although there was so much output already, all I could see was more possibility. This material was certainly interesting, and diverse, but it needed attention.

## ... More Than The Push of a Button

This is where I saw that this would be a collaboration. The ML provides a lot of very interesting material, and inspiration. But as interesting as that material was, it was only a starting point. It was now up to me to take this material, transform it, and create something more meaningful out of it. And this requirement was what made the process so engaging in my opinion. It was so far off from the idea of pushing a button and the computer giving a polished, finished output. Even if it could do that, this project has shown me that there would be no purpose or interest in that. 

## The Content

Let me talk a bit about the music itself. I mentioned the primer drum tracks earlier. Although the model was trained on a *non-genred* set of data, the use of primers of a specific style influenced the rhythms it generated. I turned to Fela Kuti and Tony Allen, wanting at this point to step away from regular, 4/4 dominated rhythms of a lot of club and dance music, and also because I just really dig their music. I transcribed a bunch of afro-beat drum grooves into the format required by Drums-RNN, as well as a few other rhythmic blueprints for a bit of deviation.

Once the rhythms were generated, I listened to them and made rough sketches in Logic, cutting, splicing and recombining. Importanlty, I sometimes left the rhythms as they were, because again, it was about me *and* the machine. Some of its outputs were really incredible, and so I left them as is. 

I translated (MIDI note changes) the rhythms to work as a djembe rather than a standard kit. The sound palette is inspired by my experience with African marimba, and love of electronic textures. I must mention the outstanding [Nihiloxica](https://www.youtube.com/watch?v=3lauecmaa3Y) which certainly inspired the energy and hybridity of this tape.

## The Result

The final result is a 4 track tape. The tracks (RHYTHM 01 through 04), are presented in the order they were created. Side A contains more *raw* rhtyhmic outputs from the neural net, while Side B is more explorative, reducing the material to smaller chunks, and introducing more elements apart from the djembe, such as synths and marimba and balafon. The idea is that the arc of the tracks traces my arc of dealing with these generated rhythms, presenting both their innate qualities, and their potential as source material. 

I recorded the tracks to tape, because I'm a sucker for physical media. I would press it to vinyl for the bigger artwork but that wasn't possible. I am curious how the sound quality degrades over time and whethet that will add or detract to the listening experience. 

![tape_1](https://github.com/artintelclass/final-andrjjr/blob/master/images/IMG_6865.JPG)
![tape_3](https://github.com/artintelclass/final-andrjjr/blob/master/images/IMG_6867.JPG)
![tape_4](https://github.com/artintelclass/final-andrjjr/blob/master/images/IMG_6868.JPG)
![tape_5](https://github.com/artintelclass/final-andrjjr/blob/master/images/IMG_6869.JPG)

The casette insert contains some text about the project. The images are of djembe drums, and the diagram is a [long short-term memory (LSTM)](https://en.wikipedia.org/wiki/Long_short-term_memory) recurrent neural network - the kind that **Drums-RNN** uses. 

Finally, you can [stream the EP online](https://soundcloud.com/peoplemachine/sets/recurrent-neural-rhythm-vol-1) if you don't happen to have a tape deck. 







