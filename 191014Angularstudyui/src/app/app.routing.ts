import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

// Import Containers
import { DefaultLayoutComponent } from './containers';

import { LoginComponent } from './views/login/login.component';
import { RegisterComponent } from './views/register/register.component';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full',
  },
  {
    path: 'login',
    component: LoginComponent,
    data: {
      title: 'Login Page'
    }
  },
  {
    path: 'register',
    component: RegisterComponent,
    data: {
      title: 'Register Page'
    }
  },
  {
    path: '',
    component: DefaultLayoutComponent,
    data: {
      title: 'Home'
    },
    children: [
      {
        path: 'dashboard',
        loadChildren: () => import('./views/dashboard/dashboard.module').then(m => m.DashboardModule)
      },

      ////
      {
        path: 'recenttask',
        loadChildren: () => import('./views/recenttask/recenttask.module').then(m => m.RecentTaskModule)
      },
      {
        path: 'focusedTask',
        loadChildren: () => import('./views/focusedtask/focusedtask.module').then(m => m.FocusedTaskModule)
      },
      {
        path: 'addNewTask',
        loadChildren: () => import('./views/addnewtask/addnewtask.module').then(m => m.AddNewTaskModule)
      },
      {
        path: 'merge',
        loadChildren: () => import('./views/merge/merge.module').then(m => m.MergeModele)
      },
      ////
    ]
  },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
