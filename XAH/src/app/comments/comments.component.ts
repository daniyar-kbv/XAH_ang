import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { IComment } from '../shared/models/comment';

@Component({
  selector: 'app-comments',
  templateUrl: './comments.component.html',
  styleUrls: ['./comments.component.scss']
})
export class CommentsComponent implements OnInit {
  public comments: IComment[] = [];
  public commentBody: string = '';


  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getComments('1').then(res => {
      this.comments = res;
    })
  }

  createComment(body){
    this.provider.createComment(body, '1').then(res => {

    })
  }

}
