# poesi.as
Collection of poems, mostly Spanish, from the 21th century and before

Some stats:
* Number of poems: 25.187
* Number of words: 7.918.679

Two jsons are provided:

* [**`poesias_corpora.json`**](./poesias_corpora.json): This is the json used to generate the txt files.
* [**`poesias_corpora_old_spanish.json`**](./poesias_corpora_old_spanish.json): This json is still a work in progress. It has old Spanish poems made mostly by Alfonso X and they are not included in the corpora folder.

An additional CSV file, [`authors.csv`](./authors.csv), provides reconciled information for authors of the 20th Century and below. Identifiers (VIAF, BnF, BNE, LoC, ISNI), dates of birth and death, and gender, are also added as they appear in Wikidata.

Example of the structure of the json. the key is the original htm file on the poesi.as website:

* Json entry from http://poesi.as/ha-s061.htm

```python
{
    "ha-s061.htm":{
        "author":"Acuña,Hernando_de",
        "century":"<XXI",
        "title":"Ajeno_Fue,_Pues_Fue_Sólo_Un_Momento",
        "text":"Ajeno fue, pues fue sólo un momento,\ny mil años el mal sin acabarse;\ninstable fue, pues vino a comenzarse\nde nuevo el mal tras su contentamiento.\nPara más daño fue, pues su cimiento\ntan sin firmeza en mí pudo fundarse;\nque grave fue mi bien, pues en mostrarse\nal parecer fue bien y al ser tormento.\nBien pudieras, Amor, con tantos males\nacabarme de un golpe, pues podías\ncon uno y el menor de los que pruebo,\nsin juntar con mis penas, siendo tales,\nel bien que tuve por tan breves días,\npara nuevo dolor y caso nuevo.",
        "language":"es"
    }
}
```

This repo is a dump of the website www.poesi.as, we do not own the rights of any of the works pulished here.

For any violations or infringement of copyright, take proper action within the scope of the original website.

## Public Domain

The script [`extract.py`](./extract.py) generates a public domain corpus in JSON extracted from the corpus in poesi.as. The number of years since the death of an author needed for a work to be considered in the public domain can be specified using `-y YEARS` (`--years YEARS`). Defaults to 80 as per Spanish copyright laws.
```
$ python extract.py > public_domain.json
``
