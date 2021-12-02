import rdflib
from rdflib import Graph, URIRef, Literal, BNode
from google.cloud import translate
from os import environ

# Change the target language here and the postfix (e.g., http://www.radlex.org/RID/Preferred_name_Dutch)
LANG='nl'
LANG_POSTFIX='_Dutch'

project_id = environ.get("PROJECT_ID", "")
assert project_id
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient()

def do_translation(i, counter):
    i = str(i)
    response = client.translate_text(
        contents=[i],
        target_language_code=LANG,
        parent=parent,
    )
    if len(response.translations) == 0:
        return ''
    print(str(2412963-counter) + '. translate <>', i, 'to', response.translations[0].translated_text)
    return response.translations[0].translated_text

radlex_tree = rdflib.Graph()
radlex_tree.parse("RadLex.owl", format='application/rdf+xml')

counter = 0

for s, p, o in radlex_tree:
    if  p.n3() == '<http://www.radlex.org/RID/Preferred_name>' or \
        p.n3() == '<http://www.radlex.org/RID/Definition>' or \
        p.n3() == '<http://www.radlex.org/RID/Comment>':
            radlex_tree.add((s, URIRef(p.n3()[1:-1]+LANG_POSTFIX), Literal(do_translation(o, counter), lang='nl')))
            counter += len(o)

radlex_tree.serialize(destination="RadLex." + LANG + ".owl", format="xml")

print('counted', counter)
