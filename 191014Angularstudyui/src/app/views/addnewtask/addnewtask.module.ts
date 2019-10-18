import { NgModule } from '@angular/core';

import { AddnewtaskComponent } from './addnewtask.component';
import { AddNewTaskRoutingModule } from './addnewtask-routing.module';

@NgModule({
  imports: [
    AddNewTaskRoutingModule,
  ],
  declarations: [ AddnewtaskComponent ]
})
export class AddNewTaskModule { }
