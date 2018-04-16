I have been thinking about how electronic music production is marketed and promoted a lot, especially with the existence of sound libraries, drum packages etc. that promise to give you the capacity to recreate certain styles and genres “in an instant.” I find this idea quite problematic, because really, it puts us in the situation where technology is inhibiting creativity rather than stimulating it, and on top of that, resulting in a large body of homogenous and undifferentiated musical output. I feel there are specific risks in the realm of musical styles like techno and other forms of electronic music, which are in any case more under scrutiny for being “machine” produced.

In line with the Magenta project’s own goal to give artistic capabilities to many people through machine learning, I will use some of the models from the Magenta Tensorflow Package to try and explore what are the possibilities for new sound and rhythmic content, specifically through the use of commercially available drums sample libraries.

Taking some inspiration from [here](https://medium.com/@snikolov/neuralbeats-generative-techno-with-recurrent-neural-networks-3824d7ba7972), of this guy who generated rhythms using LSTMs, I plan to:
1. train drum-RNN on a set of midi drum data from sample libraries. The set will depend on the required size of data, but I want to use something like this as a starting point
2. use Nsynth to generate “new” drum kit presets using combinations of existing drum samples from these packages, and audio samples of my own, as a way to personalise these prefabricated sounds

[![VIDEO](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=rU2ieu5o5DQ)
