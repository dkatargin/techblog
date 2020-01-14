import React, { Component } from 'react';
import { Router, Switch, Route } from 'react-router-dom'
import { createBrowserHistory } from 'history'
import IndexScreen from './screens/IndexScreen'
import EntityScreen from "./screens/EntityScreen";

const history = createBrowserHistory();

class App extends Component {
  render() {
    return (
       <Router history={history}>
            <section className="b-page">
            <Switch>
                <Route path="/:slug/" component={EntityScreen} />
                <Route path="/" component={IndexScreen} />
            </Switch>
        </section>
    </Router>
    );
  }
}

export default App;
