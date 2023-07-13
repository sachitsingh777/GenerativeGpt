import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
  <header>
  <nav>
    <ul>
      <li><a routerLink="/todos" routerLinkActive="active">Todos</a></li>
      <li><a routerLink="/create" routerLinkActive="active">Create</a></li>
    </ul>
  </nav>
</header>

    <router-outlet></router-outlet>
  `,
  styles: [`
  header {
    background-color: #333;
    padding: 10px;
  }

  nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
  }

  nav ul li {
    display: inline;
    margin-right: 10px;
  }

  nav ul li a {
    color: #fff;
    text-decoration: none;
  }

  nav ul li a.active {
    font-weight: bold;
  }
`]
})
export class AppComponent {
}
