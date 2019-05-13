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
  // public task_lists: ITaskList[] = [];


  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getComments('1').then(res => {
      this.comments = res;
    })
    // this.provider.getTaskLists().then(res => {
    //   this.task_lists = res;
    // })
  }

}
