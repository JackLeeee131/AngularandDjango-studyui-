from import_export import resources
from .models import Molecule, Study, Task, Report, ReportSegment, Title, Footnote, Metadata, ReportSegmentDetail, ReportHeader, ReportHeaderDetail, ReportSubset


class MoleculeResource(resources.ModelResource):
    class Meta:
        model = Molecule


class StudyResource(resources.ModelResource):
    class Meta:
        model = Study


class TaskResource(resources.ModelResource):
    class Meta:
        model = Task


class ReportResource(resources.ModelResource):
    class Meta:
        model = Report


class ReportSegmentResource(resources.ModelResource):
    class Meta:
        model = ReportSegment


class TitleResource(resources.ModelResource):
    class Meta:
        model = Title


class FootnoteResource(resources.ModelResource):
    class Meta:
        model = Footnote


class MetadataResource(resources.ModelResource):
    class Meta:
        model = Metadata


class ReportSegmentDetailResource(resources.ModelResource):
    class Meta:
        model = ReportSegmentDetail


class ReportHeaderResource(resources.ModelResource):
    class Meta:
        model = ReportHeader


class ReportHeaderDetailResource(resources.ModelResource):
    class Meta:
        model = ReportHeaderDetail


class ReportSubsetResource(resources.ModelResource):
    class Meta:
        model = ReportSubset

