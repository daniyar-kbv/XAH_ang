import { Component, OnInit } from '@angular/core';
import { IArticle } from "../shared/models/article";
import { ProviderService } from "../shared/services/provider.service";

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.scss']
})
export class PostComponent implements OnInit {
  public current_article: IArticle;
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getArticle().then(res => {
      this.current_article = res;
    })
  }

  putLike() {
    this.provider.putLike();
  }
}
