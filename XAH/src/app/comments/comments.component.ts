import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { IComment } from '../shared/models/comment';
import { ICommentLike } from '../shared/models/commentLike'

@Component({
  selector: 'app-comments',
  templateUrl: './comments.component.html',
  styleUrls: ['./comments.component.scss']
})
export class CommentsComponent implements OnInit {
  public comments: IComment[] = [];
  public commentBody: string = '';
  public likes: ICommentLike[] = [];


  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getComments('1').then(res => {
      this.comments = res;
      this.provider.getCommentLikes().then(res1 => {
        this.likes = res1;
      })
    })
  }

  createComment(body){
    this.provider.createComment(body, '1').then(res => {
      this.provider.getComments('1').then(ress => {
        this.comments = ress;
      })
    })
  }

  putCommentLike() {
    this.provider.putCommentLike().then(res => {
      this.likes.push(res);
    }).catch(res => {
      this.likes.pop();
    })
  }

}
