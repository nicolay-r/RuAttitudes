# RuAttitudes 1.0

**RuAttitudes** -- is a collection for machine learning model training. 
This repository provides a collection and **reader** (written in Python).
The collection has been developed and verbosely described in paper:

* "Distant Supervision for Sentiment Attitude Extraction" (RANLP'2019, Bulgaria, Varna)
[[paper]](),
[[poster]](https://github.com/nicolay-r/attitudes-extraction-ds/blob/master/docs/ranlp_2019_poster_portrait.pdf).

## Introduction

News articles often convey attitudes between the mentioned subjects, which is essential for understanding the described situation. 

This RuAttitudes is a result collection of an application of a new approach to distant supervision for **extracting sentiment attitudes 
between mentioned named entities in text**.

>**Example**: ``... **[USA]** is considering the possibility of new sanctions against 
    **[Russia]** ... ''. This context illustrates a negative **USA🠆Russia** attitude.
    
## How to Create a Training Set?

We use two different methods of sentiment attitude annotation, applied to the news title: 
* **Pair-Based** -- utilizing the [pre-assigned attitudes](https://github.com/nicolay-r/RuSentRel), 
organized in a list of pairs;
* **Frame-Based** -- utilizing frame entries from the 
[RuSentiFrames](https://github.com/nicolay-r/RuSentiFrames) 
lexicon.

We intersect the annotations and separate result: 
* With the **different** polarity according to both sources.
* With the **same** polarity -- is a result collection (RuAttitudes);

Figure below illustrates training collection development flow.

![](images/flow.png)


## Collection Reader ![](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

Folder `reader` contains a collection reader (source file parsers), written in Python-3.6.

Please refer to [read.py](read.py), as it provides an example of how this collection could be parsed/readed. 

## Application and Experiments

1. Application in Sentiment Attitude Classification Task of Analytical Articles, written in Russian
[[code-repository]](https://github.com/nicolay-r/attitudes-extraction-ds).

## References

> NOTE: This section will be updated since the related paper become available at aclweb.
