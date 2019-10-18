import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ChartsModule } from 'ng2-charts';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { ButtonsModule } from 'ngx-bootstrap/buttons';

import { FocusedtaskComponent } from './focusedtask.component';
import { FocosedTaskRoutingModule } from './focusedtask-routing';

@NgModule({
  imports: [
    FormsModule,
    FocosedTaskRoutingModule,
    ChartsModule,
    BsDropdownModule,
    ButtonsModule.forRoot()
  ],
  declarations: [ FocusedtaskComponent ]
})
export class FocusedTaskModule { }
