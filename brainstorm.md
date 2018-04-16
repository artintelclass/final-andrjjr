# ML Final Project Proposal

I have been thinking about how electronic music production is marketed and promoted a lot, especially with the existence of sound libraries, drum packages etc. that promise to give you the capacity to recreate certain styles and genres “in an instant.” I find this idea quite problematic, because really, it puts us in the situation where technology is inhibiting creativity rather than stimulating it, and on top of that, resulting in a large body of homogenous and undifferentiated musical output. I feel there are specific risks in the realm of musical styles like techno and other forms of electronic music, which are in any case more under scrutiny for being “machine” produced.

In line with the Magenta project’s own goal to give artistic capabilities to many people through machine learning, I will use some of the models from the Magenta Tensorflow Package to try and explore what are the possibilities for new sound and rhythmic content, specifically through the use of commercially available drums sample libraries.

Taking some inspiration from [here](https://medium.com/@snikolov/neuralbeats-generative-techno-with-recurrent-neural-networks-3824d7ba7972), of this guy who generated rhythms using LSTMs, I plan to:
1. train drum-RNN on a set of midi drum data from sample libraries. The set will depend on the required size of data, but I want to use something like this as a starting point
2. use Nsynth to generate “new” drum kit presets using combinations of existing drum samples from these packages, and audio samples of my own, as a way to personalise these prefabricated sounds

<a href="https://www.youtube.com/watch?v=rU2ieu5o5DQ" target="_blank"><img src="https://github.com/artintelclass/final-andrjjr/blob/master/0.jpg" 
alt="VIDEO" width="240" height="180" border="10" align="center"/></a>

## What I hope to see from this project

1.Can ML techniques yield interesting results in terms of sound samples, when combining presets and custom sounds. Will combining different sounds from within the presets themselves yield cool results? If successful, it can be a starting point for thinking about how producers/musicians use presets and sample libraries?

2.Can we subvert one of the possible negative effects of sample libraries i.e. reduce homogeneity of sound output, and put creative control in a musicians hands, rather than a company which designs the presets?

3.How well do these ML techniques work in situations where musical content is quite sparse and repetitive (formalised drum patterns, song structures)?
