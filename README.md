# Tensorflow Lyrics Generator

Simple Tensorflow Lyrics Generator that generates lyrics at character level, given a seed phrase, and uses a spell checker to clean up resulting text. 
Trained from 7 Metallica songs, using LSTMs.

Run run.py to use the model...
```
python run.py
[...Tensorflow warnings]

============================
Enter seed phrase: Never will it mend
Never will it mend
now the truth of me
of live
all silence the exist
cannot kill the the family
battery
never
fire
to begin whipping one
no nothing no the matters breath
oh it so met mor the role me can see
and it just free the find
never will the time
nothing is the ear fire
truth wind to see
man me will the death
writing dawn aninimine in me
cannot justice the battery
pounding either as taken my stream
to the will is the existing there is bore
make it our lothenent
born one row the better the existing fro
============================

============================
Enter seed phrase: hold my battery of breath
hold my battery of breath of eyes to set death
oh straw hat your humanity
late the ust comes before but they su
never cared to be
i the estimate it life the lost fill dead
so red
so true
battery
no nothing life now i me crossing ftin
dare
so true myself in me
now pain i mean
so net would
to be
no ripped to are

so prmd

imply solute more is to you hear
taken my end
truth the within
 so let it be worth
tro finding
something
mutilation cancellation cancellation
austin
so let it be resting  spouses the stan

serve goth
============================
```

^ Real output from one of the trained models

Run train.py to train and save a new model...

```
python train.py
[Model trains....]
```


The model obviously does not produce a whole set of lyrics that make a whole lot of sense, but it manages to string together some short phrases. This could be improved by generating at word level instead or using technologies like GPT.