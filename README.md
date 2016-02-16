# Novels-Punctuation

Inspired by the medium post ["Punctuation in novels"](https://medium.com/@neuroecology/punctuation-in-novels-8f316d542ec4#.70eq88ybg), I start to wonder what it feels like to read something just with the punctual. No words, no number. Just punctuations.

So I write this python script to help convert a PDF format reading into txt format only with the punctuation.

### Setup
First we need to setup the pdf reading component by:
```
$cd NoWords
$python pdfminer/setup.py 
```

### Usage
To convert the file, do:
```
$python NoWords.py <PATH TO THE PDF FILE> 
```
and the output txt file should be in the same path of the input file.

### Sample
To convert the file, do:
```
$python NoWords.py <PATH TO THE PDF FILE> 

# for example
$python NoWords.py sample/AAW.pdf

```
and the output txt file should be in the same path of the input file.
