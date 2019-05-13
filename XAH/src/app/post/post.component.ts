import { Component, OnInit } from '@angular/core';
import { IArticle } from "../models/models";

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.scss']
})
export class PostComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  getArticle(article: IArticle){
    this.provider.getArticle(article).then(res => {
      this.current_article = res;
    })
  }
}
