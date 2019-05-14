import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {IArticle} from '../shared/models/article';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {
  public articles: IArticle[] = [];
  public articlesAuto: IArticle[] = [];
  public articlesBusiness: IArticle[] = [];
  public articlesSport: IArticle[] = [];
  public articlesDate: IArticle[] = [];

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getArticlesByViews().then(res => {
      this.articles = res;
    });
    // this.provider.getArticlesAutoViews().then(res => {
    //   this.articlesAuto = res;
    // });
    // this.provider.getArticlesBusinessViews().then(res => {
    //   this.articlesBusiness = res;
    // });
    // this.provider.getArticlesSportViews().then(res => {
    //   this.articlesSport = res;
    // });
    // this.provider.getArticlesDate().then(res => {
    //   this.articlesDate = res;
    // })
  }

}
