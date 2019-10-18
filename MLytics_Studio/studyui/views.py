from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Molecule, Trial, Task, Report, ReportSegment, Title, Footnote, Metadata, ReportSegmentDetail, ReportHeader, ReportHeaderDetail, ReportSubset
from .forms import MoleculeForm, TrialForm, TaskForm, ReportForm, ReportSegmentForm, TitleForm, FootnoteForm, MetadataForm, ReportSegmentDetailForm, ReportHeaderForm, ReportHeaderDetailForm, ReportSubsetForm


class MoleculeListView(ListView):
    model = Molecule


class MoleculeCreateView(CreateView):
    model = Molecule
    form_class = MoleculeForm


class MoleculeDetailView(DetailView):
    model = Molecule


class MoleculeUpdateView(UpdateView):
    model = Molecule
    form_class = MoleculeForm


class TrialListView(ListView):
    model = Trial


class TrialCreateView(CreateView):
    model = Trial
    form_class = TrialForm



class TrialDetailView(DetailView):
    model = Trial


class TrialUpdateView(UpdateView):
    model = Trial
    form_class = TrialForm


class TaskListView(ListView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm


class ReportListView(ListView):
    model = Report


class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm


class ReportDetailView(DetailView):
    model = Report


class ReportUpdateView(UpdateView):
    model = Report
    form_class = ReportForm


class ReportSegmentListView(ListView):
    model = ReportSegment


class ReportSegmentCreateView(CreateView):
    model = ReportSegment
    form_class = ReportSegmentForm


class ReportSegmentDetailView(DetailView):
    model = ReportSegment


class ReportSegmentUpdateView(UpdateView):
    model = ReportSegment
    form_class = ReportSegmentForm


class TitleListView(ListView):
    model = Title


class TitleCreateView(CreateView):
    model = Title
    form_class = TitleForm


class TitleDetailView(DetailView):
    model = Title


class TitleUpdateView(UpdateView):
    model = Title
    form_class = TitleForm


class FootnoteListView(ListView):
    model = Footnote


class FootnoteCreateView(CreateView):
    model = Footnote
    form_class = FootnoteForm


class FootnoteDetailView(DetailView):
    model = Footnote


class FootnoteUpdateView(UpdateView):
    model = Footnote
    form_class = FootnoteForm


class MetadataListView(ListView):
    model = Metadata


class MetadataCreateView(CreateView):
    model = Metadata
    form_class = MetadataForm


class MetadataDetailView(DetailView):
    model = Metadata


class MetadataUpdateView(UpdateView):
    model = Metadata
    form_class = MetadataForm


class ReportSegmentDetailListView(ListView):
    model = ReportSegmentDetail


class ReportSegmentDetailCreateView(CreateView):
    model = ReportSegmentDetail
    form_class = ReportSegmentDetailForm


class ReportSegmentDetailDetailView(DetailView):
    model = ReportSegmentDetail


class ReportSegmentDetailUpdateView(UpdateView):
    model = ReportSegmentDetail
    form_class = ReportSegmentDetailForm


class ReportHeaderListView(ListView):
    model = ReportHeader


class ReportHeaderCreateView(CreateView):
    model = ReportHeader
    form_class = ReportHeaderForm


class ReportHeaderDetailView(DetailView):
    model = ReportHeader


class ReportHeaderUpdateView(UpdateView):
    model = ReportHeader
    form_class = ReportHeaderForm


class ReportHeaderDetailListView(ListView):
    model = ReportHeaderDetail


class ReportHeaderDetailCreateView(CreateView):
    model = ReportHeaderDetail
    form_class = ReportHeaderDetailForm


class ReportHeaderDetailDetailView(DetailView):
    model = ReportHeaderDetail


class ReportHeaderDetailUpdateView(UpdateView):
    model = ReportHeaderDetail
    form_class = ReportHeaderDetailForm


class ReportSubsetListView(ListView):
    model = ReportSubset


class ReportSubsetCreateView(CreateView):
    model = ReportSubset
    form_class = ReportSubsetForm


class ReportSubsetDetailView(DetailView):
    model = ReportSubset


class ReportSubsetUpdateView(UpdateView):
    model = ReportSubset
    form_class = ReportSubsetForm

