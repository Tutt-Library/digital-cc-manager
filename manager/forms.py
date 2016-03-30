"""
    forms - Create MODS metadata forms for digital-cc-manager application 

"""
__author__ = "Jeremy Nelson"
import datetime

from flask_wtf import Form
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
                                 
##    contributors = forms.CharField(required=False,
##                                   widget=forms.TextInput(
##                                         attrs={'class': 'form-control'}))
##    corporate_contributors = forms.CharField(
##        required=False,
##        widget=forms.TextInput(
##            attrs={'class': 'form-control'}))
##    corporate_creators = forms.CharField(
##        required=False,
##        widget=forms.TextInput(
##            attrs={'class': 'form-control'}))
##    creators = forms.CharField(required=False,
##                               widget=forms.TextInput(
##                                         attrs={'class': 'form-control'}))
##    date_created = forms.CharField(label='Date Created',
##                                   required=False,
##                                   widget=forms.TextInput(
##                                         attrs={'class': 'form-control'}))
##    digital_origin = forms.ChoiceField(choices=DIGITAL_ORIGIN,
##                                       label='Digital Origin',
##                                       initial=1,
##                                       widget=forms.Select(
##                                            attrs={
##                                                 'class': 'form-control'}))
##    description = forms.CharField(label='Description',
##                                  max_length=1500,
##                                  widget=forms.Textarea(
##                                      attrs={'class': 'form-control',
##                                             'rows':5}),
##                                  required=False)
##    extent = forms.CharField(label='Extent',
##                             max_length=1500,
##                             widget=forms.Textarea(
##                                 attrs={'rows':5,
##                                        'class': 'form-control',
##                                        'data-bind': 'value: extentValue'}),
##                             required=False)
##    form = forms.CharField(label='Form',
##                           required=False,
##                           widget=forms.TextInput(
##                               attrs={
##                                   'class': 'form-control',
##                                   'data-bind': 'value: formValue'}))
##    frequency_free_form = forms.CharField(label='Other',
##                                          required=False,
##                                          widget=forms.TextInput(
##                                              attrs={'class': 'form-control'}))
##    frequency = forms.ChoiceField(choices=MARC_FREQUENCY,
##                                  label='Frequency',
##                                  required=False,
##                                  widget=forms.Select(
##                                      attrs={'class': 'form-control'}))
##    genre = forms.ChoiceField(
##        label='Genre',
##        required=False,
##        widget=forms.Select(
##            attrs={'data-bind': "options: genreOptions, optionsText: 'name', optionsValue: 'value'",
##                   'class': 'form-control'}))
##    genre_free_form = forms.CharField(label='Other',
##                                      required=False,
##                                      widget=forms.TextInput(
##                                              attrs={'class': 'form-control'}))
##    number_objects = forms.CharField(initial=1,
##                                     label='Number of stub records',
##                                     max_length=5,
##                                     widget=forms.TextInput(
##                                         attrs={'class': 'form-control'}))
    object_template = SelectField(label='Content Model Template',
                                  choices=OBJECT_TEMPLATES)
##    organizations = forms.CharField(max_length=255,
##                                    required=False,
##                                    initial=INSTITUTION_NAME,
##                                    widget=forms.TextInput(
##                                         attrs={'class': 'form-control'}))
##    rights_holder = forms.CharField(max_length=255,
##                                    label='Rights Statement',
##                                    initial=RIGHTS_STATEMENT,
##                                    widget=forms.Textarea(
##                                        attrs={'rows': 3,
##                                               'class': 'form-control'}))
##    subject_dates = forms.CharField(label='Subject -- Dates',
##                                    required=False,
##                                    widget=forms.TextInput(
##                                         {'class': 'form-control'}))
##    subject_people = forms.CharField(label='Subject -- People',
##                                     required=False,
##                                     widget=forms.TextInput(
##                                         {'class': 'form-control'}))
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

                        ##    type_of_resource = forms.CharField(
##        label='Type of Resource',
##        required=False,
##        widget=forms.TextInput(
##            attrs={'data-bind': 'value: typeOfResource',
##                   'class': 'form-control'}))
##
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

