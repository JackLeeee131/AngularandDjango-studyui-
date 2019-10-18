from . import models

from rest_framework import serializers


class MoleculeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Molecule
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
            'description', 
        )


class TrialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Trial
        fields = (
            'pk', 
            'name', 
            'phase', 
            'indication', 
            'crossover', 
            'output_type', 
            'protocol', 
            'sap', 
            'created', 
            'last_updated', 
            'description', 
        )


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = (
            'pk', 
            'name', 
            'location', 
            'created', 
            'last_updated', 
            'description', 
        )


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Report
        fields = (
            'pk', 
            'report_id', 
            'created', 
            'last_updated',
            'library', 
            'subject_data', 
            'column_variable', 
            'filter', 
            'stat_label', 
            'template', 
            'report_type',
        )


class ReportSegmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ReportSegment
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'library', 
            'dataset', 
            'variable', 
            'label', 
            'filter', 
            'analysis', 
            'additional_variables', 
            'special_variables', 
        )


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Title
        fields = (
            'pk', 
            'text', 
            'created', 
            'last_updated', 
            'order', 
        )


class FootnoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Footnote
        fields = (
            'pk', 
            'text', 
            'created', 
            'last_updated', 
            'order', 
        )


class MetadataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Metadata
        fields = (
            'pk', 
            'parameter_code', 
            'created', 
            'last_updated', 
            'label', 
            'description', 
            'dataset', 
            'length', 
            'data_type', 
            'controlled_terms', 
            'adam_class', 
            'category', 
            'sub_category', 
            'variable_name', 
        )


class ReportSegmentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ReportSegmentDetail
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
            'value', 
            'description', 
            'order', 
        )


class ReportHeaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ReportHeader
        fields = (
            'pk',
            'name',
            'created',
            'last_updated',
            'description',
        )


class ReportHeaderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ReportHeaderDetail
        fields = (
            'pk',
            'name',
            'created',
            'last_updated',
            'column_condition',
            'column_order',
            'column_label',
        )


class ReportSubsetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ReportSubset
        fields = (
            'pk',
            'name',
            'created',
            'last_updated',
            'population_subset',
            'analysis_subset',
            'population_title',
            'analysis_title',
            'description',
        )


