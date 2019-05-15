import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { IArticle } from '../shared/models/article';


@Component({
  selector: 'app-my-articles',
  templateUrl: './my-articles.component.html',
  styleUrls: ['./my-articles.component.sass']
})
export class MyArticlesComponent implements OnInit {

  private TOKEN = 'Token';

  public logged = false;

  public articles: IArticle[] = [];

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem(this.TOKEN);
    if (token) {
      this.logged = true;
    }
    if(this.logged) {
      this.provider.getArticlesByUser().then(res => {
        this.articles = res;
        console.log(res);
      });
    }
  }
  delete(articleId: number) {
    this.provider.deleteArticle(articleId).then(res => {
      console.log("deleted article!");
    })
  }
}
