import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

interface SignInResponse {
  token: string;
}

interface SignUpResponse {
  message: string;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  signIn(email: string, password:string): Observable<SignInResponse>{
    const url = 'http://127.0.0.1:8000/users/signin/';
    const body = {email: email, password: password};
    return this.http.post<SignInResponse>(url, body).pipe(
      tap(response => {
        localStorage.setItem('token', response.token);
      }),
    );
  }

  signUp(firstName: string, lastName: string, email: string, password:string, group:string): Observable<SignUpResponse>{
    const url = 'http://127.0.0.1:8000/users/signup/';
    const body = {first_name: firstName, last_name: lastName, email:email, password: password, group: group};
    return this.http.post<SignUpResponse>(url, body)
  }

  getToken(): string | null {
    return localStorage.getItem('token');
  }

}
