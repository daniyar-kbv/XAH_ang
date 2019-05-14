import { IUser } from './user';
import { IComment } from './comment'

export interface ICommentLike {
  id: number;
  owner: IUser;
  comment: IComment;
}
