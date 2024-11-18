# Zirbo translator
translates sentence to multiple languages from command line using google translate api.

why?
normally you'd only check the language you see.
with this, you get multiple translations at once so you immediately see if anything funny is there,
plus, even if you don't, you kind of passively learn some stuff.

AAAAAAAAND: it works from the command line!

### prerequisite
pip3 install googletrans>=4.0.0rc1

##usage
```
./zirbotranslate.py "<text>" [-s source_language] [-t target_language]
```

the source language is optional, google translate will guess it if you don't specify;
but the guess might be wrong, plus if you give it it will speed up the query.

the target language forces the answer to be a single specific language.
this contradicts the idea of the script so i don't know why i ever implemented it.

## example
$ ./zirbotranslate.py "Your life burns faster, obey your master!" -s en
translating to all languages
from en to it:   La tua vita brucia più velocemente, obbedisci al tuo padrone!
from en to de:   Dein Leben brennt schneller, gehorche deinem Meister!
from en to fr:   Votre vie brûle plus vite, obéissez à votre maître!
from en to sr:   Твој живот је спалио брже, покоравајте се свом господару!
from en to hr:   Život vam brže gori, poslušajte svog gospodara!
from en to sl:   Vaše življenje hitreje gori, ubogate svojega gospodarja!
from en to cs:   Váš život hoří rychleji, poslouchejte svého pána!
