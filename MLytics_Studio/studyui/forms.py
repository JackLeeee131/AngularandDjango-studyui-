from django import forms
from .models import Molecule, Trial, Task, Report, ReportSegment, Title, Footnote, Metadata, ReportSegmentDetail, ReportHeader, ReportHeaderDetail, ReportSubset


class MoleculeForm(forms.ModelForm):
    class Meta:
        model = Molecule
        fields = ['name', 'description']


class TrialForm(forms.ModelForm):
    class Meta:
        model = Trial
        fields = ['name', 'phase', 'indication', 'crossover', 'output_type', 'protocol', 'sap', 'description', 'molecule']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'location', 'description', 'trial']


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_id', 'library', 'subject_data', 'column_variable', 'filter', 'stat_label', 'report_type', 'task']


class ReportSegmentForm(forms.ModelForm):
    class Meta:
        model = ReportSegment
        fields = ['variable', 'library', 'dataset', 'label', 'filter', 'analysis', 'additional_variables', 'special_variables', 'report']


class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['text', 'order', 'report']


class FootnoteForm(forms.ModelForm):
    class Meta:
        model = Footnote
        fields = ['text', 'order', 'report']


class MetadataForm(forms.ModelForm):
    class Meta:
        model = Metadata
        fields = ['parameter_code', 'label', 'description', 'dataset', 'length', 'data_type', 'controlled_terms', 'adam_class', 'category', 'sub_category', 'variable_name', 'task']


class ReportSegmentDetailForm(forms.ModelForm):
    class Meta:
        model = ReportSegmentDetail
        fields = ['name', 'value', 'description', 'order', 'reportsegment']


class ReportHeaderForm(forms.ModelForm):
    class Meta:
        model = ReportHeader
        fields = ['name', 'description', 'task']


class ReportHeaderDetailForm(forms.ModelForm):
    class Meta:
        model = ReportHeaderDetail
        fields = ['name', 'column_condition', 'column_order', 'column_label', 'reportheader']


class ReportSubsetForm(forms.ModelForm):
    class Meta:
        model = ReportSubset
        fields = ['name', 'population_subset', 'analysis_subset', 'population_title', 'analysis_title', 'description', 'report']


