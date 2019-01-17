import { Injectable }   from '@angular/core';
import { HttpClient }   from '@angular/common/http';
import { Observable }   from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import { Movie } from '../models/movie.model';

@Injectable()
export class MovieService {

  private serviceUrl = 'http://0.0.0.0:5000/movies';

  constructor(private http: HttpClient) { }

  getMovies(): Observable<Movie[]> {
    return this.http.get<Movie[]>(this.serviceUrl);
  }

}
