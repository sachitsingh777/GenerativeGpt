import { Component, OnInit } from '@angular/core';
import { Todo } from '../shared/interfaces/todo';
import { TodoService } from '../shared/services/todo.service';

@Component({
  selector: 'app-todo-list',
  template: `
  <h2>Todo List</h2>
<ul>
  <li *ngFor="let todo of todos">
    {{ todo.title }} -{{todo.description}}
  </li>
</ul>

  `,
  styles: [`h2 {
    color: #333;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 10px;
  }
  `]
})
export class TodoListComponent implements OnInit {
  todos: Todo[] = [];
  constructor(private todoService: TodoService) { }

  ngOnInit() {
    this.todos = this.todoService.getTodos();
  }
}

