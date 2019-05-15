import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import {Location} from '@angular/common';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  public username: any='';
  public password: any='';

  constructor(private provider: ProviderService, private location: Location) { }

  ngOnInit() {
  }

  login(){
    if (this.username != '' && this.password != ''){
      this.provider.login(this.username, this.password).then(res => {
        localStorage.setItem('Token', res.token);
        localStorage.setItem('username', this.username);
        this.location.back();
        location.reload();
      })
    }
  }

}
