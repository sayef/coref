#!/bin/bash
echo Downloading $1
wget -P $2 http://nlp.cs.washington.edu/pair2vec/$1.tar.gz
tar xvzf $2/$1.tar.gz -C $2
rm $2/$1.tar.gz
