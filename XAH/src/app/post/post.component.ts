import { Component, OnInit } from '@angular/core';
import { IArticle } from '../shared/models/article';
import { IArticleLike } from '../shared/models/articleLike';
import { ProviderService } from '../shared/services/provider.service';
import {tryCatch} from 'rxjs/internal-compatibility';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.scss']
})

export class PostComponent implements OnInit {
  public currentArticle: IArticle;
  public likes: IArticleLike[] = [];


  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getArticle().then(res => {
      this.currentArticle = res;
      this.provider.getArticleLikes().then(res1 => {
        this.likes = res1;
      });
    });
  }

  putArticleLike() {
    this.provider.putArticleLike().then(res => {
      this.likes.push(res);
    }).catch( res => {
      this.likes.pop();
    });
  }
}
