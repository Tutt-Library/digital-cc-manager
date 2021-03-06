"""Module constructs MODS class using MODS RDF"""
__author__ = "Jeremy Nelson"

import rdflib
import requests
import xml.etree.ElementTree as etree

from .forms import DIGITAL_ORIGIN

MODS_URI = "{http://www.loc.gov/mods/v3}"

MODS_XPATHS = {
    "admin_notes": """{0}note[@type="admin"]""".format(MODS_URI),
    "alt_title": """{0}titleInfo[@type="alternative"]/{0}title""".format(MODS_URI),
    "contributors":"""{0}name[@type="personal"]/{0}role[{0}roleTerm="contributor"]""".format(
        MODS_URI),
    "creators":"""{0}name[@type="personal"]/{0}role[{0}roleTerm="creator"]""".format(
         MODS_URI),
    "corporate_contributors": """{0}name[@type="corporate"]/{0}roleTerm="contributor""".format(
        MODS_URI)
}

etree.register_namespace("mods", MODS_URI)
etree.register_namespace("xlink", "http://www.w3.org/1999/xlink")
etree.register_namespace("xsd", "http://www.w3.org/2001/XMLSchema-instance")


def extract_multiple(doc, template):
    xpath = template
    output = []
    for row in doc.findall(xpath):
        output.append(row.text)
    return output

def extract_single(doc, template):
    xpath = template
    element = doc.find(xpath)
    if element is not None:
        return element.text
    return str()


