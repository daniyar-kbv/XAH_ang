import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { PostComponent } from './post/post.component';
import { CategoryComponent } from './category/category.component';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { CommentsComponent } from './comments/comments.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from "@angular/common/http";




@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    PostComponent,
    CategoryComponent,
    LoginComponent,
    RegistrationComponent,
    CommentsComponent,
  ],
  imports: [
    NgbModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
