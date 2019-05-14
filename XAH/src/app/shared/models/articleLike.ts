import { IUser } from './user';
import { IArticle } from './article'

export interface IArticleLike {
  id: number;
  owner: IUser;
  comment: IArticle;
}
