# text-register-analyzer
Provides data about linguistic characteristics of a group of text files.

For this project I tried to pick characteristics that could help me differentiate between texts of differing registers. 

Two of the functions were executed similarly, as both discourse markers and first person pronouns are both banks of words to identify. I simply used NLTK to tokenize the texts and then counted the number of instances in which the token matched a word from the sets I had created. Typing this now, I realize that some of the discourse markers in my set were actually phrases so I'll have to change my program and implement that function differently if I want to have accurate counts.

The contractions were a little trikier. I found a regex that would find apostrophes with letters immediately on both sides, then ran that on the raw text to count the number of matches.
