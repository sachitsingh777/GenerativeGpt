import { Injectable } from '@angular/core';
import { Todo } from '../interfaces/todo';

@Injectable({
  providedIn: 'root'
})
export class TodoService {
  todos: Todo[] = [];

  createTodo(todo: Todo) {
    todo.id = this.todos.length + 1;
    this.todos.push(todo);
  }

  getTodos() {
    return this.todos;
  }

  deleteTodo(todoId: number) {
    const index = this.todos.findIndex(todo => todo.id === todoId);
    if (index !== -1) {
      this.todos.splice(index, 1);
    }
  }
}
