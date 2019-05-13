import {IUser} from './user';
import {ICategory} from './category';

export interface IArticle {
  id: number,
  title: string,
  body: string,
  imageUrl: string,
  views: number,
  created_at: any,
  created_by: IUser,
  category: ICategory
}
