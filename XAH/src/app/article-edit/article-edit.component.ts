import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProviderService } from '../shared/services/provider.service';

@Component({
  selector: 'app-article-edit',
  templateUrl: './article-edit.component.html',
  styleUrls: ['./article-edit.component.scss']
})
export class ArticleEditComponent implements OnInit {

  private TOKEN = 'Token';
  private IMAGE_URL = 'http://127.0.0.1:8887/articles/';

  public logged = false;

  private articleId: string;
  public title: string = '';
  public body: string = '';
  public category: string = '';
  public image_url: any = '';

  constructor(private provider: ProviderService, private route: ActivatedRoute) { }

  ngOnInit() {
    this.articleId = this.route.snapshot.paramMap.get('articleId');
    const token = localStorage.getItem(this.TOKEN);
    if (token) {
      this.logged = true;
    }
    if(this.logged) {
      this.provider.getArticle(this.articleId).then(res => {
        this.title = res.title;
        this.body = res.body;
        this.category = this.getCategory(res.category);
        this.image_url = res.image_url;
      })
    }
  }
  getCategory(category: string) {
    if(category === "Auto") return '1';
    else if(category === "Business") return '2';
    else return '3';
  }
  edit(title: string, body: string, category: any, image_url: any) {
    if(image_url != '') this.image_url = this.IMAGE_URL + image_url.replace(/^.*[\\\/]/, '');
    this.provider.updateArticle(this.articleId, title, body, category, this.image_url).then(res => {
      console.log("Article updated");
    });
  }
}
