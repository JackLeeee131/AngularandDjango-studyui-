from . import models
from . import serializers
from rest_framework import viewsets, permissions


class MoleculeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Molecule class"""

    queryset = models.Molecule.objects.all()
    serializer_class = serializers.MoleculeSerializer
    permission_classes = [permissions.IsAuthenticated]


class TrialViewSet(viewsets.ModelViewSet):
    """ViewSet for the Trial class"""

    queryset = models.Trial.objects.all()
    serializer_class = serializers.TrialSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for the Task class"""

    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportViewSet(viewsets.ModelViewSet):
    """ViewSet for the Report class"""

    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportSegmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the ReportSegment class"""

    queryset = models.ReportSegment.objects.all()
    serializer_class = serializers.ReportSegmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class TitleViewSet(viewsets.ModelViewSet):
    """ViewSet for the Title class"""

    queryset = models.Title.objects.all()
    serializer_class = serializers.TitleSerializer
    permission_classes = [permissions.IsAuthenticated]


class FootnoteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Footnote class"""

    queryset = models.Footnote.objects.all()
    serializer_class = serializers.FootnoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class MetadataViewSet(viewsets.ModelViewSet):
    """ViewSet for the Metadata class"""

    queryset = models.Metadata.objects.all()
    serializer_class = serializers.MetadataSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportSegmentDetailViewSet(viewsets.ModelViewSet):
    """ViewSet for the ReportSegmentDetail class"""

    queryset = models.ReportSegmentDetail.objects.all()
    serializer_class = serializers.ReportSegmentDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportHeaderViewSet(viewsets.ModelViewSet):
    """ViewSet for the ReportHeader class"""

    queryset = models.ReportHeader.objects.all()
    serializer_class = serializers.ReportHeaderSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportHeaderDetailViewSet(viewsets.ModelViewSet):
    """ViewSet for the ReportHeaderDetail class"""

    queryset = models.ReportHeaderDetail.objects.all()
    serializer_class = serializers.ReportHeaderDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportSubsetViewSet(viewsets.ModelViewSet):
    """ViewSet for the ReportSubset class"""

    queryset = models.ReportSubset.objects.all()
    serializer_class = serializers.ReportSubsetSerializer
    permission_classes = [permissions.IsAuthenticated]


