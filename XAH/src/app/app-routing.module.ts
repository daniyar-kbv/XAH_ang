import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MainComponent } from './main/main.component';
import { PostComponent } from './post/post.component';
import { CategoryComponent } from './category/category.component';

const routes: Routes = [
    { path: 'main', component: MainComponent },
    { path: 'post', component: PostComponent },
    { path: 'category', component: CategoryComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
