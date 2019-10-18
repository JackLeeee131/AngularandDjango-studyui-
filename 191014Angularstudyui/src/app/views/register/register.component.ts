import { Component,OnInit } from '@angular/core';
import { UserService } from '../../service/user.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: 'register.component.html',
  providers:[UserService]
})
export class RegisterComponent implements OnInit{

  register;

  constructor (private userService: UserService){

  }
  ngOnInit(){
    this.register = {
      username: '',
      email: '',
      pasword: '',
      repassword:''
    }
  }
  registerUser(){
    console.log('121')
    this.userService.registerNewUser(this.register).subscribe(
      response =>{
        alert('User' + this.register.username + 'has been created')
      },
      error => console.log('error', error)
    );
  }

}
