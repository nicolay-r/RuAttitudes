# RuAttitudes 2.0

**RuAttitudes** -- is a collection of automatically labeled sentiment attitudes,
which is developed using **distant supervision** (DS) approach.
It is considered as an application for machine learning model training.
This repository provides a collection and **reader** (written in Python).

![](images/flow.png)
> News processing workflow, version 2.0 [[code]](https://github.com/nicolay-r/frame-based-attitude-extraction-workflow/tree/v2.0)

## Download

[RuAttitudes-2.0-Base (2.8 mln. news processed)](https://www.dropbox.com/s/y39vqzzjumqhce1/ruattitudes_20_base.zip?dl=1)

[RuAttitudes-2.0-Large (8.8 mln. news processed)](https://www.dropbox.com/s/43iqoxlyh38qk8u/ruattitudes_20_large.zip?dl=1)

# Contents
* [Format Description](#quick-start-format-description)
* [Reader](#collection-reader) ![](https://img.shields.io/badge/Python-3.6-brightgreen.svg)
* [References](#references)

## Format Descriptions

See the following [documentation](docs/Format.md).

## Collection Reader 

![](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

Folder `reader` contains a collection reader (source file parsers), written in Python-3.6.

Please refer to [read.py](read.py), as it provides an example of how this collection could be parsed/readed.


## References
```
@inproceedings{rusnachenko2021language,
    title={Language Models Application in Sentiment Attitude Extraction Task},
    author={Rusnachenko, Nicolay},
    booktitle={Proceedings of the Institute for System Programming of the RAS (Proceedings of ISP RAS), vol.33},
    year={2021},
    number={3},
    pages={199--222},
    authorvak={true},
    authorconf={false},
    language={russian}
}

