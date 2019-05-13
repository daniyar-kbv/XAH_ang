import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  isLogged = false;
  username = '';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    if (localStorage.getItem('Token') && localStorage.getItem('username')){
      this.isLogged = true;
      this.username = localStorage.getItem('username');
    }
  }

  logout(){
    this.provider.logout().then(res => {
      localStorage.clear();
      this.isLogged = false;
      this.username = '';
    })
  }

}
