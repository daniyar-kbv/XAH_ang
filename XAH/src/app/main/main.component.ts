import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {IArticle} from '../shared/models/article';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {
  public Articles: IArticle[] = [];

  constructor(private provider: ProviderService) { }

  ngOnInit() {
  }

}
