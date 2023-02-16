import re
from pathlib import Path
import spacy
from collections import Counter
from itertools import chain


# Compile a regex that captures the text between two quotes.
# These can be smart (”I am a quote”) or normal ("I am a quote") quote characters.
# the quoted text can span multiple lines

quote_regex = re.compile(r"[“\"](.+?)[”\"]", flags=re.S | re.MULTILINE)

nlp = spacy.load("en_core_web_md")

text_dialogue = Path(
    "data/txt/dialogue/1937.Steinbeck.Am.M.Of_Mice_and_Men.ascii.txt.dialogue.txt"
).read_text()

docs_dialogue = list(
    nlp.pipe(i.group() for i in re.finditer(quote_regex, text_dialogue))
)

# common ents
Counter(
    chain.from_iterable([[t.text for t in doc.ents] for doc in docs_dialogue])
).most_common(10)


text_narration = Path(
    "data/txt/narration/1937.Steinbeck.Am.M.Of_Mice_and_Men.ascii.txt.narration.txt"
).read_text()


docs_narration = list(nlp.pipe((i.strip() for i in text_narration.split("\n\n"))))

# common ents
Counter(
    chain.from_iterable([[t.text for t in doc.ents] for doc in docs_narration])
).most_common(10)
