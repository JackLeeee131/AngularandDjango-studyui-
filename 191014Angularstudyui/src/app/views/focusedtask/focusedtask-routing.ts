import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { FocusedtaskComponent} from './focusedtask.component';

const routes: Routes = [
  {
    path: '',
    component: FocusedtaskComponent,
    data: {
      title: 'FocusedTask'
    }
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class FocosedTaskRoutingModule {}
