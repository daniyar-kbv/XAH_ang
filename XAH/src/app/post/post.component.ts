import { Component, OnInit } from '@angular/core';
import { IArticle } from '../shared/models/article';
import { IArticleLike } from '../shared/models/articleLike';
import { ProviderService } from '../shared/services/provider.service';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.scss']
})

export class PostComponent implements OnInit {
  public currentArticle: IArticle;
  public likes: IArticleLike[] = [];
  public isLiked = false;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getArticle(1).then(res => {
      this.currentArticle = res;
      this.provider.getArticleLikes().then(res1 => {
        this.likes = res1;
      });
    });
  }

  putArticleLike() {
    this.provider.putArticleLike().then(res => {
      console.log(res)
      this.likes.push(res);
      this.isLiked = true;
    }).catch((err) => {
      this.provider.deleteArticleLike();
      this.likes.pop();
      console.log(err);
      this.isLiked = false;
  });
  }
}
