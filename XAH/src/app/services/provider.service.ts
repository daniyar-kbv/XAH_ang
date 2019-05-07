import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { IAuthResponse } from '../models/authResponse'


@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{

  private baseUrl = 'http://127.0.0.1:8000/api/';

  constructor(http: HttpClient) {
    super(http);
  }

  login(username: any, password: any): Promise<IAuthResponse> {
    return this.post(this.baseUrl + 'login/', {
      username: username,
      password: password
    })
  }
  
  logout(): Promise<any> {
    return this.post(this.baseUrl + 'logout/', {});
  }
}
