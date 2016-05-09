"""
    forms - Create MODS metadata forms for digital-cc-manager application 

"""
__author__ = "Jeremy Nelson"
import datetime

from flask_wtf import Form
from wtforms.fields.html5 import DateField, DateTimeField
from wtforms import SelectField, StringField, TextAreaField
from wtforms import FormField, FieldList, FileField
from wtforms.validators import DataRequired

DIGITAL_ORIGIN = [('1', 'born digital'),
                  ('2', 'reformatted digital'),
                  ('3', 'digitized microfilm'),
                  ('4', 'digitized other analog')]


GENRE = [('choose', 'Choose...')]

INSTITUTION_NAME = 'Colorado College'

ISLANDORA_CONTENT_MODELS = [
    ('audio', 'Audio'),
    ('basic-img', 'Basic Image'),
    ('collection', 'Collection'),
    ('compound', 'Compound'),
    ('doc', 'Document'),
    ('book', 'Book'),
    ('lg-img', 'Large Image'),
    ('news', 'Newspaper'),
    ('newspaper-issue', "Newspaper Issue"),
    ('pdf', 'PDF'),
    ('video', "Video")]

MARC_FREQUENCY = [('choose', 'Choose...'),
                  ('Semiweekly', 'Semiweekly - 2 times a week'),
                  ('Three times a week', 'Three times a week'),
                  ('Weekly', 'Weekly'),
                  ('Biweekly', 'Biweekly - every 2 weeks'),
                  ('Three times a month', 'Three times a month'),
                  ('Semimonthly', 'Semimonthly - 2 times a month'),
                  ('Monthly', 'Monthly'),
                  ('Bimonthly', 'Bimonthly - every 2 months'),
                  ('Quarterly', 'Quarterly'),
                  ('Three times a year', 'Three times a year'),
                  ('Semiannual', 'Semiannual - 2 times a year'),
                  ('Annual', 'Annual'),
                  ('Biennial', 'Biennial - every 2 years'),
                  ('Triennial', 'Triennial - every 3 years'),
                  ('Completely irregular', 'Completely irregular')]

OBJECT_TEMPLATES = [(0, 'Choose model'),
                    ('1', 'Meeting Minutes'),
                    ('2', 'Newsletter'),
                    ('3', 'Podcast'),
                    ('4', 'Video'),
                    ('5', 'Thesis'),
                    ('6', 'Master (All fields)')]

RIGHTS_STATEMENT = "Copyright restrictions apply. Contact Colorado College for permission to publish."
PLACE = 'Colorado Springs (Colo.)'
PUBLISHER = "Colorado College"
PUBLICATION_PLACE = 'Colorado Springs, Colorado'

class DatastreamUploadForm(Form):
    content_model = SelectField(
        "Content Model",
        choices=ISLANDORA_CONTENT_MODELS)
    ds_label = StringField("Label")
    datastream = FileField("Datastream")

class DeleteFedoraObjectForm(Form):
    pid = StringField(label="PID to removed",
                      validators=[DataRequired()])


class MODSBatchUpdateForm(Form):
    new_value = StringField(label="New Value")
    original_value = StringField(label="Original Value")
    select_xpath = StringField(label="MODS Selection XPath")
    

class MODSMetadataForm(Form):
    abstract = TextAreaField(label="Abstract")
    admin_notes = FieldList(TextAreaField(label='Administrative Notes'),
                            min_entries=1)
    alt_title = StringField(label='Alternative Title')
    collection_pid = StringField(
        label="PID of Parent Collection",
        validators=[DataRequired()])
    contributors = FieldList(StringField("Contributors"), min_entries=1)
    corporate_contributors = FieldList(
        StringField("Corporate Contributors"),
        min_entries=1)
    corporate_creators = FieldList(
        StringField("Corporate Creators"),
        min_entries=1)
    creators = FieldList(StringField("Creators"),
                         min_entries=1)
    datastreams = FieldList(FormField(DatastreamUploadForm), min_entries=1)
    date_created = StringField(label='Date Created')
    date_issued = StringField(label="Date Issued")
    degree_grantor = StringField(label="Degree Grantor")
    digital_origin = SelectField(choices=DIGITAL_ORIGIN,
                                 label='Digital Origin')
    description = TextAreaField(label='Description')
    extent = StringField(label='Extent')
    form = StringField(label='Form')
    frequency_free_form = StringField(label='Other')
    frequency = SelectField(choices=MARC_FREQUENCY,
                            label='Frequency')
    genre = SelectField(label='Genre', choices=[("choose","Choose genre")])
    genre_free_form = StringField(label='Other')
    languages = FieldList(StringField("Language"), min_entries=1)
    number_objects = StringField(label='Number of records')
    object_template = SelectField(label='Content Model Template',
                                  choices=OBJECT_TEMPLATES)
    organizations = FieldList(StringField("Organization", default=PUBLISHER), min_entries=1)
    publisher = StringField("Publisher Name", default=PUBLISHER)
    publisher_place = StringField("Publisher Location", default=PUBLICATION_PLACE)
    rights_statement = TextAreaField(label='Rights Statement',
                                  default=RIGHTS_STATEMENT)
    sponsor = StringField("Sponsor")
    subject_dates = FieldList(
        StringField(label='Subject -- Dates'), 
        min_entries=1)
    subject_people = StringField(label='Subject -- People')
    subject_places = FieldList(
        StringField(label='Subject -- Places', default=PLACE), 
        min_entries=1)
    subject_topics = FieldList(
        StringField(label='Subject -- Topic'), 
        min_entries=1)
    thesis_advisors = FieldList(
        StringField(label="Thesis Advisor"),
        min_entries=1)
    title = StringField(label='Title',
                        validators=[DataRequired()])
    type_of_resource = StringField(
        label='Type of Resource')

class SelectPIDForm(Form):
    pid = StringField(label="PID to removed",
                      validators=[DataRequired()])
