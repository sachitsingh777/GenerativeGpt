import { Component, Input } from '@angular/core';
import { Todo } from '../shared/interfaces/todo';
import { TodoService } from '../shared/services/todo.service';

@Component({
  selector: 'app-todo-item',
  template: `
    <div>
      <input type="checkbox" [(ngModel)]="todo.completed">
      <span [ngStyle]="{ 'text-decoration': todo.completed ? 'line-through' : 'none' }">{{ todo.title }}</span>
      <button (click)="deleteTodo()">Delete</button>
    </div>
  `,
  styles: [`div {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  
  input[type="checkbox"] {
    margin-right: 10px;
  }
  
  span {
    flex-grow: 1;
    color: #333;
  }
  
  button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
  }
  `]
})
export class TodoItemComponent {
  @Input() todo: Todo = { id: 0, title: '', description: '', completed: false };


  constructor(private todoService: TodoService) { }

  deleteTodo() {
    this.todoService.deleteTodo(this.todo.id);
  }
}

