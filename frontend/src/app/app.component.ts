import {Component, OnInit, OnDestroy} from '@angular/core';

import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'app';
  movieData: JSON;

  constructor(private httpClient: HttpClient) {
  }

  ngOnInit() {
  }

  allMovieData() {
    this.httpClient.get('http://0.0.0.0:5000/movies').subscribe(data => {
      this.movieData = data as JSON;
      console.log(this.movieData);
    })
}
}
