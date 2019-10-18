# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import subprocess as sp
from time import sleep
from import_export import resources
from .models import Report, Task
import gitlab, os
from subprocess import run

ROOT_FOLDER = "/home/raj-vm/Projects/clinroot/"
SAS_FOLDER = '/home/raj-vm/Projects/mlytics_studio/sas/*'
PRIVATE_TOKEN = 'zPgnAs5jvxu_eb7yhodx'
USER_NAME = "raj"


class ReportResource(resources.ModelResource):
    class Meta:
        model = Report


@shared_task
def csv2sas(ids):
    queryset = Report.objects.filter(id__in=ids)
    # projects = list(queryset.values_list('task__name', flat=True))
    # login session
    gl = gitlab.Gitlab('http://cde.mlyticsstudio.com/', private_token=PRIVATE_TOKEN)
    # for each unique task
    for t in queryset.order_by('task_id').values_list('task_id',flat=True).distinct('task_id'):
        # project name: Molecule-Trial-Task
        task_obj = Task.objects.get(id=t)
        project_name = dict(name=str(task_obj.__str__()))
        project_path = os.path.join(ROOT_FOLDER, '/'.join(str(task_obj.__str__()).split('-')))

        if not os.path.exists(project_path):
            try:
                os.makedirs(project_path)
            except OSError:
                print("Creation of the project directory %s failed." % project_path)
            else:
                print("Successfully created the project directory %s. " % project_path)

        try:
            p = gl.projects.create(project_name)

        except ValueError:
            print("Creation of the project %s failed." % project_name)

        else:
            print("Successfully created the project %s. " % project_name)

        # for each task, find all the reports and export in the corresponding folder
        rpt = task_obj.reports.filter(template=False)
        dataset = ReportResource().export(queryset=rpt)
        dataset.df.to_csv(os.path.join(project_path,'export.csv'))
        # copy sas programs to the project
        run(['cp -R '+SAS_FOLDER+' '+project_path], shell=True)
        run(['cp', '-r', './sas/*', project_path])
        # init version control
        run(['git', 'init'], cwd=project_path)
        # add user name and access token to repo
        repo = p.http_url_to_repo.split('//')[0]+'//'+USER_NAME+':'+PRIVATE_TOKEN+'@'+p.http_url_to_repo.split('//')[1]
        run(['git', 'remote', 'add', 'origin', repo], cwd=project_path)
        run(['git', 'add',  '.'], cwd=project_path)
        run(['git', 'commit', '-m "Initial commit"'], cwd=project_path)
        run(['git', 'push', '-u', 'origin', 'master'], cwd=project_path)



