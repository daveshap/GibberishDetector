# GibberishDetector

Detecting gibberish as a type of sentiment analysis with GPT2.

## Objective

We would like to be able to automatically label passages based upon whether or not they make sense. 

| Passage | Label |
|---|---|
| My dog's name is George | Clean |
| Tree running twinkle bovine | Gibberish |
| Ai23k3k3k3 apple cart 213k3### | Gibberish |
| Sometimes I sneeze out an entire universe | Gibberish |


## Theory

Detecting whether or not a passage is grammatically and semantically sound is a complex task that requires two things:

- General knowledge about the world 
- A strong language model

Pretrained transformers, such as GPT, may contain embedded general knowledge about the world as well as language models. If this is true, it should be possible to adapt this technology to determine whether or not a passage 
makes sense. 

# Training Data

## Positive samples

Wikipedia articles will serve as ground truth for grammatically and semantically sound passages. We will label these `clean`. We can take entire articles as well as sentences and paragraphs from articles. 
Wikipedia carries several advantages, namely that it is crowdsourced and modern. Because of this, we will assume that Wikipedia articles represent the antithesis of gibberish.

## Negative samples

There are several methods we can use here. 

1. Modify the original training data
2. Synthesize completely random passages

For the first method, we will scramble word orders, inject random words, and transpose letters. This will create a sample that is close to making sense, but not quite. The second method will generate higher-entropy examples. 