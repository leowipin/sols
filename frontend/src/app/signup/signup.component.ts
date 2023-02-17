import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent {

  firstName: string = '';
  lastName: string = '';
  email: string = '';
  password: string = '';
  confirmPassword: string = '';
  group: string = 'client';
  matchErrorPassword = '';
  errorMessage: string = '';
  succesfulMessage: string = '';
  emptyFirstName: string = '';
  emptyLastName: string = '';
  emptyEmail: string = '';
  emptyPassword: string = ''
  emptyConfirmPassword: string = '';

  constructor(private router: Router, private authService: AuthService) {}

  onSubmit(){
    this.errorMessage = '';
    this.emptyFirstName = '';
    this.emptyLastName = '';
    this.emptyEmail = '';
    this.emptyPassword = '';
    this.emptyConfirmPassword = '';
    this.matchErrorPassword = '';
    if(this.firstName && this.lastName && this.email && this.password && this.passwordsMatch){
      this.authService.signUp(this.firstName, this.lastName, this.email, this.password, this.group).subscribe({
        next: (response) => {
          this.succesfulMessage = response.message;
        },
        error: (error) => {
          if ('email' in error.error) {
            this.errorMessage = error.error.email;
          } 
        },});
    }
    if(this.firstName == ''){
      this.emptyFirstName = "First name field is empty."
    }
    if(this.lastName == ''){
      this.emptyLastName = "Last name name field is empty."
    }
    if(this.email == ''){
      this.emptyEmail = "Email field is empty."
    }
    if(this.password == ''){
      this.emptyPassword = "Password field is empty."
    }
    if(this.confirmPassword == ''){
      this.emptyConfirmPassword = "Confirm password field is empty."
    }
    if(!this.passwordsMatch){
      this.matchErrorPassword = "Password does not match"
    }
  }

  get passwordsMatch(): boolean {
    return this.password === this.confirmPassword;
  }

}
