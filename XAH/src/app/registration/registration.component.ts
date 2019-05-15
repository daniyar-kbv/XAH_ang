import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import {Location} from '@angular/common';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss']
})
export class RegistrationComponent implements OnInit {
  public username: any='';
  public password: any='';
  public email: any='';

  constructor(private provider: ProviderService, private location: Location) { }

  ngOnInit() {

  }

  register(){
    if (this.username != '' && this.password != ''){
      this.provider.register(this.username, this.password, this.email).then(res => {
        this.username = '';
        this.password = '';
        this.email = '';
        this.location.back();
      })
    }
  }

}
