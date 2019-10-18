import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AddnewtaskComponent} from './addnewtask.component';

const routes: Routes = [
  {
    path: '',
    component: AddnewtaskComponent,
    data: {
      title: 'RecentTask'
    }
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AddNewTaskRoutingModule {}
