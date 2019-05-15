import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';

@Component({
  selector: 'app-article-create',
  templateUrl: './article-create.component.html',
  styleUrls: ['./article-create.component.scss']
})
export class ArticleCreateComponent implements OnInit {

  private TOKEN = 'Token';
  private IMAGE_URL = 'http://127.0.0.1:8887/articles/';

  public logged = false;

  public title: string = '';
  public body: string = '';
  public category: string = '1';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem(this.TOKEN);
    if (token) {
      this.logged = true;
    }
  }
  create(image_url: string) {
    let url = this.IMAGE_URL + image_url.replace(/^.*[\\\/]/, '');
    this.provider.createArticle(this.title, this.body, this.category, url).then(res => {
      console.log("Created article!");
    });
  }
}
