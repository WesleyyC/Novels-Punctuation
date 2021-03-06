# Novels-Punctuation

Inspired by the medium post ["Punctuation in novels"](https://medium.com/@neuroecology/punctuation-in-novels-8f316d542ec4#.70eq88ybg), I start to wonder what it feels like to read something just with the punctual. No words, no number. Just punctuations.

So I write this python script in a cafe to help convert a PDF format reading into txt format only with the punctuation. 

### Setup
First we need to setup the pdf reading component by:
```
$ cd NoWords
$ python pdfminer/setup.py 
```

### Usage
To convert the file, do:
```
$ python NoWords.py <PATH TO THE PDF FILE> 

# for example
$ python NoWords.py sample/AAW.pdf

```
and the output txt file should be in the same path of the input file.

### Output as PDF?
I have tried to convert the txt to PDF directly in python, but it is not as nice as using Mac TextEditor to export PDF file. 
If you want to use the python pdf converter, you can set the following flag in `NoWords.py` to True:
```
pdf = False
```

### Let's look at [_Pride and Prejudice_](https://www.gutenberg.org/ebooks/1342) !

<img src="http://i.imgur.com/UbeBxCc.png?1" title="source: imgur.com"/>

