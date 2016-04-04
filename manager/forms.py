"""
    forms - Create MODS metadata forms for digital-cc-manager application 

"""
__author__ = "Jeremy Nelson"
import datetime

from flask_wtf import Form
from wtforms.fields.html5 import DateField, DateTimeField
from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired

DIGITAL_ORIGIN = [(1, 'born digital'),
                  (2, 'reformatted digital'),
                  (3, 'digitized microfilm'),
                  (4, 'digitized other analog')]


GENRE = [('choose', 'Choose...')]

INSTITUTION_NAME = 'Colorado College'

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
                    (1, 'Meeting Minutes'),
                    (2, 'Newsletter'),
                    (3, 'Podcast'),
                    (4, 'Video'),
                    (5, 'Master (All fields)')]

RIGHTS_STATEMENT = "Copyright restrictions apply. Contact Colorado College for permission to publish."
PLACE = 'Colorado Springs (Colo.)'
PUBLISHER = "Colorado College"
PUBLICATION_PLACE = 'Colorado Springs, Colorado'

class MODSMetadata(Form):
    admin_note = TextAreaField(label='Administrative Notes')
    alt_title = StringField(label='Alternative Title')
    collection_pid = StringField(label="PID of Parent Collection")
                                 
    contributors = StringField("Contributors")
    corporate_contributors = StringField("Corporate Contributors")
    corporate_creators = StringField("Corporate Creators")
    creators = StringField("Creators")
    date_created = DateField(label='Date Created')
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
    number_objects = StringField(label='Number of records')
    object_template = SelectField(label='Content Model Template',
                                  choices=OBJECT_TEMPLATES)
##    organizations = forms.CharField(max_length=255,
##                                    required=False,
##                                    initial=INSTITUTION_NAME,
##                                    widget=forms.TextInput(
##                                         attrs={'class': 'form-control'}))
    rights_holder = TextAreaField(label='Rights Statement',
                                  default=RIGHTS_STATEMENT)
##                                    widget=forms.Textarea(
##                                        attrs={'rows': 3,
##                                               'class': 'form-control'}))
##    subject_dates = forms.CharField(label='Subject -- Dates',
##                                    required=False,
##                                    widget=forms.TextInput(
##                                         {'class': 'form-control'}))
    subject_people = StringField(label='Subject -- People')
##    subject_places = forms.CharField(label='Subject -- Places',
##                                     required=False,
##                                     initial=PLACE,
##                                     widget=forms.TextInput(
##                                         {'class': 'form-control'}))
##    subject_topics = forms.CharField(
##        label='Subject -- Topic',
##        required=False,
##        widget=forms.TextInput(
##            attrs={'data-bind': 'value: topicOne',
##                   'class': 'form-control'}))
    title = StringField(label='Title',
                        validators=[DataRequired()])
    type_of_resource = StringField(
        label='Type of Resource')
##    def clean(self):
##        if self._errors.has_key('genre'):
##            del self._errors['genre']
##        return self.cleaned_data
##
##
##
##class BatchIngestForm(Form):
##    collection_pid = forms.CharField(max_length=20)
##    compressed_file = forms.FileField(label="A .tar or .zip file",
##                                      required=False)
##    target_directory = forms.FileField(label="Select Directory to upload",
##                                       required=False,
##                                       widget=forms.ClearableFileInput(attrs={"webkitdirectory":"",
##                                                                              "directory":"",
##                                                                              "mozdirectory":""}))

