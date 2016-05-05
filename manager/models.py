"""Module constructs MODS class using MODS RDF"""
__author__ = "Jeremy Nelson"

import rdflib
import xml.etree.ElementTree as etree

etree.register_namespace("mods", "http://www.loc.gov/mods/v3")
etree.register_namespace("xlink", "http://www.w3.org/1999/xlink")
etree.register_namespace("xsd", "http://www.w3.org/2001/XMLSchema-instance")

class MODS(object):

    def __init__(self, xml=None):
        if xml is None:
            self.doc = etree.Element("mods")
        else:
            self.doc = etree.XML(xml)

    def __add__(self, parent_xpath, name, value):
        parent_element = self.doc.find(parent_xpath)
        element = etree.SubElement(parent_element, name)
        element.text = value

    def __update__(self, xpath, value):
        element = self.doc.find(xpath)
        if element is not None:
             element.text = value

       

MODS_RDF = rdflib.Graph()
MODS_RDF.parse("http://www.loc.gov/standards/mods/modsrdf/v1/modsrdf.owl", 
              format="xml")

for subject in set([s for s in MODS_RDF.subjects()]):
    property_name = str(subject).split("#")[-1]
    setattr(MODS, property_name, "")
