from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'molecule', api.MoleculeViewSet)
router.register(r'trial', api.TrialViewSet)
router.register(r'task', api.TaskViewSet)
router.register(r'report', api.ReportViewSet)
router.register(r'reportsegment', api.ReportSegmentViewSet)
router.register(r'title', api.TitleViewSet)
router.register(r'footnote', api.FootnoteViewSet)
router.register(r'metadata', api.MetadataViewSet)
router.register(r'reportsegmentdetail', api.ReportSegmentDetailViewSet)
router.register(r'reportheader', api.ReportHeaderViewSet)
router.register(r'reportheaderdetail', api.ReportHeaderDetailViewSet)
router.register(r'reportsubset', api.ReportSubsetViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Molecule
    path('studyui/molecule/', views.MoleculeListView.as_view(), name='studyui_molecule_list'),
    path('studyui/molecule/create/', views.MoleculeCreateView.as_view(), name='studyui_molecule_create'),
    path('studyui/molecule/detail/<int:pk>/', views.MoleculeDetailView.as_view(), name='studyui_molecule_detail'),
    path('studyui/molecule/update/<int:pk>/', views.MoleculeUpdateView.as_view(), name='studyui_molecule_update'),
)

urlpatterns += (
    # urls for Trial
    path('studyui/trial/', views.TrialListView.as_view(), name='studyui_trial_list'),
    path('studyui/trial/create/', views.TrialCreateView.as_view(), name='studyui_trial_create'),
    path('studyui/trial/detail/<int:pk>/', views.TrialDetailView.as_view(), name='studyui_trial_detail'),
    path('studyui/trial/update/<int:pk>/', views.TrialUpdateView.as_view(), name='studyui_trial_update'),
)

urlpatterns += (
    # urls for Task
    path('studyui/task/', views.TaskListView.as_view(), name='studyui_task_list'),
    path('studyui/task/create/', views.TaskCreateView.as_view(), name='studyui_task_create'),
    path('studyui/task/detail/<int:pk>/', views.TaskDetailView.as_view(), name='studyui_task_detail'),
    path('studyui/task/update/<int:pk>/', views.TaskUpdateView.as_view(), name='studyui_task_update'),
)

urlpatterns += (
    # urls for Report
    path('studyui/report/', views.ReportListView.as_view(), name='studyui_report_list'),
    path('studyui/report/create/', views.ReportCreateView.as_view(), name='studyui_report_create'),
    path('studyui/report/detail/<int:pk>/', views.ReportDetailView.as_view(), name='studyui_report_detail'),
    path('studyui/report/update/<int:pk>/', views.ReportUpdateView.as_view(), name='studyui_report_update'),
)

urlpatterns += (
    # urls for ReportSegment
    path('studyui/reportsegment/', views.ReportSegmentListView.as_view(), name='studyui_reportsegment_list'),
    path('studyui/reportsegment/create/', views.ReportSegmentCreateView.as_view(), name='studyui_reportsegment_create'),
    path('studyui/reportsegment/detail/<int:pk>/', views.ReportSegmentDetailView.as_view(), name='studyui_reportsegment_detail'),
    path('studyui/reportsegment/update/<int:pk>/', views.ReportSegmentUpdateView.as_view(), name='studyui_reportsegment_update'),
)

urlpatterns += (
    # urls for Title
    path('studyui/title/', views.TitleListView.as_view(), name='studyui_title_list'),
    path('studyui/title/create/', views.TitleCreateView.as_view(), name='studyui_title_create'),
    path('studyui/title/detail/<int:pk>/', views.TitleDetailView.as_view(), name='studyui_title_detail'),
    path('studyui/title/update/<int:pk>/', views.TitleUpdateView.as_view(), name='studyui_title_update'),
)

urlpatterns += (
    # urls for Footnote
    path('studyui/footnote/', views.FootnoteListView.as_view(), name='studyui_footnote_list'),
    path('studyui/footnote/create/', views.FootnoteCreateView.as_view(), name='studyui_footnote_create'),
    path('studyui/footnote/detail/<int:pk>/', views.FootnoteDetailView.as_view(), name='studyui_footnote_detail'),
    path('studyui/footnote/update/<int:pk>/', views.FootnoteUpdateView.as_view(), name='studyui_footnote_update'),
)

urlpatterns += (
    # urls for Metadata
    path('studyui/metadata/', views.MetadataListView.as_view(), name='studyui_metadata_list'),
    path('studyui/metadata/create/', views.MetadataCreateView.as_view(), name='studyui_metadata_create'),
    path('studyui/metadata/detail/<int:pk>/', views.MetadataDetailView.as_view(), name='studyui_metadata_detail'),
    path('studyui/metadata/update/<int:pk>/', views.MetadataUpdateView.as_view(), name='studyui_metadata_update'),
)

urlpatterns += (
    # urls for ReportSegmentDetail
    path('studyui/reportsegmentdetail/', views.ReportSegmentDetailListView.as_view(), name='studyui_reportsegmentdetail_list'),
    path('studyui/reportsegmentdetail/create/', views.ReportSegmentDetailCreateView.as_view(), name='studyui_reportsegmentdetail_create'),
    path('studyui/reportsegmentdetail/detail/<int:pk>/', views.ReportSegmentDetailDetailView.as_view(), name='studyui_reportsegmentdetail_detail'),
    path('studyui/reportsegmentdetail/update/<int:pk>/', views.ReportSegmentDetailUpdateView.as_view(), name='studyui_reportsegmentdetail_update'),
)

urlpatterns += (
    # urls for ReportHeader
    path('studyui/reportheader/', views.ReportHeaderListView.as_view(), name='studyui_reportheader_list'),
    path('studyui/reportheader/create/', views.ReportHeaderCreateView.as_view(), name='studyui_reportheader_create'),
    path('studyui/reportheader/detail/<int:pk>/', views.ReportHeaderDetailView.as_view(), name='studyui_reportheader_detail'),
    path('studyui/reportheader/update/<int:pk>/', views.ReportHeaderUpdateView.as_view(), name='studyui_reportheader_update'),
)

urlpatterns += (
    # urls for ReportHeaderDetail
    path('studyui/reportheaderdetail/', views.ReportHeaderDetailListView.as_view(), name='studyui_reportheaderdetail_list'),
    path('studyui/reportheaderdetail/create/', views.ReportHeaderDetailCreateView.as_view(), name='studyui_reportheaderdetail_create'),
    path('studyui/reportheaderdetail/detail/<int:pk>/', views.ReportHeaderDetailDetailView.as_view(), name='studyui_reportheaderdetail_detail'),
    path('studyui/reportheaderdetail/update/<int:pk>/', views.ReportHeaderDetailUpdateView.as_view(), name='studyui_reportheaderdetail_update'),
)

urlpatterns += (
    # urls for ReportSubset
    path('studyui/reportsubset/', views.ReportSubsetListView.as_view(), name='studyui_reportsubset_list'),
    path('studyui/reportsubset/create/', views.ReportSubsetCreateView.as_view(), name='studyui_reportsubset_create'),
    path('studyui/reportsubset/detail/<int:pk>/', views.ReportSubsetDetailView.as_view(), name='studyui_reportsubset_detail'),
    path('studyui/reportsubset/update/<int:pk>/', views.ReportSubsetUpdateView.as_view(), name='studyui_reportsubset_update'),
)

