import logo from './logo.svg';
import './App.css';
import {BrowserRouter as Router,Routes,Route,Link} from "react-router-dom";

import Washingmachine from './components/washingmachine'
import Language from './components/language'
import Home from './my_app/home'

import Stories from './components/stories'
import Jsondata from './components/jsondata'

function App() {
  return (
    <>
    

      <Router>
        <Routes>
          <Route path={"/"} element={<Home />}></Route> 
          <Route path='/Washingmachine' element ={<Washingmachine />}></Route>
          <Route path='/Home' element ={<Home />}></Route>
          <Route path='/Language' element ={<Language />}></Route>
          <Route path='/Stories' element={<Stories />}></Route>
          <Route path='/Jsondata' element={<Jsondata />}></Route>
        </Routes>
      </Router>
    </>
  
  );
}

export default App;
