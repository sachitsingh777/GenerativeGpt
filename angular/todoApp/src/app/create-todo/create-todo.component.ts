import { Component, Input } from '@angular/core';
import { Todo } from '../shared/interfaces/todo';
import { TodoService } from '../shared/services/todo.service';


@Component({
  selector: 'app-create-todo',
  template: `
  <h2>Create Todo</h2>
  <form (ngSubmit)="createTodo()">
    <label>Title:</label>
    <input type="text" name="title" [(ngModel)]="newTodo.title" required>
    <label>Description:</label>
    <textarea name="description" [(ngModel)]="newTodo.description" required></textarea>
    <button type="submit">Create</button>
  </form>
  
  `,
  styles: [`h2 {
    color: #333;
  }
  
  form {
    margin-top: 10px;
  }
  
  label {
    display: block;
    margin-top: 10px;
    color: #333;
  }
  
  input[type="text"],
  textarea {
    width: 100%;
    padding: 5px;
    border: 1px solid #ccc;
  }
  
  button[type="submit"] {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
  }
  `]
})
export class CreateTodoComponent {
  newTodo: Todo = {
    id: 0,
    title: '',
    description: '',
    completed: false
  };

  constructor(private todoService: TodoService) { }

  createTodo() {
    this.todoService.createTodo(this.newTodo);
    this.newTodo = {
      id: 0,
      title: '',
      description: '',
      completed: false
    };
  }
}
