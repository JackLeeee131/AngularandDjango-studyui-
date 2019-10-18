import { NgModule } from '@angular/core';
import {Routes, RouterModule } from '@angular/router';
import {MergeComponent} from './merge.component';

const routes: Routes = [
    {
        path:'',
        component: MergeComponent,
        data: {
            title:'Merge'
        }
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
  })

export class MergeRoutingModule {}