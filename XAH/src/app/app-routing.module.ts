import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MainComponent } from './main/main.component';
import { PostComponent } from './post/post.component';
import { CategoryComponent } from './category/category.component';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import {ArticleCreateComponent} from './article-create/article-create.component';
import { ArticleEditComponent } from './article-edit/article-edit.component';

const routes: Routes = [
    { 
        path: '',
        redirectTo: '/main',
        pathMatch: 'full'
    },
    { path: 'main', component: MainComponent },
    { path: 'post/:articleId', component: PostComponent },
    { path: 'post', component: PostComponent },
    { path: 'category', component: CategoryComponent },
    { path: 'login', component: LoginComponent },
    { path: 'registration', component: RegistrationComponent },
    { path: 'article_create', component: ArticleCreateComponent },
    { path: 'article_edit/:articleId', component: ArticleEditComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
