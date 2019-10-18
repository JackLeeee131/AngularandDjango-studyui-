import django
from django.contrib import admin
from django.urls import reverse, path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django import forms
from import_export.admin import ImportExportModelAdmin
from .models import Molecule, Trial, Task, Report, Template, ReportSegment, Title, Footnote, Metadata, ReportSegmentDetail, \
    ReportHeader, ReportHeaderDetail, ReportSubset
import copy
import modelclone
from django.contrib.admin.helpers import ActionForm
from django import forms
from import_export import resources
from .tasks import csv2sas


admin.site.site_header = "MLytics Studio"
admin.site.site_title = "MLytics Studio"

from django.contrib.admin import AdminSite

class RawAdminSite(AdminSite):
    site_header = "MLyticsAdmin"
    site_title = "MLyticsAdmin"
    index_title = "MLyticsAdmin"


raw_admin_site = RawAdminSite(name='raw_admin')

raw_admin_site.register(Molecule)
raw_admin_site.register(Trial)
raw_admin_site.register(Task)

#######################
# Inline models
#######################

class TrialInline(admin.StackedInline):
    model = Trial
    extra = 0


class TaskInline(admin.StackedInline):
    model = Task
    extra = 0


class ReportInline(admin.StackedInline):
    model = Report
    extra = 0


class ReportSegmentInline(admin.StackedInline):
    model = ReportSegment
    extra = 0


class TitleInline(admin.StackedInline):
    model = Title
    extra = 0


class FootnoteInline(admin.StackedInline):
    model = Footnote
    extra = 0


class MetadataInline(admin.StackedInline):
    model = Metadata
    extra = 0


class ReportSegmentDetailInline(admin.StackedInline):
    model = ReportSegmentDetail
    extra = 0


class ReportHeaderInline(admin.StackedInline):
    model = ReportHeader
    extra = 0


class ReportHeaderDetailInline(admin.StackedInline):
    model = ReportHeaderDetail
    extra = 0


class ReportSubsetInline(admin.StackedInline):
    model = ReportSubset
    extra = 0


#######################
# End Inline Models
#######################


#######################
# Model forms
#######################


class MoleculeAdminForm(forms.ModelForm):
    class Meta:
        model = Molecule
        fields = '__all__'


class TrialAdminForm(forms.ModelForm):
    class Meta:
        model = Trial
        fields = '__all__'


class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class ReportAdminForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

class TemplateAdminForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'


class ReportSegmentAdminForm(forms.ModelForm):
    class Meta:
        model = ReportSegment
        fields = '__all__'


class TitleAdminForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = '__all__'


class FootnoteAdminForm(forms.ModelForm):
    class Meta:
        model = Footnote
        fields = '__all__'


class MetadataAdminForm(forms.ModelForm):
    class Meta:
        model = Metadata
        fields = '__all__'


class ReportSegmentDetailAdminForm(forms.ModelForm):
    class Meta:
        model = ReportSegmentDetail
        fields = '__all__'


class ReportHeaderAdminForm(forms.ModelForm):
    class Meta:
        model = ReportHeader
        fields = '__all__'


class ReportHeaderDetailAdminForm(forms.ModelForm):
    class Meta:
        model = ReportHeaderDetail
        fields = '__all__'


class ReportSubsetAdminForm(forms.ModelForm):
    class Meta:
        model = ReportSubset
        fields = '__all__'


#######################
# End Model forms
#######################

@admin.register(Molecule)
class MoleculeAdmin(ImportExportModelAdmin):
    form = MoleculeAdminForm
    save_as = True
    save_as_continue = True

    list_display = ['name', 'created', 'last_updated', 'description']
    list_filter = ['last_updated']
    list_per_page = 25
    inlines = [
        TrialInline,
    ]


