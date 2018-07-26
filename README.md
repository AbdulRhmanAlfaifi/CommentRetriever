## CommentRetriever
A python script to extract HTML comments from any webpage.
## Installation
Execute the following code in the terminal:
```
git clone https://github.com/AbdulRhmanAlfaifi/CommentRetriever.git
```
Then change the directory to CommentRetriever using this command:
```
cd CommentRetriever
```
Finally execute the program using the following command:
```
python CommentRetriever.py
```
## Usage
```
  Developed by AbdulRhman Alfaifi
  --------------------------------
  Usage : ./commentRetriever.py [options] website
  Example: ./commentRetriever.py www.google.com
  --------------------------------
  Options:
  --------------------------------
  -oX                Output XML formatted output.
  -w [FILE]                 Write the results to a file.
  -h                 Print this message.
  --------------------------------
  Contacts:
  --------------------------------
  Twitter            @A__ALFAIFI
  E-mail             a.alfaifi.14@gmail.com
```
## Example
Let's say we want to exteract all the comments from the following website:
```
www.github.com
```
Then we will execute the following command:
```
python CommentRetriever.py github.com
```
### Output
```
--------------------
 2 Comments Found.
--------------------
--------------------
 '"` 
--------------------
 </textarea></xmp> 
--------------------

```
