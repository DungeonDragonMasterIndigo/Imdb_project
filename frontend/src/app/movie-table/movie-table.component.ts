import { Component, OnInit } from '@angular/core';
import { MovieService } from '../services/movie.service';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';
import {DataSource} from '@angular/cdk/collections';
import { Movie } from '../models/movie.model';

@Component({
  selector: 'movietable',
  templateUrl: './movie-table.component.html',
  styleUrls: ['./movie-table.component.css']
})
export class MovieTableComponent implements OnInit {
  dataSource = new MovieDataSource(this.movieService);
  displayedColumns = ["titleId",  "ordering", "title"];
  constructor(private movieService: MovieService) { }

  ngOnInit() {
  }
}

export class MovieDataSource extends DataSource<any> {
  constructor(private userService: MovieService) {
    super();
  }
  connect(): Observable<Movie[]> {
    return this.userService.getMovies();
  }
  disconnect() {}
}
