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
<rdf:Description rdf:about="http://www.radlex.org/RID/RID49888">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdfs:subClassOf rdf:resource="http://www.radlex.org/RID/RID49887"/>
    <Comment>Recently, authors have subclassified comet-tail artifacts into small and large types and found a prevalence of malignancy of 15% in nodules that had echogenic foci with small comet-tail artifacts [12]. Conversely, when considering large comet-tail artifacts in cystic or partially cystic nodules, multiple studies have shown a strong association with benignity</Comment>
    <Created rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2015-11-18T00:00:00</Created>
    <Preferred_name xml:lang="en">comet-tail artifact (large)</Preferred_name>
    <Preferred_name_German xml:lang="de">Kometenschweifartefakt (groß)</Preferred_name_German>
    <Radlex_version_of_class_change>3.14</Radlex_version_of_class_change>
    <Source>TI-RADS</Source>
    <Synonym xml:lang="de">Kometenschweifartefakt (ausgeprägt)</Synonym>
    <rdfs:label xml:lang="en">RID49888</rdfs:label>
    <Preferred_name_Dutch xml:lang="nl">komeetstaartartefact (groot)</Preferred_name_Dutch>
    <Comment_Dutch xml:lang="nl">Onlangs hebben auteurs komeetstaartartefacten onderverdeeld in kleine en grote typen en een prevalentie van maligniteit van 15% gevonden in knobbeltjes met echogene foci met kleine komeetstaartartefacten [12]. Omgekeerd, bij het overwegen van grote komeetstaartartefacten in cystische of gedeeltelijk cystische knobbeltjes, hebben meerdere onderzoeken een sterke associatie aangetoond met goedaardigheid</Comment_Dutch>
  </rdf:Description>
```

## Note

Note that the translations are done purely based on machine translations. You are responsible to determine if your use case (e.g., machine learning training) is sufficient to rely on them.