@admin.register(Trial)
class TrialAdmin(ImportExportModelAdmin):
    form = TrialAdminForm
    list_display = ['name', 'phase', 'indication', 'crossover', 'output_type', 'protocol', 'sap', 'created',
                    'last_updated', 'description']

    inlines = [
        TaskInline,
    ]


@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    form = TaskAdminForm
    list_display = ['name', 'location', 'created', 'last_updated', 'description']


class ReportResource(resources.ModelResource):
    class Meta:
        model = Report


@admin.register(Report)
class ReportAdmin(ImportExportModelAdmin):
    # change the default template to add a custom link 'Generate Programs'
    # change_list_template = "studyui/change_list.html"
    form = ReportAdminForm
    view_on_site = False
    save_as = True
    save_as_continue = True
    list_display = ['report_id', 'created', 'last_updated', 'library', 'subject_data', 'column_variable', 'filter',
                    'stat_label', 'report_type', 'task']

    # having task as filter is time consuming
    # list_filter = ['last_updated', ('task', admin.RelatedOnlyFieldListFilter)]
    list_filter = ['last_updated', 'task']
    list_per_page = 20

    # had to use an admin action because queryset was not accessible
    # override the method to add custom link URL 'Generate Programs'
    # def get_urls(self):
    #     urls = super().get_urls()
    #     my_urls = [
    #         path('genpgms/', self.generate_programs),
    #     ]
    #     return my_urls + urls

    # create a method to handle the custom link 'Generate Programs'
    def generate_programs(self, request, queryset):
        from django.core import serializers
        # data = serializers.serialize("json", queryset.objects.all())
        ids = list(queryset.values_list('id', flat=True))
        print("Test of IDS: " + str(ids))
        csv2sas.delay(ids)
        # csv2sas.delay(queryset=queryset)
        # self.model.objects.all().update(column_variable='trt01p')
        self.message_user(request, "Programs will be generated")
        return HttpResponseRedirect(request.get_full_path())

    actions = ['generate_programs']

    # class CopyTemplateForm(ActionForm):
    #     task_new = forms.ModelChoiceField(queryset=Task.objects.all(), required=False)
    #
    # action_form = CopyTemplateForm

    # def copy_reports(self, request, queryset):
    #     task_new = request.POST['task_new']
    #     # queryset.update(task_id=task_new)
    #     num_of_reports = 0
    #     for temp in queryset:
    #         temp_copy = copy.deepcopy(temp)
    #         temp_copy.id = None
    #         temp_copy.task_id = task_new
    #         temp_copy.save()
    #         num_of_reports += 1
    #         # copy all the report segments
    #         for segs in temp.reportsegments.all():
    #             segs.id = None
    #             segs.save()
    #             temp_copy.reportsegments.add(segs)
    #
    #     self.message_user(request, str(num_of_reports)+" report(s) successfully copied.")
    #
    #     return HttpResponseRedirect(request.get_full_path())
    # copy_reports.short_description = "Copy selected Reports"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(template=False)

    def children_display(self, obj):
        return ", ".join([
            seg.label for seg in obj.reportsegments.all()
        ])
    children_display.short_description = "Children"

    inlines = [
        ReportSegmentInline,
        # ReportSegmentDetailInline,
        TitleInline,
        FootnoteInline,
        ReportSubsetInline,
        # ReportHeaderInline,
        # ReportHeaderDetail,

    ]