class MODS(object):

    def __init__(self, xml=None):
        if xml is None:
            self.doc = etree.Element("""<mods xmlns:mods="http://www.loc.gov/mods/v3" 
           xmlns="http://www.loc.gov/mods/v3" 
           xmlns:xlink="http://www.w3.org/1999/xlink" 
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"></mods>""")
        else:
            self.doc = etree.XML(xml)
        self.abstract = extract_single(
            self.doc,
            "{0}abstract".format(MODS_URI))
        self.admin_notes = extract_multiple(
            self.doc,
            MODS_XPATHS.get("admin_notes"))
        self.alt_title = extract_single(
            self.doc,
            MODS_XPATHS.get("alt_title"))
        self.date_created = extract_single(
            self.doc,
            "{0}originInfo/{0}dateCreated".format(MODS_URI))
        self.date_issued = extract_single(
            self.doc,
            "{0}originInfo/{0}dateIssued".format(MODS_URI))
        self.digital_origin = extract_single(
            self.doc,
            "{0}physicalDescription/{0}digitalOrigin".format(MODS_URI))
        self.extent = extract_single(
            self.doc,
            "{0}physicalDescription/{0}extent".format(MODS_URI))
        self.__init_names__()
        self.languages = extract_multiple(
            self.doc,
            "{0}language/{0}languageTerm".format(MODS_URI))
        self.publisher = extract_single(
            self.doc,
            "{0}originInfo/{0}publisher".format(MODS_URI))
        self.publisher_place = extract_single(
            self.doc,
            "{0}originInfo/{0}place/{0}placeTerm".format(MODS_URI))
        self.rights_statement = extract_single(
            self.doc,
            """{0}accessCondition[@type="useAndReproduction"]""".format(
                MODS_URI))
        self.subject_places = extract_multiple(
            self.doc,
            """{0}subject/{0}place""".format(MODS_URI))
        self.subject_topics = extract_multiple(
            self.doc,
            """{0}subject/{0}topic""".format(MODS_URI))
        self.title = extract_single(
            self.doc,
            "{0}titleInfo/{0}title".format(MODS_URI))
        self.type_of_resource = extract_single(
            self.doc,
            "{0}typeOfResource".format(MODS_URI))

                

    def __init_names__(self):
        self.contributors, self.creators, self.thesis_advisors = [], [], []
        self.corporate_contributors, self.degree_grantor, self.sponsor  = [], None, None
        self.corporate_creators = []
        for name in self.doc.findall("""{0}name""".format(MODS_URI)):
            name_part = name.find("{0}namePart".format(MODS_URI))
            role_term = name.find("{0}role/{0}roleTerm".format(MODS_URI))
            type_of = name.get("type")
            if role_term.text.startswith("contributor"):
                if type_of.startswith("corporate"):
                    self.corporate_contributors.append(name_part.text)
                else: # Default assumes that a contributor is a person
                    self.contributors.append(name_part.text)
            if role_term.text.startswith("creator"):
                if type_of.startswith("corporate"):
                    self.corporate_creators.append(name_part.text)
                else:
                    self.creators.append(name_part.text)
            if role_term.text.startswith("degree grantor"):
                self.degree_grantor = name_part.text
            if role_term.text.startswith("sponsor"):
                self.sponsor = name_part.text
            if role_term.text.startswith("thesis advisor"):
                self.thesis_advisors.append(name_part.text)

                       

    def __add__(self, parent_xpath, name, value):
        parent_element = self.doc.find(parent_xpath)
        element = etree.SubElement(parent_element, name)
        element.text = value

    def __populate_multiple__(self, element, form_field):
        if len(element) > 0:
            form_field.pop_entry()
        for row in element:
            form_field.append_entry(row)

    def __populate_select__(self, element, choices):
        for choice in choices:
            if choice[1] == element:
                return choice[0]

    def __update__(self, xpath, value):
        element = self.doc.find(xpath)
        if element is not None:
             element.text = value

    def get_info(self, pid, config, form):
        ri_query = """SELECT distinct ?parent ?content_model
WHERE {{
   <info:fedora/{0}> <fedora-rels-ext:isMemberOfCollection>  ?parent .
   <info:fedora/{0}> <fedora-model:hasModel> ?content_model
}}""".format(pid)
        ri_result = requests.post(config.get("RI_URL"),
            data={"type": "tuples",
                  "lang": "sparql",
                "format": "json",
                "query": ri_query},
            auth=config.get("FEDORA_AUTH"))
        for row in ri_result.json().get('results'):
            print(row)
            if 'parent' in row:
                parent_pid = row.get('parent').split("/")[-1]
                print(parent_pid, form.collection_pid.data)
                form.collection_pid.data = parent_pid
            if 'content_model' in row and \
                not row['content_model'].endswith("3.0"):
                form.content_model.data = row["content_model"].split("/")[-1].split(":")[-1].split("_")[-1]
        
    

    def populate(self, form):
        form.abstract.data = self.abstract
        self.__populate_multiple__(
            self.contributors,
            form.contributors)
        self.__populate_multiple__(
            self.creators,
            form.creators)
        form.date_created.data = self.date_created
        if self.date_issued:
            form.date_issued.data = self.date_issued
        if self.degree_grantor:
            form.degree_grantor.data = self.degree_grantor
        form.extent.data = self.extent
        form.digital_origin.data = self.__populate_select__(
            self.digital_origin,
            DIGITAL_ORIGIN)
        self.__populate_multiple__(
            self.languages,
            form.languages)
        form.publisher.data = self.publisher
        form.publisher_place.data = self.publisher_place
        form.rights_statement.data = self.rights_statement
        form.sponsor.data = self.sponsor
        self.__populate_multiple__(
            self.subject_places,
            form.subject_places)
        self.__populate_multiple__(
            self.subject_topics,
            form.subject_topics)
        self.__populate_multiple__(
            self.thesis_advisors,
            form.thesis_advisors)
        form.title.data = self.title
        form.type_of_resource.data = self.type_of_resource
                               
            
       

#MODS_RDF = rdflib.Graph()
#MODS_RDF.parse("http://www.loc.gov/standards/mods/modsrdf/v1/modsrdf.owl", 
#              format="xml")

#for subject in set([s for s in MODS_RDF.subjects()]):
#    property_name = str(subject).split("#")[-1]
#    setattr(MODS, property_name, "")
