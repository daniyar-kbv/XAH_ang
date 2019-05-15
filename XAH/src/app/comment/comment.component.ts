import { Component, OnInit, Input } from '@angular/core';
import {IComment} from '../shared/models/comment';
import {ProviderService} from '../shared/services/provider.service';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss']
})
export class CommentComponent implements OnInit {
  @Input() commentId: any;
  public comment: IComment;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getComment(this.commentId).then(res => {
      this.comment = res;
    })
  }

}