@admin.register(Template)
class TemplateAdmin(ImportExportModelAdmin):
    form = ReportAdminForm
    view_on_site = False
    list_display = ['report_id', 'created', 'last_updated', 'library', 'subject_data', 'column_variable', 'filter',
                    'stat_label', 'report_type', 'task', 'children_display']

    list_filter = ['last_updated', 'report_type']

    list_per_page = 25

    actions = ['copy_templates']

    class CopyTemplateForm(ActionForm):
        task_new = forms.ModelChoiceField(queryset=Task.objects.all(),required=False)

    action_form = CopyTemplateForm

    def copy_templates(self, request, queryset):
        task_new = request.POST['task_new']
        # queryset.update(task_id=task_new)
        print("Testing the copy_template method: task selected-" + str(task_new))
        for temp in queryset:
            temp_copy = copy.deepcopy(temp)
            print("Id value before save: " + str(temp_copy.id))
            temp_copy.id = None
            temp_copy.task_id = task_new
            temp_copy.template = False
            temp_copy.save()
            # copy all the report segments
            for segs in temp.reportsegments.all():
                segs.id = None
                segs.save()
                temp_copy.reportsegments.add(segs)

        self.message_user(request, "Successfully copied.")

        return HttpResponseRedirect(request.get_full_path())

        # if not form:
        #     form = self.CopyTemplateForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        #
        # return render('admin/studyui/copy_template.html', {'articles': queryset, 'tag_form': form,})
        # if rows_updated == 1:
        #     message_bit = "1 template was"
        # else:
        #     message_bit = "%s templates were" % rows_updated
        # self.message_user(request, "%s successfully copied." % message_bit)

    copy_templates.short_description = 'Copy Template'


    def children_display(self, obj):
        display_text = ", ".join([
            "<a href={}>{}</a>".format(
                    reverse('admin:{}_{}_change'.format(obj._meta.app_label, obj._meta.model_name),
                    args=(seg.pk,)),seg.label)
            for seg in obj.reportsegments.all()
        ])
        if display_text:
            return mark_safe(display_text)
        return "-"
        # return ", ".join([
        #     seg.label for seg in obj.reportsegments.all()
        # ])
    children_display.short_description = "Segments"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(template=True)

    inlines = [
        ReportSegmentInline,
        TitleInline,
        FootnoteInline,
    ]


@admin.register(ReportSegment)
class ReportSegmentAdmin(ImportExportModelAdmin):
    form = ReportSegmentAdminForm
    view_on_site = False

    list_display = ['variable', 'created', 'last_updated', 'library', 'dataset', 'label', 'filter', 'analysis',
                    'additional_variables', 'special_variables']
    inlines = [
        ReportSegmentDetailInline,
    ]


#@admin.register(Title)
class TitleAdmin(ImportExportModelAdmin):
    form = TitleAdminForm
    list_display = ['text', 'created', 'last_updated', 'order']


# @admin.register(Footnote)
class FootnoteAdmin(ImportExportModelAdmin):
    form = FootnoteAdminForm
    list_display = ['text', 'created', 'last_updated', 'order']


# @admin.register(Metadata)
class MetadataAdmin(ImportExportModelAdmin):
    form = MetadataAdminForm
    list_display = ['parameter_code', 'created', 'last_updated', 'label', 'description', 'dataset', 'length',
                    'data_type', 'controlled_terms', 'adam_class', 'category', 'sub_category', 'variable_name']


# @admin.register(ReportSegmentDetail)
class ReportSegmentDetailAdmin(ImportExportModelAdmin):
    form = ReportSegmentDetailAdminForm
    list_display = ['name', 'created', 'last_updated', 'value', 'description', 'order']


@admin.register(ReportHeader)
class ReportHeaderAdmin(ImportExportModelAdmin):
    form = ReportHeaderAdminForm
    list_display = ['name', 'created', 'last_updated', 'description']
    inlines = [
        ReportHeaderDetailInline
    ]


# @admin.register(ReportHeaderDetail)
class ReportHeaderDetailAdmin(ImportExportModelAdmin):
    form = ReportHeaderDetailAdminForm
    list_display = ['name', 'created', 'last_updated', 'column_condition', 'column_order', 'column_label']


# @admin.register(ReportSubset)
class ReportSubsetAdmin(ImportExportModelAdmin):
    form = ReportSubsetAdminForm
    list_display = ['name', 'created', 'last_updated', 'population_subset', 'analysis_subset', 'population_title',
                    'analysis_title', 'description']
