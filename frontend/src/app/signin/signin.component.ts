import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css'],
})
export class SigninComponent {
  email: string = '';
  password: string = '';
  errorMessage: string = '';
  emptyEmail: string = '';
  emptyPassword: string = '';

  constructor(private router: Router, private authService: AuthService) {}

  onSubmit() {
    this.emptyEmail = '';
    this.emptyPassword = '';
    this.errorMessage = '';
    if (this.email && this.password) {
      this.authService.signIn(this.email, this.password).subscribe({
        next: (response) => {
          this.router.navigate(['/sols']);
        },
        error: (error) => {
          if ('email' in error.error) {
            this.errorMessage = error.error.email;
          } else {
            this.errorMessage = error.error.non_field_errors;
          }
        },
      });
    }
    if (this.email == ''){
        this.emptyEmail = "Email field is empty"
    } 
    if (this.password ==''){
        this.emptyPassword = "Password field is empty"
    }
  }
}
