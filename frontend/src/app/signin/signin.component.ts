import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent {

  username: string = '';
  password: string = '';
  
  constructor(private router: Router) { }

  onSubmit() {    
    console.log(this.username);
    console.log(this.password);
    this.router.navigate(['/sols']);
  }

}
