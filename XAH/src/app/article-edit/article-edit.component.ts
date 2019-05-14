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
        this.category = res.category;
        this.image_url = res.image_url;
      })
    }
  }
  edit(image_url: any) {

  }
}
