import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {ActivatedRoute} from '@angular/router';
import {IArticle} from '../shared/models/article';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.scss']
})
export class CategoryComponent implements OnInit {

  public categoryId: string = '';
  public articles: IArticle[] = [];

  constructor(private provider: ProviderService, private route: ActivatedRoute) { }


  ngOnInit() {
    const routeParams = this.route.snapshot.params;
    this.route.params.subscribe(routeParams => {
      this.categoryId = this.route.snapshot.paramMap.get('categoryId');
      if (this.categoryId == '1') {
        this.provider.getArticlesAutoDate().then(res => {
          this.articles = res;
        })
      }
      if (this.categoryId == '2'){
        this.provider.getArticlesBusinessDate().then(res => {
          this.articles = res;
        })
      }
      if (this.categoryId == '3') {
        this.provider.getArticlesSportDate().then(res => {
          this.articles = res;
        })
      }
    });
  }

}
