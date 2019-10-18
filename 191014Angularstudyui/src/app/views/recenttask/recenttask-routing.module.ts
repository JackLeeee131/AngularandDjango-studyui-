import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { RecenttaskComponent} from './recenttask.component';

const routes: Routes = [
  {
    path: '',
    component: RecenttaskComponent,
    data: {
      title: 'RecentTask'
    }
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class RecenttaskRoutingModule {}
