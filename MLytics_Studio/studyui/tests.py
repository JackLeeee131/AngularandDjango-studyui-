import unittest
from django.urls import reverse
from django.test import Client
from .models import Molecule, Trial, Task, Report, ReportSegment, Title, Footnote, Metadata, ReportSegmentDetail, ReportHeader, ReportHeaderDetail, ReportSubset
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_molecule(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    return Molecule.objects.create(**defaults)


def create_trial(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["phase"] = "phase"
    defaults["indication"] = "indication"
    defaults["crossover"] = "crossover"
    defaults["output_type"] = "output_type"
    defaults["protocol"] = "protocol"
    defaults["sap"] = "sap"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    if "molecule" not in defaults:
        defaults["molecule"] = create_molecule()
    return Trial.objects.create(**defaults)


def create_task(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["location"] = "location"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    if "study" not in defaults:
        defaults["study"] = create_study()
    return Task.objects.create(**defaults)


def create_report(**kwargs):
    defaults = {}
    defaults["report_id"] = "report_id"
    defaults["library"] = "library"
    defaults["subject_data"] = "subject_data"
    defaults["column_variable"] = "column_variable"
    defaults["filter"] = "filter"
    defaults["stat_label"] = "stat_label"
    defaults["template"] = "template"
    defaults["report_type"] = "report_type"
    defaults.update(**kwargs)
    if "task" not in defaults:
        defaults["task"] = create_task()
    return Report.objects.create(**defaults)


def create_reportsegment(**kwargs):
    defaults = {}
    defaults["library"] = "library"
    defaults["dataset"] = "dataset"
    defaults["variable"] = "variable"
    defaults["label"] = "label"
    defaults["filter"] = "filter"
    defaults["analysis"] = "analysis"
    defaults["additional_variables"] = "additional_variables"
    defaults["special_variables"] = "special_variables"
    defaults.update(**kwargs)
    if "report" not in defaults:
        defaults["report"] = create_report()
    return ReportSegment.objects.create(**defaults)


def create_title(**kwargs):
    defaults = {}
    defaults["text"] = "text"
    defaults["order"] = "order"
    defaults.update(**kwargs)
    if "report" not in defaults:
        defaults["report"] = create_report()
    return Title.objects.create(**defaults)


def create_footnote(**kwargs):
    defaults = {}
    defaults["text"] = "text"
    defaults["order"] = "order"
    defaults.update(**kwargs)
    if "report" not in defaults:
        defaults["report"] = create_report()
    return Footnote.objects.create(**defaults)


def create_metadata(**kwargs):
    defaults = {}
    defaults["parameter_code"] = "parameter_code"
    defaults["label"] = "label"
    defaults["description"] = "description"
    defaults["dataset"] = "dataset"
    defaults["length"] = "length"
    defaults["data_type"] = "data_type"
    defaults["controlled_terms"] = "controlled_terms"
    defaults["adam_class"] = "adam_class"
    defaults["category"] = "category"
    defaults["sub_category"] = "sub_category"
    defaults["variable_name"] = "variable_name"
    defaults.update(**kwargs)
    if "task" not in defaults:
        defaults["task"] = create_task()
    return Metadata.objects.create(**defaults)


def create_reportsegmentdetail(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["value"] = "value"
    defaults["description"] = "description"
    defaults["order"] = "order"
    defaults.update(**kwargs)
    if "reportsegment" not in defaults:
        defaults["reportsegment"] = create_reportsegment()
    return ReportSegmentDetail.objects.create(**defaults)


def create_reportheader(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    if "task" not in defaults:
        defaults["task"] = create_task()
    return ReportHeader.objects.create(**defaults)


def create_reportheaderdetail(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["column_condition"] = "column_condition"
    defaults["column_order"] = "column_order"
    defaults["column_label"] = "column_label"
    defaults.update(**kwargs)
    if "reportheader" not in defaults:
        defaults["reportheader"] = create_reportheader()
    return ReportHeaderDetail.objects.create(**defaults)


def create_reportsubset(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["population_subset"] = "population_subset"
    defaults["analysis_subset"] = "analysis_subset"
    defaults["population_title"] = "population_title"
    defaults["analysis_title"] = "analysis_title"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    if "report" not in defaults:
        defaults["report"] = create_report()
    return ReportSubset.objects.create(**defaults)


class MoleculeViewTest(unittest.TestCase):
    '''
    Tests for Molecule
    '''
    def setUp(self):
        self.client = Client()

    def test_list_molecule(self):
        url = reverse('studyui_molecule_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_molecule(self):
        url = reverse('studyui_molecule_create')
        data = {
            "name": "name",
            "description": "description",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_molecule(self):
        molecule = create_molecule()
        url = reverse('studyui_molecule_detail', args=[molecule.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_molecule(self):
        molecule = create_molecule()
        data = {
            "name": "name",
            "description": "description",
        }
        url = reverse('studyui_molecule_update', args=[molecule.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TrialViewTest(unittest.TestCase):
    '''
    Tests for Trial
    '''
    def setUp(self):
        self.client = Client()

    def test_list_trial(self):
        url = reverse('studyui_trial_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_trial(self):
        url = reverse('studyui_trial_create')
        data = {
            "name": "name",
            "phase": "phase",
            "indication": "indication",
            "crossover": "crossover",
            "output_type": "output_type",
            "protocol": "protocol",
            "sap": "sap",
            "description": "description",
            "molecule": create_molecule().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_trial(self):
        trial = create_trial()
        url = reverse('studyui_trial_detail', args=[trial.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_trial(self):
        trial = create_trial()
        data = {
            "name": "name",
            "phase": "phase",
            "indication": "indication",
            "crossover": "crossover",
            "output_type": "output_type",
            "protocol": "protocol",
            "sap": "sap",
            "description": "description",
            "molecule": create_molecule().pk,
        }
        url = reverse('studyui_trial_update', args=[trial.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TaskViewTest(unittest.TestCase):
    '''
    Tests for Task
    '''
    def setUp(self):
        self.client = Client()

    def test_list_task(self):
        url = reverse('studyui_task_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        url = reverse('studyui_task_create')
        data = {
            "name": "name",
            "location": "location",
            "description": "description",
            "study": create_study().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_task(self):
        task = create_task()
        url = reverse('studyui_task_detail', args=[task.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_task(self):
        task = create_task()
        data = {
            "name": "name",
            "location": "location",
            "description": "description",
            "study": create_study().pk,
        }
        url = reverse('studyui_task_update', args=[task.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ReportViewTest(unittest.TestCase):
    '''
    Tests for Report
    '''
    def setUp(self):
        self.client = Client()

    def test_list_report(self):
        url = reverse('studyui_report_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_report(self):
        url = reverse('studyui_report_create')
        data = {
            "report_id": "report_id",
            "library": "library",
            "subject_data": "subject_data",
            "column_variable": "column_variable",
            "filter": "filter",
            "stat_label": "stat_label",
            "template": "template",
            "report_type": "report_type",
            "task": create_task().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_report(self):
        report = create_report()
        url = reverse('studyui_report_detail', args=[report.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_report(self):
        report = create_report()
        data = {
            "report_id": "report_id",
            "library": "library",
            "subject_data": "subject_data",
            "column_variable": "column_variable",
            "filter": "filter",
            "stat_label": "stat_label",
            "template": "template",
            "report_type": "report_type",
            "task": create_task().pk,
        }
        url = reverse('studyui_report_update', args=[report.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ReportSegmentViewTest(unittest.TestCase):
    '''
    Tests for ReportSegment
    '''
    def setUp(self):
        self.client = Client()

    def test_list_reportsegment(self):
        url = reverse('studyui_reportsegment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_reportsegment(self):
        url = reverse('studyui_reportsegment_create')
        data = {
            "library": "library",
            "dataset": "dataset",
            "variable": "variable",
            "label": "label",
            "filter": "filter",
            "analysis": "analysis",
            "additional_variables": "additional_variables",
            "special_variables": "special_variables",
            "report": create_report().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_reportsegment(self):
        reportsegment = create_reportsegment()
        url = reverse('studyui_reportsegment_detail', args=[reportsegment.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_reportsegment(self):
        reportsegment = create_reportsegment()
        data = {
            "library": "library",
            "dataset": "dataset",
            "variable": "variable",
            "label": "label",
            "filter": "filter",
            "analysis": "analysis",
            "additional_variables": "additional_variables",
            "special_variables": "special_variables",
            "report": create_report().pk,
        }
        url = reverse('studyui_reportsegment_update', args=[reportsegment.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TitleViewTest(unittest.TestCase):
    '''
    Tests for Title
    '''
    def setUp(self):
        self.client = Client()

    def test_list_title(self):
        url = reverse('studyui_title_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_title(self):
        url = reverse('studyui_title_create')
        data = {
            "text": "text",
            "order": "order",
            "report": create_report().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_title(self):
        title = create_title()
        url = reverse('studyui_title_detail', args=[title.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_title(self):
        title = create_title()
        data = {
            "text": "text",
            "order": "order",
            "report": create_report().pk,
        }
        url = reverse('studyui_title_update', args=[title.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class FootnoteViewTest(unittest.TestCase):
    '''
    Tests for Footnote
    '''
    def setUp(self):
        self.client = Client()

    def test_list_footnote(self):
        url = reverse('studyui_footnote_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_footnote(self):
        url = reverse('studyui_footnote_create')
        data = {
            "text": "text",
            "order": "order",
            "report": create_report().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_footnote(self):
        footnote = create_footnote()
        url = reverse('studyui_footnote_detail', args=[footnote.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_footnote(self):
        footnote = create_footnote()
        data = {
            "text": "text",
            "order": "order",
            "report": create_report().pk,
        }
        url = reverse('studyui_footnote_update', args=[footnote.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MetadataViewTest(unittest.TestCase):
    '''
    Tests for Metadata
    '''
    def setUp(self):
        self.client = Client()

    def test_list_metadata(self):
        url = reverse('studyui_metadata_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_metadata(self):
        url = reverse('studyui_metadata_create')
        data = {
            "parameter_code": "parameter_code",
            "label": "label",
            "description": "description",
            "dataset": "dataset",
            "length": "length",
            "data_type": "data_type",
            "controlled_terms": "controlled_terms",
            "adam_class": "adam_class",
            "category": "category",
            "sub_category": "sub_category",
            "variable_name": "variable_name",
            "task": create_task().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_metadata(self):
        metadata = create_metadata()
        url = reverse('studyui_metadata_detail', args=[metadata.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_metadata(self):
        metadata = create_metadata()
        data = {
            "parameter_code": "parameter_code",
            "label": "label",
            "description": "description",
            "dataset": "dataset",
            "length": "length",
            "data_type": "data_type",
            "controlled_terms": "controlled_terms",
            "adam_class": "adam_class",
            "category": "category",
            "sub_category": "sub_category",
            "variable_name": "variable_name",
            "task": create_task().pk,
        }
        url = reverse('studyui_metadata_update', args=[metadata.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ReportSegmentDetailViewTest(unittest.TestCase):
    '''
    Tests for ReportSegmentDetail
    '''
    def setUp(self):
        self.client = Client()

    def test_list_reportsegmentdetail(self):
        url = reverse('studyui_reportsegmentdetail_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_reportsegmentdetail(self):
        url = reverse('studyui_reportsegmentdetail_create')
        data = {
            "name": "name",
            "value": "value",
            "description": "description",
            "order": "order",
            "reportsegment": create_reportsegment().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_reportsegmentdetail(self):
        reportsegmentdetail = create_reportsegmentdetail()
        url = reverse('studyui_reportsegmentdetail_detail', args=[reportsegmentdetail.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_reportsegmentdetail(self):
        reportsegmentdetail = create_reportsegmentdetail()
        data = {
            "name": "name",
            "value": "value",
            "description": "description",
            "order": "order",
            "reportsegment": create_reportsegment().pk,
        }
        url = reverse('studyui_reportsegmentdetail_update', args=[reportsegmentdetail.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ReportHeaderViewTest(unittest.TestCase):
    '''
    Tests for ReportHeader
    '''
    def setUp(self):
        self.client = Client()

    def test_list_reportheader(self):
        url = reverse('studyui_reportheader_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_reportheader(self):
        url = reverse('studyui_reportheader_create')
        data = {
            "name": "name",
            "description": "description",
            "task": create_task().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_reportheader(self):
        reportheader = create_reportheader()
        url = reverse('studyui_reportheader_detail', args=[reportheader.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_reportheader(self):
        reportheader = create_reportheader()
        data = {
            "name": "name",
            "description": "description",
            "task": create_task().pk,
        }
        url = reverse('studyui_reportheader_update', args=[reportheader.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ReportHeaderDetailViewTest(unittest.TestCase):
    '''
    Tests for ReportHeaderDetail
    '''
    def setUp(self):
        self.client = Client()

    def test_list_reportheaderdetail(self):
        url = reverse('studyui_reportheaderdetail_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_reportheaderdetail(self):
        url = reverse('studyui_reportheaderdetail_create')
        data = {
            "name": "name",
            "column_condition": "column_condition",
            "column_order": "column_order",
            "column_label": "column_label",
            "reportheader": create_reportheader().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_reportheaderdetail(self):
        reportheaderdetail = create_reportheaderdetail()
        url = reverse('studyui_reportheaderdetail_detail', args=[reportheaderdetail.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_reportheaderdetail(self):
        reportheaderdetail = create_reportheaderdetail()
        data = {
            "name": "name",
            "column_condition": "column_condition",
            "column_order": "column_order",
            "column_label": "column_label",
            "reportheader": create_reportheader().pk,
        }
        url = reverse('studyui_reportheaderdetail_update', args=[reportheaderdetail.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ReportSubsetViewTest(unittest.TestCase):
    '''
    Tests for ReportSubset
    '''
    def setUp(self):
        self.client = Client()

    def test_list_reportsubset(self):
        url = reverse('studyui_reportsubset_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_reportsubset(self):
        url = reverse('studyui_reportsubset_create')
        data = {
            "name": "name",
            "population_subset": "population_subset",
            "analysis_subset": "analysis_subset",
            "population_title": "population_title",
            "analysis_title": "analysis_title",
            "description": "description",
            "report": create_report().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_reportsubset(self):
        reportsubset = create_reportsubset()
        url = reverse('studyui_reportsubset_detail', args=[reportsubset.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_reportsubset(self):
        reportsubset = create_reportsubset()
        data = {
            "name": "name",
            "population_subset": "population_subset",
            "analysis_subset": "analysis_subset",
            "population_title": "population_title",
            "analysis_title": "analysis_title",
            "description": "description",
            "report": create_report().pk,
        }
        url = reverse('studyui_reportsubset_update', args=[reportsubset.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


