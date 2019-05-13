import { IUser } from './user';
import {IArticle} from './article';

export interface IComment {
  id: number;
  body: string;
  date_published: any;
  created_by: IUser;
  article: IArticle;
}
