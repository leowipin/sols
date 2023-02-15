import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

interface SignInResponse {
  token: string;
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

  getToken(): string | null {
    return localStorage.getItem('token');
  }

}
