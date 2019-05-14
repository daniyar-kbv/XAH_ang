import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { IAuthResponse } from '../models/authResponse';
import {IArticle} from '../models/article';
import {IComment} from '../models/comment';
import {IUser} from '../models/user';


@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  private baseUrl = 'http://127.0.0.1:8000/api/';

  constructor(http: HttpClient) {
    super(http);
  }

  getComments(articleId: any): Promise<IComment[]> {
    return this.get(this.baseUrl + `articles/${articleId}/comments/?ordering=-date_published`, {});
  }

  createComment(body: string, articleId: any): Promise<IComment> {
    return this.post(this.baseUrl + `articles/${articleId}/comments/create/`, {
      body
    });
  }

  login(username: any, password: any): Promise<IAuthResponse> {
    return this.post( this.baseUrl + 'login/', {
      username,
      password
    });
  }

  register(username: any, password: any, email: any): Promise<IUser> {
    return this.post(  this.baseUrl + 'register/', {
      username,
      password,
      email
    });
  }

  logout(): Promise<any> {
    return this.post(this.baseUrl + 'logout/', {});
  }

  getArticlesByViews(): Promise<IArticle[]> {
    return this.get(this.baseUrl + 'articles/?ordering=-views', {});
  }

  getArticlesAutoViews(): Promise<IArticle[]>{
    return this.get(this.baseUrl + 'articles/?ordering=-views&?category=1', {});
  }

  getArticlesBusinessViews(): Promise<IArticle[]>{
    return this.get(this.baseUrl + 'articles/?ordering=-views&?category=2', {});
  }

  getArticlesSportViews(): Promise<IArticle[]>{
    return this.get(this.baseUrl + 'articles/?ordering=-views&?category=3', {});
  }

  getArticlesDate(): Promise<IArticle[]>{
    return this.get(this.baseUrl + 'articles/?ordering=-created_at', {});
  }

  getArticle(articleId): Promise<IArticle> {
    return this.get(this.baseUrl  + `articles/${articleId}/`, {});
  }

  putArticleLike() {
    return this.post(this.baseUrl  + 'articles/4/likes/', {});
  }

  getArticleLikes() {
    return this.get(this.baseUrl  + 'articles/4/likes/', {});
  }

  createArticle(title, body, category, image_url): Promise<any>{
    return this.post(this.baseUrl + `articles/create/`, {
      title: title,
      body: body,
      image_url: image_url,
      category: category
    })
  }
  updateArticle(articleId, title, body, category, image_url): Promise<any> {
    return this.put(this.baseUrl + `articles/${articleId}/update/`, {
      title: title,
      body: body,
      image_url: image_url,
      category: category
    })
  }
  deleteArticle(articleId): Promise<any> {
    return this.delete(this.baseUrl + `articles/${articleId}/delete/`, {});
  }

  putLike() {
    return this.post(`http://localhost:8000/api/articles/1/likes/`, {})
  }

  deleteArticleLike() {
    return this.delete(this.baseUrl  + 'articles/4/likes/', {});
  }

  putCommentLike() {
    return this.post(this.baseUrl  + 'comments/1/likes/', {});
  }

  getCommentLikes() {
    return this.get(`http://localhost:8000/api/comments/1/likes/`, {})
  }
}
