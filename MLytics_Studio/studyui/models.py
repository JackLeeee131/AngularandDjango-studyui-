from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import IntegerField
from django.db.models import TextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Molecule(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.CharField(max_length=100)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('studyui_molecule_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('studyui_molecule_update', args=(self.pk,))


class Trial(models.Model):

    # Fields
    name = models.CharField(max_length=200)
    phase = models.CharField(max_length=200,null=True)
    indication = models.CharField(max_length=1000,null=True)
    crossover = models.BooleanField(default=False)
    output_type = models.CharField(max_length=200,null=True)
    protocol = models.CharField(max_length=200,null=True)
    sap = models.CharField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.CharField(max_length=1000)

    # Relationship Fields
    molecule = models.ForeignKey(
        'studyui.Molecule',
        on_delete=models.CASCADE, related_name="trials",
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('studyui_trial_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('studyui_trial_update', args=(self.pk,))


class Task(models.Model):

    # Fields
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.CharField(max_length=1000)

    # Relationship Fields
    trial = models.ForeignKey(
        'studyui.Trial',
        on_delete=models.CASCADE, related_name="tasks", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        # return self.trial.molecule.name+str('-')+self.trial.name+str('-')+self.name
        return self.trial.name+str('-')+self.name

    def get_absolute_url(self):
        return reverse('studyui_task_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('studyui_task_update', args=(self.pk,))


class Report(models.Model):

    # Fields
    report_id = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    library = models.CharField(max_length=100)
    subject_data = models.CharField(max_length=100)
    column_variable = models.CharField(max_length=100)
    filter = models.CharField(max_length=1000)
    stat_label = models.CharField(max_length=1000)
    report_type = models.CharField(max_length=100)
    template = models.BooleanField()

    # Relationship Fields
    task = models.ForeignKey(
        'studyui.Task',
        on_delete=models.CASCADE, related_name="reports",
    )

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = "Reports"

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return self.report_id

    def get_absolute_url(self):
        return reverse('studyui_report_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('studyui_report_update', args=(self.pk,))

    # def generate_programs(self):




class Template(Report):

    class Meta:
        proxy = True


class ReportSegment(models.Model):

    # Fields
    variable = models.CharField(max_length=100)
    library = models.CharField(max_length=100)
    dataset = models.CharField(max_length=100)
    label = models.CharField(max_length=1000)
    filter = models.CharField(max_length=1000)
    analysis = models.CharField(max_length=100)
    additional_variables = models.CharField(max_length=1000,null=True)
    special_variables = models.CharField(max_length=1000, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    report = models.ForeignKey(
        'studyui.Report',
        on_delete=models.CASCADE, related_name="reportsegments", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return self.variable

    def get_absolute_url(self):
        return reverse('studyui_reportsegment_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('studyui_reportsegment_update', args=(self.pk,))


class Title(models.Model):

    # Fields
    text = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    order = models.IntegerField()

    # Relationship Fields
    report = models.ForeignKey(
        'studyui.Report',
        on_delete=models.CASCADE, related_name="titles", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('studyui_title_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('studyui_title_update', args=(self.pk,))


class Footnote(models.Model):

    # Fields
    text = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    order = models.IntegerField()

    # Relationship Fields
    report = models.ForeignKey(
        'studyui.Report',
        on_delete=models.CASCADE, related_name="footnotes", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('studyui_footnote_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('studyui_footnote_update', args=(self.pk,))


class Metadata(models.Model):

    # Fields
    parameter_code = models.CharField(max_length=100)
    parameter = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    label = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    dataset = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    data_type = models.CharField(max_length=100)
    controlled_terms = models.CharField(max_length=100)
    adam_class = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    variable_name = models.CharField(max_length=100)

    # Relationship Fields
    task = models.ForeignKey(
        'studyui.Task',
        on_delete=models.CASCADE, related_name="metadatas", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return self.parameter

    def get_absolute_url(self):
        return reverse('studyui_metadata_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('studyui_metadata_update', args=(self.pk,))


class ReportSegmentDetail(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    value = models.CharField(max_length=1000)
    description = models.CharField(max_length=100)
    order = models.CharField(max_length=100)

    # Relationship Fields
    reportsegment = models.ForeignKey(
        'studyui.ReportSegment',
        on_delete=models.CASCADE, related_name="reportsegmentdetails", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('studyui_reportsegmentdetail_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('studyui_reportsegmentdetail_update', args=(self.pk,))


class ReportHeader(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.CharField(max_length=100)

    # Relationship Fields
    task = models.ForeignKey(
        'studyui.Task',
        on_delete=models.CASCADE, related_name="taskheaders",
    )
    report = models.ForeignKey(
        'studyui.Report',
        on_delete=models.CASCADE, related_name="reportheaders",
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('studyui_reportheader_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('studyui_reportheader_update', args=(self.pk,))


class ReportHeaderDetail(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    column_condition = models.CharField(max_length=100)
    column_order = models.CharField(max_length=100)
    column_label = models.CharField(max_length=100)

    # Relationship Fields
    reportheader = models.ForeignKey(
        'studyui.ReportHeader',
        on_delete=models.CASCADE, related_name="reportheaderdetails",
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('studyui_reportheaderdetail_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('studyui_reportheaderdetail_update', args=(self.pk,))


class ReportSubset(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    population_subset = models.CharField(max_length=100)
    analysis_subset = models.CharField(max_length=100)
    population_title = models.CharField(max_length=1000)
    analysis_title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    # Relationship Fields
    report = models.ForeignKey(
        'studyui.Report',
        on_delete=models.CASCADE, related_name="reportsubsets",
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('studyui_reportsubset_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('studyui_reportsubset_update', args=(self.pk,))


