# RadLex machine translations

Machine translations for [RadLex radiology lexicon](http://radlex.org/) using the Google Translation API.

## Available languages

| Language | Filename | Native description |
| --- | --- | --- |
| Dutch / Nederlands | `RadLex.NL.owl` | Nederlandse machinevertalingen van RadLex-codes. Het OWM-XML bestand bevat Nederlandse machine vertalingen van de Radlex `<http://www.radlex.org/RID/Preferred_name>`, `<http://www.radlex.org/RID/Definition>` en `<http://www.radlex.org/RID/Comment>` nodes.| 

## Custom language translation

0. Download the latest [RadLex OWL](http://radlex.org/download/RadLex_OWL4.1.zip) (v4.1)
0. Follow [these](https://codelabs.developers.google.com/codelabs/cloud-translation-python3#0) API setup steps
0. `$ pip3 install -r requirements.txt`
0. `$ python3 translate.py`

The output file will look like: `RadLex.{LANG}.owl` and is in XML format.

## Example node

```xml
<rdf:Description rdf:about="http://www.radlex.org/RID/RID43011">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdfs:subClassOf rdf:resource="http://www.radlex.org/RID/RID42998"/>
    <FMAID>296521</FMAID>
    <Preferred_name xml:lang="en">segment of inferior glenohumeral ligament</Preferred_name>
    <Preferred_name_German xml:lang="de">Segment des unteren Ligamentum glenohumerale</Preferred_name_German>
    <rdfs:label xml:lang="en">RID43011</rdfs:label>
    <Preferred_name_Dutch xml:lang="nl">segment van het onderste glenohumerale ligament</Preferred_name_Dutch>
  </rdf:Description>
```

## Note

Note that the translations are done purely based on machine translations. You are responsible to determine if your use case (e.g., machine learning training) is sufficient to rely on them.