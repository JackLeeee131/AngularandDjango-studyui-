import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ChartsModule } from 'ng2-charts';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { ButtonsModule } from 'ngx-bootstrap/buttons';

import { RecenttaskComponent } from './recenttask.component';
import { RecenttaskRoutingModule } from './recenttask-routing.module';

@NgModule({
  imports: [
    FormsModule,
    RecenttaskRoutingModule,
    ChartsModule,
    BsDropdownModule,
    ButtonsModule.forRoot()
  ],
  declarations: [ RecenttaskComponent ]
})
export class RecentTaskModule { }
