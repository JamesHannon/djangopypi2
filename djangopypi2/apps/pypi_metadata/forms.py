from django import forms
from django.utils.translation import ugettext_lazy as _
from .definitions import METADATA_LICENSES
from .models import Classifier

class LinesField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', forms.Textarea())
        super(LinesField, self).__init__(*args, **kwargs)
    
    def to_python(self, value):
        return map(lambda s: s.strip(),
                   super(LinesField, self).to_python(value).split('\n'))

class Metadata10Form(forms.Form):
    platform = LinesField(required=False,
                          help_text=_(u'A comma-separated list of platform '
                                      'specifications, summarizing the '
                                      'operating systems supported by the '
                                      'package.'))
    
    summary = forms.CharField(help_text=_(u'A one-line summary of what the '
                                          'package does.'))
    
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs=dict(rows=40,
                                                                   columns=40)),
                                  help_text=_(u'A longer description of the '
                                              'package that can run to several '
                                              'paragraphs. If this is in '
                                              'reStructuredText format, it will '
                                              'be rendered nicely on display.'))
    
    keywords = forms.CharField(help_text=_(u'A list of additional keywords to '
                                           'be used to assist searching for the '
                                           'package in a larger catalog'))
    
    home_page = forms.URLField(required=False,
                               help_text=_(u'A string containing the URL for '
                                           'the package\'s home page.'))
    
    author = forms.CharField(required=False,
                             widget=forms.Textarea(attrs=dict(rows=3,
                                                              columns=20)),
                             help_text=_(u'A string containing at a minimum the '
                                         'author\'s name.  Contact information '
                                         'can also be added, separating each '
                                         'line with newlines.'))
    
    author_email = forms.CharField(help_text=_(u'A string containing the '
                                               'author\'s e-mail address.  It '
                                               'can contain a name and e-mail '
                                               'address in the legal forms for '
                                               'a RFC-822 \'From:\' header.'))
    
    license = forms.CharField(max_length=32,
                              help_text=_(u'A string selected from a short list '
                                          'of choices, specifying the license '
                                          'covering the package.'),
                              widget=forms.Select(choices=(zip(METADATA_LICENSES,
                                                               METADATA_LICENSES))))
    
class Metadata11Form(Metadata10Form):
    supported_platform = forms.CharField(required=False, widget=forms.Textarea(),
                                         help_text=_(u'The OS and CPU for which '
                                                     'the binary package was '
                                                     'compiled.'))
    
    keywords = forms.CharField(required=False,
                               help_text=_(u'A list of additional keywords to '
                                           'be used to assist searching for the '
                                           'package in a larger catalog'))
    
    download_url = forms.URLField(required=False,
                                  help_text=_(u'A string containing the URL for '
                                              'the package\'s home page.'))
    
    license = forms.CharField(required=False, widget=forms.Textarea(),
                              help_text=_(u'Text indicating the license '
                                          'covering the package where the '
                                          'license is not a selection from the '
                                          '"License" Trove classifiers.'))
    
    classifier = forms.ModelMultipleChoiceField(required=False,
                                                queryset=Classifier.objects.all(),
                                                help_text=_(u'Trove classifiers'))
    
    requires = LinesField(required=False,
                          help_text=_(u'Each line contains a string describing '
                                      'some other module or package required by '
                                      'this package.'))
    
    provides = LinesField(required=False,
                          help_text=_(u'Each line contains a string describing '
                                      'a package or module that will be '
                                      'provided by this package once it is '
                                      'installed'))
    
    obsoletes = LinesField(required=False,
                           help_text=_(u'Each line contains a string describing '
                                       'a package or module that this package '
                                       'renders obsolete, meaning that the two '
                                       'packages should not be installed at the '
                                       'same time'))

class Metadata12Form(Metadata10Form):
    supported_platform = forms.CharField(required=False, widget=forms.Textarea(),
                                         help_text=_(u'The OS and CPU for which '
                                                     'the binary package was '
                                                     'compiled.'))
    
    keywords = forms.CharField(required=False,
                               help_text=_(u'A list of additional keywords to '
                                           'be used to assist searching for the '
                                           'package in a larger catalog'))
    
    download_url = forms.URLField(required=False,
                                  help_text=_(u'A string containing the URL for '
                                              'the package\'s home page.'))
    
    author_email = forms.CharField(required=False,
                                   help_text=_(u'A string containing the '
                                               'author\'s e-mail address.  It '
                                               'can contain a name and e-mail '
                                               'address in the legal forms for '
                                               'a RFC-822 \'From:\' header.'))
    
    maintainer = forms.CharField(required=False, widget=forms.Textarea(),
                                 help_text=_(u'A string containing at a minimum '
                                             'the maintainer\'s name.  Contact '
                                             'information can also be added, '
                                             'separating each line with '
                                             'newlines.'))
    maintainer_email = forms.CharField(required=False,
                                       help_text=_(u'A string containing the '
                                                   'maintainer\'s e-mail address. '
                                                   'It can contain a name and '
                                                   'e-mail address in the legal '
                                                   'forms for a RFC-822 '
                                                   '\'From:\' header.'))
    
    license = forms.CharField(required=False, widget=forms.Textarea(),
                              help_text=_(u'Text indicating the license '
                                          'covering the package where the '
                                          'license is not a selection from the '
                                          '"License" Trove classifiers.'))
    
    classifier = forms.ModelMultipleChoiceField(required=False,
                                                queryset=Classifier.objects.all(),
                                                help_text=_(u'Trove classifiers'))
    
    requires_dist = LinesField(required=False,
                               help_text=_(u'Each line contains a string '
                                            'describing some other module or '
                                            'package required by this package.'))
    
    provides_dist = LinesField(required=False,
                               help_text=_(u'Each line contains a string '
                                           'describing a package or module that '
                                           'will be provided by this package '
                                           'once it is installed'))

    obsoletes_dist = LinesField(required=False,
                                help_text=_(u'Each line contains a string '
                                            'describing a package or module that '
                                            'this package renders obsolete, '
                                            'meaning that the two packages '
                                            'should not be installed at the '
                                            'same time'))
    
    requires_python = forms.CharField(required=False,
                                      help_text=_(u'This field specifies the '
                                                  'Python version(s) that the '
                                                  'distribution is guaranteed '
                                                  'to be compatible with.'))
    
    requires_external = forms.CharField(required=False, widget=forms.Textarea(),
                                        help_text=_(u'Each line contains a '
                                                    'string describing some '
                                                    'dependency in the system '
                                                    'that the distribution is '
                                                    'to be used.'))
    project_url = forms.CharField(required=False, widget=forms.Textarea(),
                                  help_text=_(u'Each line is a string containing '
                                              'a browsable URL for the project '
                                              'and a label for it, separated '
                                              'by a comma: "Bug Tracker, '
                                              'http://bugs.project.com"'))

METADATA_FORMS = {
    '1.0': Metadata10Form,
    '1.1': Metadata11Form,
    '1.2': Metadata12Form,
}
