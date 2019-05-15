import { BrowserModule } from '@angular/platform-browser';
import { NgModule, ClassProvider } from '@angular/core';
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
import { AuthInterceptor } from './AuthInterceptor';
import { ProviderService } from './shared/services/provider.service';
import { FormsModule } from '@angular/forms';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { ArticleCreateComponent } from './article-create/article-create.component';
import { MyArticlesComponent } from './my-articles/my-articles.component';
import { ArticleEditComponent } from './article-edit/article-edit.component';
import { CommentComponent } from './comment/comment.component';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    PostComponent,
    CategoryComponent,
    LoginComponent,
    RegistrationComponent,
    CommentsComponent,
    HeaderComponent,
    FooterComponent,
    ArticleCreateComponent,
    MyArticlesComponent,
    ArticleEditComponent,
    CommentComponent,
  ],
  imports: [
    NgbModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [
    ProviderService,
    <ClassProvider> {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
