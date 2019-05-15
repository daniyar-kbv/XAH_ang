import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { ActivatedRoute } from '@angular/router';
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
  public articleId: string;


  constructor(private provider: ProviderService, private route: ActivatedRoute) { }

  ngOnInit() {
    this.articleId = this.route.snapshot.paramMap.get('articleId');
    // console.log(this.articleId);
    this.provider.getComments(this.articleId).then(res => {
      console.log(res);
      this.comments = res;
      this.provider.getCommentLikes().then(res1 => {
        this.likes = res1;
      })
    })
  }

  createComment(body){
    console.log("button clicked")
    this.provider.createComment(body, this.articleId).then(res => {
      console.log(res);
      this.provider.getComments(this.articleId).then(ress => {
        console.log(ress);
        this.comments = ress;
      })
    }).catch( res => {
      alert(res.message)
    })
  }

  putCommentLike() {
    this.provider.putCommentLike().then(res => {
      this.likes.push(res);
    }).catch(res => {
      this.likes.pop();
    })
  }

  // putCommentLike() {
  //   this.provider.putCommentLike().then(res => {
  //     this.likes.push(res);
  //   }).catch(res => {
  //     this.likes.pop();
  //   })
  // }

}
