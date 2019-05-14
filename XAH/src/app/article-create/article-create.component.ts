import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';

@Component({
  selector: 'app-article-create',
  templateUrl: './article-create.component.html',
  styleUrls: ['./article-create.component.scss']
})
export class ArticleCreateComponent implements OnInit {
  public title: string = '';
  public body: string = '';
  public category: string = '';
  // public imageUrl:
  public path: any;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
  }

}
